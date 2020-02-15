import os

import searchtweets as st

ENDPOINT_ENV_VAR = "SEARCHTWEETS_ENDPOINT"

TWITTER_PREMIUM_API_ENDPOINT_FORMAT = "https://api.twitter.com/{}/tweets/search/{}/{}.json"
TWITTER_API_VERSION = "1.1"
MONTH_SEARCH_PRODUCT = "30day"
FULL_ARCHIVE_SEARCH_PRODUCT = "fullarchive"
MONTH_SEARCH_DEV_ENV_LABEL = "SSBase30DayEnv"
FULL_ARCHIVE_SEARCH_DEV_ENV_LABEL = "SSBaseFullArchiveEnv"

PREMIUM_30_DAY_ENDPOINT = TWITTER_PREMIUM_API_ENDPOINT_FORMAT.format(TWITTER_API_VERSION, MONTH_SEARCH_PRODUCT,
                                                                     MONTH_SEARCH_DEV_ENV_LABEL)
PREMIUM_FULL_ARCHIVE_ENDPOINT = TWITTER_PREMIUM_API_ENDPOINT_FORMAT.format(TWITTER_API_VERSION,
                                                                           FULL_ARCHIVE_SEARCH_PRODUCT,
                                                                           FULL_ARCHIVE_SEARCH_DEV_ENV_LABEL)


def getPremiumEndpointCreds(endpointType):
    os.environ[ENDPOINT_ENV_VAR] = endpointType;

    searchArgs = st.load_credentials(filename="NoCredsFile.yaml", account_type="premium", yaml_key="dummyYamlKey")
    print(searchArgs)

    # cleaning up this temporary environment variable to avoid causing a side effect
    del os.environ[ENDPOINT_ENV_VAR]

    return searchArgs


if __name__ == '__main__':
    print("running search-tweets demo program")

    print(os.environ.get("SEARCHTWEETS_ACCOUNT_TYPE"))
    print(os.environ.get("SEARCHTWEETS_CONSUMER_KEY"))
    print(os.environ.get("SEARCHTWEETS_CONSUMER_SECRET"))

    monthSearchArgs = getPremiumEndpointCreds(PREMIUM_30_DAY_ENDPOINT)
