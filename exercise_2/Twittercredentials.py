import tweepy

consumer_key = "cWbUtUlTKAmmqy6dvmAqCN2ES";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "AiQD9yxnxiW7wztG1ooRcCe862dfcN0r4of0MpsTa9Y3tbfJ3o";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "2812253327-DiPF2EIYrPHU2U9V8d3uH8qttGpwJSWcVyt5Otn";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "KvvXHUL6UNKJI7smEbTjwvztvRdnOkajphve8wKMGmKiF";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



