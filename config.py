from dotenv import load_dotenv
load_dotenv()


import os

class Config:
    SECRET_KEY = 'your_secret_key'
    # Specify database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USER')

    # Email settings
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    MAIL_DEBUG = True

