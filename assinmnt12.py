# ASSIGNMENT-12
# Let’s learn and practise concepts of API: 
# Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
# An access token is an object that describes the security context of a process or thread.
# The information in a token includes the identity and privileges of the user account associated with the process or thread.
# The security identifier (SID) for the user's account.SIDs for the groups of which the user is a member.
# cnsumer key='PjnBK3XGym4ftdYnJmVO95678'
# cunsumer secret='CYXfjBS5tEFXdFfzioLT13CFioSdB2hxN1qszrQvMKBlva1234'
# access_token='	1011129079666335746-udUl85NhJMs5ELmiiAMCB1UO9y1234'
# access_secret='	Jfg9y6kYnEr6efvTUJWxSMttyclBeJYHXzQHsw72t5678'
  
 
 
 
 
 
 

  
 
# Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup. 
# Microsoft Windows [Version 10.0.14393]
# (c) 2016 Microsoft Corporation. All rights reserved.

# C:\Users\user\Desktop\assign,ent\cls2>nslookup google.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:807::200e
          # 172.217.161.14


# C:\Users\user\Desktop\assign,ent\cls2>nslookup instagram.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    instagram.com
# Addresses:  2406:da00:ff00::23aa:5823
          # 2406:da00:ff00::3448:6dc5
          # 2406:da00:ff00::34c8:afc2
          # 2406:da00:ff00::34cb:8741
          # 2406:da00:ff00::22e9:ffc5
          # 2406:da00:ff00::342c:f9cd
          # 2406:da00:ff00::22e2:135a
          # 2406:da00:ff00::3416:3580
          # 34.224.11.122
          # 52.20.220.177
          # 34.227.141.166
          # 34.194.59.113
          # 34.196.103.119
          # 34.225.221.52
          # 54.210.70.115
          # 34.199.53.7


# C:\Users\user\Desktop\assign,ent\cls2>nslookup amazon.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    amazon.com
# Addresses:  64:ff9b::cdfb:f267
          # 64:ff9b::b020:62a6
          # 64:ff9b::b020:67cd
          # 176.32.98.166
          # 176.32.103.205
          # 205.251.242.103


# C:\Users\user\Desktop\assign,ent\cls2>

# Q.3- Using Tweepy library try to extract tweets from Twitter.\
import tweepy

consumer_key='PjnBK3XGym4ftdYnJmVO910dA'
consumer_secret='CYXfjBS5tEFXdFfzioLT13CFioSdB2hxN1qszrQvMKBlvaWLak'

access_token='1011129079666335746-udUl85NhJMs5ELmiiAMCB1UO9yijnB'
access_secret='Jfg9y6kYnEr6efvTUJWxSMttyclBeJYHXzQHsw72tgVXV'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token,(access_token,access_secret)
api=tweepy.API(auth)

tweets=api.search('#race3',lang='en',count=7,tweet_mode='extended')


for tweet in tweets: 
    print("......")
    print(tweet.full_text)
    print(".....")
    


# ASSIGNMENT-12
# Q.4- What is a difference between library and API . Figure it out with examples.
# Q.5- Try to access Spotify API . Find out some library for it and play some music.-