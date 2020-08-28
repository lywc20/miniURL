import os
import tempfile

import pytest

from miniurl import create_app

@pytest.fixture
def app():
    #db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
    #set up mock database with mongomock

    #miniurl.app.config['TESTING'] = True
    app = create_app(True)
    #app = create_app({"TESTING":True})


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing

## Write for URL validation 

#@pytest.fixture
#def app():
#    yield main

#def test_empty_db(client):

 #   rv = client.get('/')
 #   assert b'No entries here so far' in rv.data
