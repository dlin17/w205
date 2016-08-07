from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

conn = psycopg2.connect(
    database="tcount", user="postgres", password="pass", host="localhost", port="5432")
curs = conn.cursor()
curs.execute("DELETE FROM tweetwordcount")
conn.commit()


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0].replace("'",r"\'")

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.

        # Increment the local count
        self.counts[word] += 1

        if self.counts[word] == 1:
            curs.execute("""INSERT INTO tweetwordcount (word, count) VALUES ('%s', 1)""" % word)
            conn.commit()
        else:
            curs.execute("UPDATE tweetwordcount set count = %s where word = '%s'" % (
                self.counts[word], word))
            conn.commit()

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
