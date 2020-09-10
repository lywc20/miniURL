import pytest
from miniurl.api.key_generator import *
from flask_pymongo import PyMongo


# Fixture for keygen obj
@pytest.fixture(scope='module')
def keygen_fix(mock_pymongo):
    return KeyGenerator(mock_pymongo)

def test_default_constructor(keygen_fix):
    assert keygen_fix != None

def test_genereateKey(keygen_fix):
    generated_key = keygen_fix.generateKey()
    assert type(generated_key) == str


    generated_key2 = keygen_fix.generateKey()
    assert generated_key2 != generated_key

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

def test_bindUrl(keygen_fix,mock_pymongo):
    shorten_url = 'abcdef'
    url = 'https://www.github.com'
    keygen_fix.bindUrl(shorten_url,url)
    
    assert mock_pymongo.db.collection.find_one({'shorten_url':shorten_url},{'_id':1}) == mock_pymongo.db.collection.find_one({'url':url},{'_id':1})

    shorten_url2 = 'abcdeg'
    url2 = 'https://www.github.org'
    keygen_fix.bindUrl(shorten_url2,url2)

    assert mock_pymongo.db.collection.find_one({'shorten_url':shorten_url2},{'_id':1}) != mock_pymongo.db.collection.find_one({'url':url},{'_id':1})
    
def test_findUrl(keygen_fix,mock_pymongo):
    addr = 'shorten_link'
    assert keygen_fix.findUrl(addr) == None

    mock_pymongo.db.collection.insert_one({
        'shorten_url': addr
    })

    assert keygen_fix.findUrl(addr) != None