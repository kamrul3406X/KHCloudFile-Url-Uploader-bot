import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6163953668:AAFQQPv-hS1esd2VQmW7JYzInkPSU57Q3RM",)
    # The Telegram API things
    APP_ID = int(os.environ.get("26562439", 12345))
    API_HASH = os.environ.get("9c7481e79c58d0e66fe8c4343a9e414d")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1761465389").split())
    # MongoDB information
    DATABASE_URI = environ['mongodb+srv://kamrulhasan913406:kamrulhasan913406@cluster0.i56slcw.mongodb.net/?retryWrites=true&w=majority']
    DATABASE_NAME = environ['kamrulhasan913406']
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/3d73f9cb444cb8140edda.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 40960
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "@KHCloudFile"
    #Admin id is stored in 
    LAZY_DEVELOPER = set(int(x) for x in os.environ.get("Admin", "1761465389").split())
