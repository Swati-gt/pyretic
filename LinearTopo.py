#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
import sys
class LinearTopo(Topo):
    "Linear topology of 2 switches, with one switch has two hosts and other has one."

    def __init__(self, k=2, **opts):
        """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

        super(LinearTopo, self).__init__(**opts)

        self.k = k

        lastSwitch = None
	#print "sys argument",sys.argv[2]
	host_counter = int(sys.argv[2])
        for i in irange(1, k):
            #host = self.addHost('h%s' % i)
            #self.addLink( host, switch)
            if not lastSwitch:
		    for h in range(host_counter):
			host = self.addHost('h%s' %(h+1))
            	        switch = self.addSwitch('s%s' % i)
            	        self.addLink( host, switch)
 
		    '''host1 = self.addHost('h%s' % i)
        	    host2 = self.addHost('h%s' % (i+1))
            	    switch = self.addSwitch('s%s' % i)
            	    self.addLink( host1, switch)
                    self.addLink( host2, switch)'''
	    else:
		    host3 = self.addHost('h%s' % (host_counter+1))		
            	    switch = self.addSwitch('s%s' % i)
            	    self.addLink( host3, switch)

            if lastSwitch:
                self.addLink( switch, lastSwitch)
            lastSwitch = switch
	
    #print self.hosts[0].cmd('ping -c1 %s' %self.hosts[3].IP())

def simpleTest():
    "Create and test a simple network"
    topo = LinearTopo(k=2)
    net = Mininet(topo)
    net.start()
    h1,h3 = net.hosts[0],net.hosts[2]
    net.pingAll()
    print h1.cmd('ping -c1 %s' %h3.IP())
    #print cmd('link %s %s' %h1.IP() %h3.IP())
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"

    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
