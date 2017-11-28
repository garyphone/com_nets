#!/usr/bin/python

## Adapted from: https://raw.githubusercontent.com/Lab41/graph-generators/master/create_graph.py

import math, sys, time, uuid
from random import randint, sample

def output_file(file):
    fo = open(file, 'w')
    return fo


def print_keys(fo):
    # write headers
    #
    node_str = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
    node_str += "<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">\n"

    # keys for a node 
    #
    node_str += "<key attr.name=\"id\" attr.type=\"int\" for=\"node\" id=\"d30\" />\n"
    node_str += "<key attr.name=\"Longitude\" attr.type=\"double\" for=\"node\" id=\"d31\" />\n"
    node_str += "<key attr.name=\"Latitude\" attr.type=\"double\" for=\"node\" id=\"d32\" />\n"
    node_str += "<key attr.name=\"label\" attr.type=\"string\" for=\"node\" id=\"d33\" />\n"
    node_str += "<key attr.name=\"Country\" attr.type=\"string\" for=\"node\" id=\"d34\" />\n"
    node_str += "<key attr.name=\"Internal\" attr.type=\"int\" for=\"node\" id=\"d35\" />\n"

    # keys for an edge
    #
    node_str += "<key attr.name=\"id\" attr.type=\"string\" for=\"edge\" id=\"d40\" />\n"
    node_str += "<key attr.name=\"key\" attr.type=\"int\" for=\"edge\" id=\"d41\" />\n"

    # other keys
    #
    node_str += "<key attr.name=\"Testbed\" attr.type=\"int\" for=\"graph\" id=\"d27\" />\n"
    node_str += "<key attr.name=\"LastProcessed\" attr.type=\"string\" for=\"graph\" id=\"d26\" />\n"
    node_str += "<key attr.name=\"DateYear\" attr.type=\"string\" for=\"graph\" id=\"d25\" />\n"
    node_str += "<key attr.name=\"NetworkDate\" attr.type=\"string\" for=\"graph\" id=\"d24\" />\n"
    node_str += "<key attr.name=\"Transit\" attr.type=\"int\" for=\"graph\" id=\"d23\" />\n"
    node_str += "<key attr.name=\"Developed\" attr.type=\"int\" for=\"graph\" id=\"d22\" />\n"
    node_str += "<key attr.name=\"Creator\" attr.type=\"string\" for=\"graph\" id=\"d21\" />\n"
    node_str += "<key attr.name=\"Layer\" attr.type=\"string\" for=\"graph\" id=\"d20\" />\n"
    node_str += "<key attr.name=\"LastAccess\" attr.type=\"string\" for=\"graph\" id=\"d19\" />\n"
    node_str += "<key attr.name=\"DateMonth\" attr.type=\"string\" for=\"graph\" id=\"d18\" />\n"
    node_str += "<key attr.name=\"DateModifier\" attr.type=\"string\" for=\"graph\" id=\"d17\" />\n"
    node_str += "<key attr.name=\"SourceGitVersion\" attr.type=\"string\" for=\"graph\" id=\"d16\" />\n"
    node_str += "<key attr.name=\"IX\" attr.type=\"int\" for=\"graph\" id=\"d15\" />\n"
    node_str += "<key attr.name=\"Customer\" attr.type=\"int\" for=\"graph\" id=\"d14\" />\n"
    node_str += "<key attr.name=\"ToolsetVersion\" attr.type=\"string\" for=\"graph\" id=\"d13\" />\n"
    node_str += "<key attr.name=\"label\" attr.type=\"string\" for=\"graph\" id=\"d12\" />\n"
    node_str += "<key attr.name=\"Commercial\" attr.type=\"int\" for=\"graph\" id=\"d11\" />\n"
    node_str += "<key attr.name=\"Backbone\" attr.type=\"int\" for=\"graph\" id=\"d10\" />\n"
    node_str += "<key attr.name=\"DateType\" attr.type=\"string\" for=\"graph\" id=\"d9\" />\n"
    node_str += "<key attr.name=\"Type\" attr.type=\"string\" for=\"graph\" id=\"d8\" />\n"
    node_str += "<key attr.name=\"Version\" attr.type=\"string\" for=\"graph\" id=\"d7\" />\n"
    node_str += "<key attr.name=\"Source\" attr.type=\"string\" for=\"graph\" id=\"d6\" />\n"
    node_str += "<key attr.name=\"Access\" attr.type=\"int\" for=\"graph\" id=\"d5\" />\n"
    node_str += "<key attr.name=\"Provenance\" attr.type=\"string\" for=\"graph\" id=\"d4\" />\n"
    node_str += "<key attr.name=\"Network\" attr.type=\"string\" for=\"graph\" id=\"d3\" />\n"
    node_str += "<key attr.name=\"GeoExtent\" attr.type=\"string\" for=\"graph\" id=\"d2\" />\n"
    node_str += "<key attr.name=\"GeoLocation\" attr.type=\"string\" for=\"graph\" id=\"d1\" />\n"
    node_str += "<key attr.name=\"DateObtained\" attr.type=\"string\" for=\"graph\" id=\"d0\" /> \n"   

    # other headers
    #
    node_str += "    <graph edgedefault=\"undirected\">\n"
    node_str += "        <data key=\"d0\">19/09/17</data>\n"
    node_str += "        <data key=\"d1\">Germany</data>\n"
    node_str += "        <data key=\"d2\">Country</data>\n"
    node_str += "        <data key=\"d3\">HAEC</data>\n"
    node_str += "        <data key=\"d4\">Secondary</data>\n"
    node_str += "        <data key=\"d5\">0</data>\n"
    node_str += "        <data key=\"d6\">https://cn.ifn.et.tu-dresden.de/</data>\n"
    node_str += "        <data key=\"d7\">1.0</data>\n"
    node_str += "        <data key=\"d8\">grid</data>\n"
    node_str += "        <data key=\"d9\">Historic</data>\n"
    node_str += "        <data key=\"d10\">1</data>\n"
    node_str += "        <data key=\"d11\">0</data>\n"
    node_str += "        <data key=\"d12\">HAEC-box</data>\n"
    node_str += "        <data key=\"d13\">0.1</data>\n"
    node_str += "        <data key=\"d14\">0</data>\n"
    node_str += "        <data key=\"d15\">0</data>\n"
    node_str += "        <data key=\"d16\">0</data>\n"
    node_str += "        <data key=\"d17\">=</data>\n"
    node_str += "        <data key=\"d18\">12</data>\n"
    node_str += "        <data key=\"d19\">19/09/17</data>\n"
    node_str += "        <data key=\"d20\">HAEC</data>\n"
    node_str += "        <data key=\"d21\">Modified from Topology Zoo Toolset</data>\n"
    node_str += "        <data key=\"d22\">1</data>\n"
    node_str += "        <data key=\"d23\">0</data>\n"
    node_str += "        <data key=\"d24\">=</data>\n"
    node_str += "        <data key=\"d25\">=</data>\n"
    node_str += "        <data key=\"d26\">2017_09_19</data>\n"
    node_str += "        <data key=\"d27\">0</data>\n"
    #
    fo.write(node_str)

    
def print_closing_tags(fo):
    str_tag = "    </graph>\n"
    str_tag += "</graphml>\n"
    #
    fo.write(str_tag)
        
    
def print_one_node(fo, id, longitude, lattitude):
    
    str_temp = "    <node id=\"" + str(id) + "\">\n"
    str_temp += "        <data key=\"d35\">1</data>\n"
    str_temp += "        <data key=\"d31\">" + str(longitude) + "</data>\n"
    str_temp += "        <data key=\"d34\">Germany</data>\n"
    str_temp += "        <data key=\"d30\">" + str(id) + "</data>\n"
    str_temp += "        <data key=\"d32\">" + str(lattitude) + "</data>\n"
    str_temp += "        <data key=\"d33\">PCB-" + str(id) + "</data>\n"
        
    str_temp += "    </node>\n"
    #    
    fo.write(str_temp)


def print_one_edge(fo, id, source_node, dest_node):

    str_temp = "    <edge source=\"" + str(source_node) + "\" target=\"" + str(dest_node) + "\">\n"
    str_temp += "        <data key=\"d40\">e" + str(id) + "\"</data>\n"
    str_temp += "        <data key=\"d41\">0</data>\n"
    str_temp += "    </edge>\n"
    #    
    fo.write(str_temp)



def print_help():
    print "\n-n \t<number of nodes per dimension> (default is 4, must be greater than 0)\n"
    print "-o \t<path to output file> (default is 'haec-box--4x4.xml')\n"
    print "* only graphml has been implemented so far\n"
    sys.exit(0)
    
def process_args(args):
    # default initialization
    #
    num_nodes = 5
    output = "haec-box--5x5.xml"
    
    # process rest of the args
    i = 0
    while i < len(args): 
        if args[i] == "-n":
            try:
                num_nodes = int(args[i+1])
                if num_nodes < 1:
                    print "number of nodes per dimenstion has to be at least one \n"
            except:
                print "Unable to read number of nodes"
        elif args[i] == "-o":
            try:
                output = args[i+1]
                f = open(output, 'w')
                f.close()
            except:
                print "unable to open file"+output
        else:
            print_help()
        i += 2
    return output, num_nodes
    
        
def get_args():
    args = []
    for arg in sys.argv:
        args.append(arg)
    return args[1:]

            
if __name__ == "__main__":
    start_time = time.time()
    # Parameters
    #
    args = get_args()
    output, num_nodes = process_args(args)

    fo = output_file(output)
    print_keys(fo)
        
    delta_long = 5.0
    delta_latt = 5.0
    ori_long = 0.0
    ori_latt = 0.0
    x = y = num_nodes
    
    # Nodes
    #
    id = 0
    for i in range (0, x):
        for j in range (0, y):
            longitude = ori_long + i * delta_long
            lattitude = ori_latt + j * delta_latt
            print_one_node(fo, id, longitude, lattitude)
            id += 1
    
    # Edges
    #
    id = 0
    for i in range (0, x):
        for j in range (0, y-1):
            cur_id = i * x + j
            next_id = cur_id + 1
            print_one_edge(fo, id, cur_id, next_id)
            id += 1
    
    for i in range (0, x - 1):
        for j in range (0, y):
            cur_id = i * x + j
            next_id = (i + 1) * x + j
            print_one_edge(fo, id, cur_id, next_id)            
            id += 1
            
    print_closing_tags(fo)    
    fo.close()

