import sys

import psycopg2


conn = psycopg2.connect(
    database="tcount", user="postgres", password="pass", host="localhost", port="5432")
curs = conn.cursor()

try:
    keyword = sys.argv[1]

    curs.execute("SELECT count FROM tweetwordcount WHERE word = '%s'" % keyword)
    c = curs.fetchone()[0]

    print "Total number of occurences of '%s': %s" % (keyword, c)

except:
    curs.execute("SELECT * FROM tweetwordcount ORDER BY count desc")
    for row in curs.fetchall():
        print '%s: %s' %(row[0], row[1])
