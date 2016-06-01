import youtube_user_query

youtube = youtube_user_query.build_youtube_service(
	'AIzaSyAM5ytZfxRt9lAJBZkCDG8aFATE9030mAg'
)

youtube_username = "RealRobReport"
youtube_user_query.get_channel_info(youtube, youtube_username)

