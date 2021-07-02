# Mininet ToyNet

This module containerizes and provides interfaces for the backend of ToyNet to
interface with the Mininet emulator implementing the topology that a user builds.

## Building

Run `docker build -t toynet .` to build the production image using the `Dockerfile`.
For the development image, run `docker build -t toynet-dev -f dev.Dockerfile .`

It will take several minutes the first time for both images, but after the
majority of the images get cached by Docker it will be much faster.

## Running

Assuming you tagged the images as specified above:

To run the production image:
run `docker run --privileged -v sample.xml:/root/toynet-mininet/topo.xml -v /lib/modules:/lib/modules toynet`

And to run the development image:
run `docker run --privileged -v sample.xml:/root/toynet-mininet/topo.xml -v /lib/modules:/lib/modules toynet-dev`

# Installing Dependencies

This library makes some functionality of the Docker Python API more readily
accessible for your use case. This library is intended to facilitate Flask
managing Mininet containers local to its running instance.

## External Repositories

Download mininet: `git submodule update --init --recursive` 

## Installing Python Dependencies

If you are testing code that is managing Docker (therefore cannot be tested in
a container: e.g. `tests/test_orchestration.py`), you can setup your virtual
environment by:

Linux / MacOS:
```
python3 -m venv venv
```

Windows:
```
py -3 -m venv venv
```

Then activate it:

Linux / MacOS:
```
. venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

Make sure you are using Python 3.x, recommended Python 3.7. Install
dependencies from the `requirements.txt` with:
`pip3 install -r requirements.txt`

Run the `deactivate` command to exit the virtual environment.

## Testing

Run `make test` from the project root directory.

# Future Work

We need to expand this functionality to manage remote Docker instances so we
can decouple Flask from the Mininet containers. In the more distant future, the
Mininet containers will run in a Kubernetes cluster.
