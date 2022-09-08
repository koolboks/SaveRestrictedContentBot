#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("17118701", default=None, cast=int)
API_HASH = config("0ed3280c3fdc037b8febdfbc59536839", default=None)
BOT_TOKEN = config("5409863953:AAHLL9ryGMhh2uUZVwfbrkOihjmIO8sjfKY", default=None)
SESSION = config("BAAo78P6fISlPJh5xb8Bt60dXfU5wpKhM-FjyZST-p1IcBTQynt7r_KrWPLzsSyAdvGnvEhNEUBWgnzZLgCk3yBhBexX6KCgFc-LblWahEzQmOL_Rj-Jpr4DtmqT1zG-Xw7Ap3DIHQv9bl1EKnGAaxwzBSKZlxGck9i6gNiEHzMRJ761OJzqMXEs8b_k_NIrEBVD6DCk3ytBXoYmy32VfHn4Ic9XYag_X3KVJr7KxA_qYtnKPVMxzLqnS4Nn8Qt0ZFhHEP2C-5VrumH3LkUMjZvQQ1A-HLEYJGmVQ25EiHnWXytGOAM2exk2LgapOQ-ojVoNP-QA0lK_lH5codw_5OQYAAAAATwzKGwA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
