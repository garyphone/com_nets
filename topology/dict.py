# This Python program is used to test and verify the real situation in building
# YAML-file with variables.

import yaml

# Static lists for purpose of illustration
names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]
data ={}
filename = 'arpanet1969'
Nodes = ['Node0', 'Node1', 'Node2']
Nes = ['Ne0', 'Ne1', 'Ne2']
k = len(Nes)
routes = {}
files = {}

# Here to create nodes
for i in range(len(Nodes)):
    data[Nodes[i]] = {'type' : 'OS::Neutron::Net'}
    data[Nodes[i]]['properties'] = {'name' : names[i]}

for i in range(len(Nes)):
    ips = []
    def setHostRoutes(value):
        for j in range(k):
            ipA = ('10.' + str(j) + '.0.0/24')
            ipB = ('10.' + str(value) + '.0.' + str(j))
            routes = {'destination' : ipA, 'nexthop' : ipB}
            ips.append(routes)
        return ips

    data[Nes[i]] = {'type' : 'OS::Neutron::Net'}
    data[Nes[i]]['properties'] = {'network_id' : {'get_resource' : Nodes[i]},
                                'name' : names[i],
                                'cidr' : '10.' + str(i) + '.0.0/24',
                                'host_routes' : setHostRoutes(i)
                                }

files = {'heat_template_version' : '2015-04-30',
        'description' : filename,
        'resources' : data}

with open('dict.yaml', 'w') as outfile:
    yaml.dump(files, outfile)
