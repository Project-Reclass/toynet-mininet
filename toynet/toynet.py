from toynet.toytopo import ToyTopo
import toynet.xmlParser as parser
from toynet.xmlParser import ToyTopoConfig

from mininet.net import Mininet
from mininet.cli import CLI

class ToyNet():
    def __init__(self, filename:str=None):
        #can throw: XMLParseError, TypeCheckError
        self.config:ToyTopoConfig = parser.parseXMLFilename(filename)
        self.topology = ToyTopo(self.config)
        self.mininet = Mininet(topo=self.topology)

    def __init__(self, filecontent:str=None):
        #can throw: XMLParseError, TypeCheckError
        self.config:ToyTopoConfig = parser.parseXMLContent(filecontent)
        self.topology = ToyTopo(self.config)
        self.mininet = Mininet(topo=self.topology)

    def interact(self):
        print('__INFO___ Generating Interactive Mininet Instance')
        self.topology=ToyTopo(self.config) # ToyNet( topo=TreeTopo( depth=2, fanout=6 ) )
        self.mininet = Mininet(topo=self.topology)

        self.mininet.start()
        CLI( self.mininet )
        self.mininet.stop()

    def start(self):
        if self.mininet is not None:
            self.mininet.start()

    def cmd(self, command:str):
        #send command to mininet
        pass

    def stop(self):
        if self.mininet is not None:
            self.mininet.stop()

    def restart(self, new_topology=None):
        print(new_topology)
        self.stop()
        if new_topology is not None:
            #can throw: XMLParseError, TypeCheckError
            self.config:ToyTopoConfig = parser.parseXMLContent(new_topology)
            self.topology = ToyTopo(self.config)
            self.mininet = Mininet(topo=self.topology)
        self.start()

