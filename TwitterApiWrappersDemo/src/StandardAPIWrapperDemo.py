import tweepy

import src.TwitterCredentialManagement as tcm

TEST_TWITTER_USERNAME = "ScottSSalisbur1"

if __name__ == '__main__':
    print("running tweepy demo program")

    apiKey, apiSecretKey, accessToken, accessTokenSecret = tcm.fetchAPICredentials()

    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)

    twitterStandardApi = tweepy.API(auth)

    try:
        twitterStandardApi.verify_credentials()
        print("Twitter credentials valid")
    except:
        print("Tweepy unable to authenticate with Twitter")

    user = twitterStandardApi.get_user(TEST_TWITTER_USERNAME)
    print("Test User Details:")
    print("Account creation date= " + str(user.created_at))
    print("ID String= " + user.id_str)

    # todo add toy trend fetch
