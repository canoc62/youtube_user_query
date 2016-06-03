from apiclient.discovery import build
import json

# devKey - Google Developer API Key

def build_youtube_service(devKey):
    api = 'youtube' 
    api_version = 'v3'
    youtube_service = build(api, api_version, developerKey=devKey)
    return youtube_service


def get_channel_id_list(youtube_service):

    channel_id_list = []

    video_list = youtube_service.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="US",

    ).execute()

    for video in video_list["items"]:
        channel_id_list.append(video["snippet"]["channelId"])

    return channel_id_list


def create_channel_list(youtube_service, user_list):

    for channel_id in user_list:
        write_channel_info(youtube_service, channel_id)


def write_channel_info(youtube_service, channel_id): 

    '''
    user_list = {
        "users": [

        ]
    }
    '''

    results = youtube_service.channels().list(
        part="snippet, statistics",
        id=channel_id
    ).execute()

    user_object = {
        "meta": {
            "channel_id": channel_id
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

    '''
    user_list["users"].append(
        user_object
    )
    '''

    # FIND A WAY TO OPEN EXTERNAL FILE AND WRITE TO SPECIFIC 
    # PART OF THAT FILE (ADD CHANNEL TO USER(CHANNEL) LIST IN JSON OBJECT)
    youtube_file = 'youtube_%s.json' %(channel_id)
    f = open(youtube_file, 'w')
    f.write(json.dumps(user_object, indent=4, sort_keys=False))
    f.close()
         

# Test
'''
youtube = build_youtube_service(
    'AIzaSyAM5ytZfxRt9lAJBZkCDG8aFATE9030mAg'
)
'''
