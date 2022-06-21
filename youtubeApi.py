import googleapiclient.discovery
import os


def youtube():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBza-dzQvxY-SZkHGAHQaM_DrcMRSFzPw4"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    return youtube
