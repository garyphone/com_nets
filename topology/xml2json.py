from xml.dom import minidom

#filename = raw_input('please print the filename you want to launch: ')

filename = 'haec-box--4x4.xml'

xmldoc = minidom.parse(filename)

graph = xmldoc.getElementsByTagName("graph")[0]

nodes = graph.getElementsByTagName("node")

Names = []
Sources = []
Targets = []
Latitudes = []
Longitudes = []
sources = []
targets = []
latitudes = []
longitudes = []

for node in nodes:

    names = node.getElementsByTagName("data")[5].firstChild.data
    Names.append(str(names))
    latitudes = node.getElementsByTagName("data")[1].firstChild.data
    Latitudes.append(str(latitudes))
    longitudes = node.getElementsByTagName("data")[4].firstChild.data
    Longitudes.append(str(longitudes))

edges = graph.getElementsByTagName("edge")

for edge in edges:
    lst = edge.attributes['source'].value
    for node in nodes:
        check = node.getElementsByTagName("data")[3].firstChild.data
        if check == lst:
            names = node.getElementsByTagName("data")[5].firstChild.data
            sources.append(str(names))

Sources.append(sources)
Sources = Sources[0]

for edge in edges:

    lst = edge.attributes['target'].value
    for node in nodes:
        check = node.getElementsByTagName("data")[3].firstChild.data
        if check == lst:
            names = node.getElementsByTagName("data")[5].firstChild.data
            targets.append(str(names))

Targets.append(targets)
Targets = Targets[0]

########################################################################
########################################################################

import json
import os

places = {}
k = len(Names)
l = len(Sources)
routes = {}
Routes = []
save_path = '/opt/stack/horizon/openstack_dashboard/dashboards/project/visualization/templates/visualization'

for i in range(k):
    places[Names[i]] = [float(Longitudes[i]), float(Latitudes[i])]

with open(os.path.join(save_path, 'places.json'), 'w') as outfile:
    json.dump(places, outfile)

for i in range(l):
    routes = {"source": Sources[i], "target": Targets[i]}
    Routes.append(routes)

with open(os.path.join(save_path, 'routes.json'), 'w') as outfile:
    json.dump(Routes, outfile)

########################################################################
########################################################################
