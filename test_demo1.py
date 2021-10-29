import demo1
import twitter

api = twitter.Api(consumer_key='qTzLMH5SOWoTO3EthGybTU9Uh',
                  consumer_secret='k6zgpvS59uBZTXAvlPOkwwdbAM45fPIGLmrMpl2V1avGbSFWuI',
                  access_token_key='1440792971234873344-DYQVxYr4pygqo4DNpwkP34c19EEhMB',
                  access_token_secret='piVEkV1MgGPnJAnMNLDxoaAzBouSGCgzVGc2nNX10DBOq')


def test_finduser():
    users = api.GetFriends()

    followers = api.GetFollowers()


def test_submiting():
    status = api.PostUpdate('I love playing games')
    # print(status.text)

    status = api.PostUpdate('who kill me?')

    status = api.PostUpdate('jz likes drinking coke')


def test_getdetails():
    print(api.GetSearch(term='Boston University', since=2021 - 4 - 7, count=10))
