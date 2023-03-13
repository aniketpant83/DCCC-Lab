from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class FatTree(Topo):
    def __init__(self, n):
        Topo.__init__(self)

        # Number of hosts per edge switch
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

if __name__ == '__main__':
    n = 4  # Change this to the desired value of n
    topo = FatTree(n)
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.pingAll()
    net.stop()
