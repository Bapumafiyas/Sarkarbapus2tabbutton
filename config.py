# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7210056748:AAFbRKFkl3XOrDIjCzZS7xqdzBHnEzV0OWw")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20170562"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "56aa61b4d1198329f24c1602eb3f73d4")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002052438967"))

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database SQL
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Mscmafiacorporation:<8TdhoEYC2hZcGfnC>@cluster0.hxu1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#Database MONGO
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Mscmafiacorporation:<8TdhoEYC2hZcGfnC>@cluster0.hxu1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_NAME = os.environ.get("MONGO_NAME", "filesbyjbls")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001992105804")) 
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001559911506"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "7115098385").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

ADMINS.append(7115098385) 


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
