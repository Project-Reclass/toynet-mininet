#!/usr/bin/env bash
FILENAME=topo.xml

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

#read XML file
python3 build_mininet.py ${FILENAME} 
