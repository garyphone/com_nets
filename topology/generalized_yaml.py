# This Python program is combined with export.py and import.py.
# Finally, I use this program to build network topology in OpenStack.
# Maybe there are some ip-address conflicts in part of building host_routes.
# These errors will be fixed in the part of Visualization.

from xml.dom import minidom

#filename = input('please print the filename you want to convert:) ')

filename = 'haec-box--cube-surface.xml'

xmldoc = minidom.parse(filename)

graph = xmldoc.getElementsByTagName("graph")[0]

nodes = graph.getElementsByTagName("node")

Names = []
Sources = []
Targets = []
sources = []
targets = []

for node in nodes:

    names = node.getElementsByTagName("data")[5].firstChild.data
    Names.append(str(names))

edges = graph.getElementsByTagName("edge")

for edge in edges:

    lst = edge.attributes['source'].value
    # with str() is used to remove 'u' in dictory.
    Sources.append('Node' + str(lst))
    sources.append(str(lst))

edges = graph.getElementsByTagName("edge")

for edge in edges:

    lst = edge.attributes['target'].value
    Targets.append('Node' + str(lst))
    targets.append(str(lst))

########################################################################
########################################################################

import yaml

index1 = len(Names) #=> 4
index2 = len(Sources)
Nodes = [] #=> []
Nes = []
internal_routers = []
internal_rinterfaceAs = []
internal_rinterfaceBs = []
instancers_port0 = []
instancers_port1 = []

def generateNodes():

    i = 0
    for i in range(index1):

        Nodes.append('Node' + str(i))

def generateNes():

    i = 0
    for i in range(index1):

        Nes.append('Ne' + str(i))

generateNodes()
generateNes()

def generateRoutes():

    i = 0
    for i in range(index2):

        internal_routers.append('ir' + str(i))

def generateInterfaces():

    i = 0
    for i in range(index2):

        internal_rinterfaceAs.append('iriA' + str(i))
        internal_rinterfaceBs.append('iriB' + str(i))

def generatePorts():

    i = 0
    for i in range(index2):

        instancers_port0.append(str(i) + 'port0')
        instancers_port1.append(str(i) + 'port1')

generateRoutes()
generateInterfaces()
generatePorts()

# with the conflict in arrays, the first element plays no role, so I remove it
# to build a suitable arrays in each router and port.
internal_routers.append('0')
internal_rinterfaceAs.append('0')
internal_rinterfaceBs.append('0')
instancers_port0.append('0')
instancers_port1.append('0')

routes = {}
files = {}
data = {}
k = len(Nes)

for i in range(len(Nodes)):
    data[Nodes[i]] = {'type' : 'OS::Neutron::Net'}
    data[Nodes[i]]['properties'] = {'name' : Names[i]}

def setHostRoutes(value):
    def all_indices(key, qlist):
      indices = []
      idx = -1
      while True:
        try:
            idx = qlist.index(key, idx+1)
            indices.append(idx)
        except ValueError:
            break
      return indices

    alpha = all_indices(str(value), sources)
    belta = all_indices(str(value), targets)

    ipAs = []
    ipBs = []
    
    for i in range(len(alpha)):
       ipA = ('10.' + str(int(targets[alpha[i]]) + 1) + '.0.0/24')
       ipB = ('10.' + str(int(value) + 1) + '.0.' + str(int(targets[alpha[i]]) + 3))
       routes = {'destination' : ipA, 'nexthop' : ipB}
       ipAs.append(routes) 

    for i in range(len(belta)):
       ipA = ('10.' + str(int(sources[belta[i]]) + 1) + '.0.0/24')
       ipB = ('10.' + str(int(value) + 1) + '.0.' + str(int(sources[belta[i]]) + 3))
       routes = {'destination' : ipA, 'nexthop' : ipB}
       ipBs.append(routes) 
    return ipAs + ipBs

for i in range(len(Nes)):
    #ips = []
    #def setHostRoutes(value):
      #ips = (x for x in sources if (str(value) in source))
      

        #for j in range(k): #this loop should be corrected.
	#  if str(value) in sources:
        #    ipA = ('10.' + str(int(targets[value]) + 1) + '.0.0/24')
        #    ipB = ('10.' + str(value + 1) + '.0.' + str(int(targets[value]) + 3))
        #    routes = {'destination' : ipA, 'nexthop' : ipB}
        #    ips.append(routes)
        #return ips

    data[Nes[i]] = {'type' : 'OS::Neutron::Subnet'}
    data[Nes[i]]['properties'] = {'network_id' : {'get_resource' : Nodes[i]},
                                'name' : Names[i],
                                'cidr' : '10.' + str(i + 1) + '.0.0/24',
                                'host_routes' : setHostRoutes(i)
                                }
    ###########################################################


for i in range(len(internal_routers)-1):
    data[internal_routers[i]] = {'type' : 'OS::Neutron::Router'}
    data[internal_routers[i]]['properties'] = {'name' : internal_routers[i]}

for i in range(len(internal_rinterfaceAs)-1):
    data[internal_rinterfaceAs[i]] = {'type' : 'OS::Neutron::RouterInterface'}
    data[internal_rinterfaceAs[i]]['properties'] = {'router_id' : {'get_resource' : internal_routers[i]},
                                                    'port' : {'get_resource' : instancers_port0[i]}}

for i in range(len(internal_rinterfaceBs)-1):
    data[internal_rinterfaceBs[i]] = {'type' : 'OS::Neutron::RouterInterface'}
    data[internal_rinterfaceBs[i]]['properties'] = {'router_id' : {'get_resource' : internal_routers[i]},
                                                    'port' : {'get_resource' : instancers_port1[i]}}

for i in range(len(instancers_port0)-1):
    data[instancers_port0[i]] = {'type' : 'OS::Neutron::Port'}
    data[instancers_port0[i]]['properties'] = {'network' : {'get_resource' : Sources[i]},
                                            'fixed_ips': [{'ip_address' : '10.' + str(int(sources[i]) + 1) + '.0.' + str(int(targets[i]) + 3)}]}

for i in range(len(instancers_port1)-1):
    data[instancers_port1[i]] = {'type' : 'OS::Neutron::Port'}
    data[instancers_port1[i]]['properties'] = {'network' : {'get_resource' : Targets[i]},
                                            'fixed_ips': [{'ip_address' : '10.' + str(int(targets[i]) + 1) + '.0.' + str(int(sources[i]) + 3)}]}

files = {'heat_template_version' : '2015-04-30',
        'description' : filename,
        'resources' : data}

with open('launch.yaml', 'w') as outfile:
    yaml.dump(files, outfile)
