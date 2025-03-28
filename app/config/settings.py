import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    TESTING = os.getenv("TESTING", "False").lower() in ("true", "1", "t")
    
    STATIC_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'static')

class APIConfig:
    BING_COOKIE = os.getenv("BingCookie")
    SECURE_1PSID = os.getenv("Secure1PSID")
    SECURE_1PSIDTS = os.getenv("Secure1PSIDTS")
    LANG = os.getenv("LANG")
