#from flask_pymongo import PyMongo
import pytest
import mongomock


# Fixture to mocks pymongo instance which points to a mock instance of mongodb
@pytest.fixture(autouse=True,scope='module')
def mock_pymongo():
    client = mongomock.MongoClient()
    return client