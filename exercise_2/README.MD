# Storm Twitter Streaming App

## Requirements

Python 2.7.10+
psycopg2
tweepy
lein
streamparse

## Postgres

An instances of postgres on localhost:5432 must be running. Execute the following code in psql

```
CREATE DATABASE tcount;

\c tcount

CREATE TABLE tweetwordcount(
    word TEXT PRIMARY KEY     NOT NULL,
    count INT     NOT NULL);
```

## Twitter OAuth Credentials

A file named `credentials.py` needs to be created in the spouts folder with the following code

```
def auth_get(auth_key):
    twitter_credentials = {
        "consumer_key"        :  "<enter your consumer key>",
        "consumer_secret"     :  "<enter your consumer secret key>",
        "access_token"        :  "<enter your access token>",
        "access_token_secret" :  "<enter your access token secret key>",
    }

    if auth_key in twitter_credentials:
        return twitter_credentials[auth_key]
    return None
```

## Running

`sparse run`

## Analysis

Search for number of times a word is mentioned

`python finalresults.py your_word`

Search for words between k1 and k2 number of mentions

`python histogram.py k1,k2`