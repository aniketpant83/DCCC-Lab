"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class FatTree(Topo):
    def __init__(self, n):
        Topo.__init__(self)

        # Your code here
        h = n // 2

        # Create core switches
        core_switches = []
        for i in range(n // 2):
            core_switches.append(self.addSwitch('c{}'.format(i+1)))

        # Create aggregation switches
        agg_switches = []
        for i in range(n):
            agg_switches.append(self.addSwitch('a{}'.format(i+1)))

        # Create edge switches and hosts
        for i in range(n):
            edge_switch = self.addSwitch('e{}'.format(i+1))
            for j in range(h):
                host = self.addHost('h{}{}'.format(i+1, j+1))
                self.addLink(host, edge_switch, bw=10)
            self.addLink(edge_switch, agg_switches[i // 2], bw=10)

        # Connect aggregation switches to core switches
        for i in range(n):
            self.addLink(agg_switches[i], core_switches[i // (n // 2)], bw=20)
