import os
import tempfile
import pytest
import json
from flasksrc import create_app

@pytest.fixture
def client():
    app = create_app()
    yield app.test_client()

def test_topo_post(client):
    '''Checks the post topology functionality'''
    with open('sample.xml','r') as sample_topo:
        rv = client.post(
            '/api/topo',
            json = { 'topology': sample_topo.read(),},
        )
    assert rv.status_code == 200


