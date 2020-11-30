from pymongo import MongoClient
MC=MongoClient("39.102.200.61",27017)
MONGODB=MC["flask_toy"]
class DebugConfig():
    DEBUG=True
    SECRET_KEY="!@#QWE"

class TestingConfig():
    TESTING=True
    SECRET_KEY="!@#QWE"