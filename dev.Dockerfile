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
    python3-pip \
 && rm -rf /var/lib/apt/lists/* 

#might need to further research the differences between expose and publish
EXPOSE 5000 

RUN pip3 install flask flask_restful flask_apispec mininet

WORKDIR /root/toynet-mininet
#Docker ignore file to leave files out
COPY . . 
RUN chmod +x /root/toynet-mininet/entrypoint.sh


ENV FLASK_APP=flasksrc
ENV FLASK_ENV=development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENTRYPOINT ["/root/toynet-mininet/entrypoint.sh"]
