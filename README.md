run `docker build -t toynet .`

run `docker run --privileged -v sample.xml:/root/toynet-mininet/topo.xml -v /lib/modules:/lib/modules toynet`

For development build:
run `docker build -t toynet -f dev.Dockerfile .` 


Troubleshooting:
docker build --network=host -t toynet -f dev.Dockerfile .
