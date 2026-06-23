from .library import *

admin_user_id = 8599705796 #<--- آیدی ادمین
api_id = 33494882 #<--- آی پی آی آیدی
api_hash = 'a85812b381be0c0f5c1e58bd79ca3509' #<--- ای پی آی هش
helper_username = 'myselfux_bot' #<--- یوزر ربات هلپر بدون @
bot_token = '8817276845:AAEYqLQA7Oa0FWtO2QtpAFZt3osXHYZrU5w' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
