from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class FatTree(Topo):
    def __init__(self, n):
        Topo.__init__(self)

        # Number of hosts per edge switch
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

if __name__ == '__main__':
    n = 4  # Change as desired
    topo = FatTree(n)
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.pingAll()
    net.stop()
