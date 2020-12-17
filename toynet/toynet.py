from toynet.toytopo import ToyTopo
import toynet.xmlParser as parser
from toynet.xmlParser import ToyTopoConfig

from mininet.net import Mininet
from mininet.cli import CLI

class ToyNet():
    def __init__(self, filename:str):
        self.config:ToyTopoConfig = parser.parseXML(filename)

    def interact(self):
        print('__INFO___ Generating Interactive Mininet Instance')
        topology=ToyTopo(self.config) # ToyNet( topo=TreeTopo( depth=2, fanout=6 ) )
        self.mininet = Mininet(topo=topology)

        self.mininet.start()
        CLI( self.mininet )
        self.mininet.stop()
