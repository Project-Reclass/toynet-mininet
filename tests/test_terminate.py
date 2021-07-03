import pytest
import json
from flasksrc import create_app

@pytest.fixture
def client():
    app = create_app()
    yield app.test_client()

def test_terminate_post(client):
    '''test terminate POST functionality'''
    #empty, i.e. terminate not specified
    rv = client.post(
        '/api/terminate',
        json = {
        },
    )
    assert rv.status_code == 422
    
    #validate the post terminate:True fails if state is None
    rv = client.post(
        '/api/terminate',
        json = {
            'terminate': True,
        },
    )
    assert rv.status_code == 500
    rv_json = json.loads(rv.data.decode('utf-8'))
    assert rv_json['message'] == 'terminate request failed'

    #validate the post terminate:False succeeds if state is None
    rv = client.post(
        '/api/terminate',
        json = {
            'terminate': False,
        },
    )
    assert rv.status_code == 200
    rv_json = json.loads(rv.data.decode('utf-8'))
    assert rv_json['terminated'] == False

    #create state
    with open('sample.xml','r') as sample_topo:
        rv = client.post(
            '/api/topo',
            json = { 
                'topology': sample_topo.read(),
            },
        )
    assert rv.status_code == 200

    #validate the post terminate:False succeeds if state is not None
    rv = client.post(
        '/api/terminate',
        json = {
            'terminate': False,
        },
    )
    assert rv.status_code == 200
    rv_json = json.loads(rv.data.decode('utf-8'))
    assert rv_json['terminated'] == False

    #validate the post terminate:True succeeds if state is not None (should still be set after previous test)
    rv = client.post(
        '/api/terminate',
        json = {
            'terminate': True,
        },
    )
    assert rv.status_code == 200
    rv_json = json.loads(rv.data.decode('utf-8'))
    assert rv_json['terminated'] == True
