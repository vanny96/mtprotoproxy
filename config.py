import os

PORT = int(os.getenv("MTPROTO_PORT", 443))

# name -> secret (32 hex chars)
# USERS environment variable format: "user1:secret1,user2:secret2"
users_env = os.getenv("MTPROTO_USERS", "tg:00000000000000000000000000000001")
USERS = dict(user.split(":") for user in users_env.split(","))

MODES = {
    "classic": os.getenv("MTPROTO_MODE_CLASSIC", "False").lower() == "true",
    "secure": os.getenv("MTPROTO_MODE_SECURE", "False").lower() == "true",
    "tls": os.getenv("MTPROTO_MODE_TLS", "True").lower() == "true"
}

TLS_DOMAIN = os.getenv("MTPROTO_TLS_DOMAIN", "www.google.com")
AD_TAG = os.getenv("MTPROTO_AD_TAG", None)