# built from github user: iwaseyusuke
# Apache License v2.0
# FROM iwaseyusuke/mininet
# Run command
# 
# 	-v :/root/topo.xml

FROM ubuntu:20.04

USER root
WORKDIR /root

#our entrypoint.sh should take an XML file and use that to instantiate mininet
#COPY entrypoint.sh /root


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
#    tcpdump \
#    vim \
#    x11-xserver-utils \
#    xterm \
 && rm -rf /var/lib/apt/lists/* 
# && chmod +x /root/entrypoint.sh

RUN git clone https://github.com/Project-Reclass/toynet-mininet.git && cd toynet-mininet && git submodule init && chmod +x /root/toynet-mininet/entrypoint.sh

WORKDIR /root/toynet-mininet

#EXPOSE 6633 6653 6640

ENTRYPOINT ["/root/toynet-mininet/entrypoint.sh"]
