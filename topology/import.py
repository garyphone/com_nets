# This Python program is used for get information from a XML-file.
# The definitions of geographic XML-file is shown in *example*-folder.

# Use minidom to cut the node information in XML-file, it can be also
# achieved by using tree.
from xml.dom import minidom

xmldoc = minidom.parse("arpanet1969.xml")

graph = xmldoc.getElementsByTagName("graph")[0]

nodes = graph.getElementsByTagName("node")

for node in nodes:

    # The array element should be defined with a specific number to locate it.
    des = node.getElementsByTagName("data")[5].firstChild.data

    print des

print "#############################"

edges = graph.getElementsByTagName("edge")

for edge in edges:

    # Use the key value pair to trace the information.
    print(edge.attributes['source'].value)

print "#############################"

edges = graph.getElementsByTagName("edge")

for edge in edges:

    print(edge.attributes['target'].value)
