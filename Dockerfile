# built from github user: iwaseyusuke
# Apache License v2.0
# FROM iwaseyusuke/mininet
# Run command
# 
# 	-v <XML File Path>:/root/toynet-mininet/topo.xml #mounts the <XML File Path> to /root/toynet-mininet/topo.xml on the container

FROM ubuntu:18.04

USER root
WORKDIR /root

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    git \
    python3-pip \
 && rm -rf /var/lib/apt/lists/* 

RUN pip3 install mininet
RUN git clone https://github.com/Project-Reclass/toynet-mininet.git && cd toynet-mininet && git submodule init && chmod +x /root/toynet-mininet/entrypoint.sh

WORKDIR /root/toynet-mininet

ENTRYPOINT ["/root/toynet-mininet/entrypoint.sh"]
