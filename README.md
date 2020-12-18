run `docker build -t toynet .`

run `docker run -v sample.xml:/root/toynet-mininet/topo.xml toynet`

For development build:
run `docker build -t toynet -f dev.Dockerfile .` 
