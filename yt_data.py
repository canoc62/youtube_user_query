from apiclient.discovery import build
import json

# devKey - Google Developer API Key

def build_youtube_service(devKey):
    api = 'youtube' 
    api_version = 'v3'
    youtube_service = build(api, api_version, developerKey=devKey)
    return youtube_service

def get_channel_info(youtube_service, youtube_username): 

    user_list = {
       "users": [

        ]
    }

    results = youtube_service.channels().list(
        part="snippet, statistics",
        forUsername=youtube_username
    ).execute()

    user_object = {
        "meta": {
            "username": youtube_username
        },
        "channels": [

        ]
    }

    for item in results["items"]:
        channel_title = item["snippet"]["title"]
        channel_description = item["snippet"]["description"]
        subscriber_count = item["statistics"]["subscriberCount"]

        channel = {
            "channel_title": channel_title,
            "channel_description": channel_description,
            "subscriber_count": subscriber_count
        }
    
        user_object["channels"].append(channel)

    user_list["users"].append(
        user_object
    )

    youtube_file = 'youtube_%s.json' %(youtube_username)
    f = open(youtube_file, 'w')
    f.write(json.dumps(user_list, indent=4, sort_keys=False))
    f.close()
         

# Test
'''
youtube = build_youtube_service(
    'AIzaSyAM5ytZfxRt9lAJBZkCDG8aFATE9030mAg'
)

username = "RealRobReport"
get_channel_info(youtube, username)
'''





