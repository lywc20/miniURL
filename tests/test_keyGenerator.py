import pytest
from miniurl.api.key_generator import *
from flask_pymongo import PyMongo


# Fixture for keygen obj
@pytest.fixture(scope='module')
def keygen_fix(mock_pymongo):
    return KeyGenerator(mock_pymongo)

def test_genereateKey(keygen_fix):
    print(keygen_fix)
    generated_key = keygen_fix.generateKey()
    assert type(generated_key) == str

def test_available(keygen_fix):
    generated_key = keygen_fix.generateKey()

    assert keygen_fix.available(generated_key) == True
    
    keygen_fix.client.db.collection.insert_one({
        'url': 'www.test.org',
        'shorten_url': generated_key,
        'creation_date': None,
        'expiration': None
    })

    assert keygen_fix.available(generated_key) == False
