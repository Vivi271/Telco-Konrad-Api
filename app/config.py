class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///telco_konrad.db'
    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    API_VERSION = 'v1'
    PORT = 5000