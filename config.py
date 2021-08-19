import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1764154226:AAHQhzmvpVgqgzwbh5CQfd48K9mjXB5v0OU")

    APP_ID = int(os.environ.get("APP_ID", 3945177))

    API_HASH = os.environ.get("API_HASH", "d38af2312a3297963ada65e2ee9dbdad")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
