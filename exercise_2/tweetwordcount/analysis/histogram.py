import sys

import psycopg2

try:
    ll, ul = sys.argv[1].split(",")

    conn = psycopg2.connect(
        database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    curs = conn.cursor()

    curs.execute(
        "SELECT * FROM tweetwordcount WHERE count BETWEEN %s and %s ORDER BY count desc" % (ll, ul))
    for row in curs.fetchall():
        print '%s: %s' % (row[0], row[1])

except:
    print "Enter parameters in form (k1,k2)"
