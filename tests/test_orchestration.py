'''
Unit test suite for ToyNet Docker container orchistration utilities
'''

import os
import pytest

from toynet_manager import ToynetManager

@pytest.fixture
def manager():
    '''
    Instantiate the ToynetManager class
    '''

    yield ToynetManager()

def test_check_resources(manager):
    '''
    Test that the ToynetManager can correctly assess resource constraints
    '''

    # Confirm high/low CPU usage detection
    assert manager.check_cpu_availability(100.0, 100.0, 100.0)
    assert not manager.check_cpu_availability(-1.0, -1.0, -1.0)

    # Confirm high/low memory usage detection
    assert manager.check_memory_availability(100, 0)
    assert not manager.check_memory_availability(0, 1024)

def test_build_image(manager):
    '''
    Test that the ToynetManager can build images as directed
    '''

    # Test invalid filename
    assert not manager.build_mininet_container(dev=False, docker_file='fake_file')
    assert manager.dev_image is None

    # Test development image build
    assert manager.build_mininet_container()
    assert manager.dev_image is not None and manager.dev_image[0].tags == ['toynet-dev:latest']

    # Test production image build
    assert manager.build_mininet_container(False, 'Dockerfile')
    assert manager.prod_image is not None and manager.prod_image[0].tags == ['toynet:latest']

def test_run_container(manager):
    '''
    Test that the ToynetManager can run containers correctly
    '''

    # Build images
    manager.build_mininet_container()
    manager.build_mininet_container(False, 'Dockerfile')

    # Test invalid filename
    no_container = manager.run_mininet_container('fake_file')
    assert no_container == '' and no_container not in manager.running_containers

    # Test development container
    dev_container = manager.run_mininet_container(os.path.abspath('./sample.xml'))
    assert dev_container != '' and dev_container in manager.running_containers

    # Test production container
    prod_container = manager.run_mininet_container(os.path.abspath('./sample.xml'), dev=False)
    assert prod_container != '' and prod_container in manager.running_containers

    # Test killing nonexistent container
    assert not manager.kill_container(None)

    # Test killing development and production containers
    assert manager.kill_container(dev_container)
    assert manager.kill_container(prod_container)
