"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        n = 4

        h = n // 2

        # Create core switches
        coreSwitches = []
        for i in range(n // 2):
            coreSwitches.append(self.addSwitch('c{}'.format(i+1)))

        # Create aggregation switches
        aggSwitches = []
        for i in range(n):
            aggSwitches.append(self.addSwitch('a{}'.format(i+1)))

        # Create edge switches and hosts
        for i in range(n):
            edgeSwitch = self.addSwitch('e{}'.format(i+1))
            for j in range(h):
                host = self.addHost('h{}{}'.format(i+1, j+1))
                self.addLink(host, edgeSwitch, bw=10)
            self.addLink(edgeSwitch, aggSwitches[i // 2], bw=10)

        # Connect aggregation switches to core switches
        for i in range(n):
            self.addLink(aggSwitches[i], coreSwitches[i // (n // 2)], bw=20)



topos = { 'mytopo': ( lambda: MyTopo() ) }