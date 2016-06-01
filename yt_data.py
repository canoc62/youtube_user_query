from apiclient.discovery import build
import json

# developerKey - Google Developer API Key
youtube_service = build('youtube', 'v3', developerKey="")

user_list = {
    "users": [

    ]
}

# Can use username or channel_id for channel query
def get_channel_info(youtube_service, username): #channel_id):
    results = youtube_service.channels().list(
        part="snippet, statistics",
        forUsername=username
        #id=channel_id
    ).execute()

    user_object = {
        "meta": {
            "username": username
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

    youtube_file = 'youtube_%s.json' %(username)
    f = open(youtube_file, 'w')
    f.write(json.dumps(user_list, indent=4, sort_keys=False))
    f.close()
         

# Test

#yt_channel_id = "UCtblLfYa5QmFUndxGGdp24g"
username = "RealRobReport"
get_channel_info(youtube_service, username)#yt_channel_id)





