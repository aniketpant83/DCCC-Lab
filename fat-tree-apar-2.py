from mininet.topo import Topo
from mininet.link import TCLink

class FatTree(Topo):
    def __init__(self, n=4):
        super().__init__()
        
        # Add hosts
        for i in range(1, (n // 2) + 1):
            for j in range(1, (n // 2) + 1):
                host = self.addHost('h%d%d' % (i, j))
                edge_switch = self.addSwitch('es%d%d' % (i, j))
                self.addLink(host, edge_switch, link=TCLink(bw=10))

        # Add edge switches
        for i in range(1, (n // 2) + 1):
            edge_switch = self.addSwitch('es%d' % i)
            for j in range(1, (n // 2) + 1):
                self.addLink(edge_switch, self.get('h%d%d' % (i, j)), link=TCLink(bw=10))

        # Add aggregation switches
        agg_switches = []
        for i in range(1, (n // 2) + 1):
            agg_switch = self.addSwitch('as%d' % i)
            agg_switches.append(agg_switch)
            for j in range(1, (n // 2) + 1):
                edge_switch = self.get('es%d%d' % (j, i))
                self.addLink(agg_switch, edge_switch, link=TCLink(bw=10))

        # Add core switches
        core_switches = []
        for i in range(1, (n // 2) + 1):
            core_switch = self.addSwitch('cs%d' % i)
            core_switches.append(core_switch)
            for j in range(1, (n // 2) + 1):
                agg_switch = agg_switches[j - 1]
                self.addLink(core_switch, agg_switch, link=TCLink(bw=20))

topos = {'fattree': FatTree}
