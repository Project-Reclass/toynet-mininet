# built from github user: iwaseyusuke
# Apache License v2.0
# FROM iwaseyusuke/mininet
# Run command
# 
# 	-v <XML File Path>:/root/toynet-mininet/topo.xml #mounts the <XML File Path> to /root/toynet-mininet/topo.xml on the container
FROM ubuntu:18.04

USER root
WORKDIR /root

RUN apt-get -y update && apt-get install -y apt-transport-https && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    gcc \
    python3.6-dev \
    python3-pip \
 && rm -rf /var/lib/apt/lists/* 

#might need to further research the differences between expose and publish
EXPOSE 5000 

WORKDIR /root/toynet-mininet
COPY . . 
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt 
RUN chmod +x /root/toynet-mininet/entrypoint.sh /root/toynet-mininet/test-entrypoint.sh

ENV FLASK_APP=flasksrc
ENV FLASK_ENV=development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENTRYPOINT ["/root/toynet-mininet/entrypoint.sh"]
