import twitter

api = twitter.Api(consumer_key='qTzLMH5SOWoTO3EthGybTU9Uh',
                  consumer_secret='k6zgpvS59uBZTXAvlPOkwwdbAM45fPIGLmrMpl2V1avGbSFWuI',
                  access_token_key='1440792971234873344-DYQVxYr4pygqo4DNpwkP34c19EEhMB',
                  access_token_secret='piVEkV1MgGPnJAnMNLDxoaAzBouSGCgzVGc2nNX10DBOq')

# Function2 : Get my Twitter Account info

# print(api.VerifyCredentials())

users = api.GetFriends()
# print([u.name for u in users])

followers = api.GetFollowers()
# print([f.name for f in followers])

# Function2 : Submit Twitter using API

status = api.PostUpdate('I love playing games')
# print(status.text)

status = api.PostUpdate('who kill me?')

status = api.PostUpdate('jz likes drinking coke')

# print(status.text)

# Function3 : Get the website contained messages I wanted, even search for twitter in some special places
print(api.GetSearch(term='Boston University', since=2021 - 4 - 7, count=10))
print(api.GetSearch(term='Kobe Bryant', since=2021 - 4 - 7, count=10))
print(api.GetSearch(term='朱家辉和赵劲舟', since=2021 - 9 - 25, count=10))
print(api.GetSearch(geocode="42.210407,-71.073705,2mi", since=2021-9 - 24))

