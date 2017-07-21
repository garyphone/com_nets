# The OpenStack onlytread the HEAT-template file with YAML-format.
# This Python prgram is used to build a YAML-format structure and
# export it in a local folder.

# Import the specific file format.
import yaml

# The following array data are examples to combine as a YAML-file.
Nodes = ['Node0', 'Node1', 'Node2']
Nes = ['Ne0', 'Ne1', 'Ne2']
names = ['BERLIN', 'FRANKFURT', 'MUNICH']

internal_routers = ['ir0', 'ir1', 'ir2']
internal_rinterfaceAs = ['iriA0', 'iriA1', 'iriA2']
internal_rinterfaceBs = ['iriB0', 'iriB1', 'iriB2']
instancers_port0 = ['0port0', '1port0', '2port0']
instancers_port1 = ['0port1', '1port1', '2port1']
sources = ['Node0', 'Node0', 'Node1']
targets = ['Node1', 'Node2', 'Node2']

data = {'heat_template_version' : '2015-04-30',

        'description' : '3 nodes network',

        'resources' : {

            Nodes[0] : {

                'type' : 'OS::Neutron::Net',

                'properties' : {

                    'name' : names[0]
                }
            },

            Nes[0] : {

                'type' : 'OS::Neutron::Subnet',

                'properties' : {

                    'name' : names[0],

                    'cidr' : '10.20.0.0/24',

                    # Good to know is here, how can we build the key-value pair.
                    'network_id' : {'get_resource' : Nodes[0]},

                    # For the many destinations situation, how can we build the
                    # key-value pairs.
                    'host_routes' : [
                    {'destination' : '10.40.0.0/24', 'nexthop' : '10.20.0.10'},
                    {'destination' : '10.60.0.0/24', 'nexthop' : '10.20.0.40'}
                    ]
                }
            },

            Nodes[1] : {

                'type' : 'OS::Neutron::Net',

                'properties' : {

                    'name' : names[1]
                }
            },

            Nes[1] : {

                'type' : 'OS::Neutron::Subnet',

                'properties' : {

                    'name' : names[1],

                    'cidr' : '10.40.0.0/24',

                    'network_id' : {'get_resource' : Nodes[1]},

                    'host_routes' : [
                    {'destination' : '10.20.0.0/24', 'nexthop' : '10.40.0.40'},
                    {'destination' : '10.60.0.0/24', 'nexthop' : '10.40.0.10'}
                    ]
                }
            },

            Nodes[2] : {

                'type' : 'OS::Neutron::Net',

                'properties' : {

                    'name' : names[2]
                }
            },

            Nes[2]: {

                'type' : 'OS::Neutron::Subnet',

                'properties' : {

                    'name' : names[2],

                    'cidr' : '10.60.0.0/24',

                    'network_id' : {'get_resource' : Nodes[2]},

                    'host_routes' : [
                    {'destination' : '10.20.0.0/24', 'nexthop' : '10.60.0.10'},
                    {'destination' : '10.40.0.0/24', 'nexthop' : '10.60.0.40'}
                    ]
                }
            },

            internal_routers[0] : {

                'type' : 'OS::Neutron::Router',

                'properties' : {

                    'name' : internal_routers[0]

                }
            },

            internal_rinterfaceAs[0] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[0]},

                    'port' : {'get_resource' : instancers_port0[0]}
                }
            },

            internal_rinterfaceBs[0] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[0]},

                    'port' : {'get_resource' : instancers_port1[0]}
                }
            },

            instancers_port0[0] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : sources[0]},

                    'fixed_ips' : [
                    {'ip_address' : '10.20.0.10'}
                    ]
                }
            },

            instancers_port1[0] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : targets[0]},

                    'fixed_ips' : [
                    {'ip_address' : '10.40.0.40'}
                    ]
                }
            },

	    internal_routers[1] : {

                'type' : 'OS::Neutron::Router',

                'properties' : {

                    'name' : internal_routers[1]

                }
            },

            internal_rinterfaceAs[1] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[1]},

                    'port' : {'get_resource' : instancers_port0[1]}
                }
            },

            internal_rinterfaceBs[1] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[1]},

                    'port' : {'get_resource' : instancers_port1[1]}
                }
            },

            instancers_port0[1] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : sources[1]},

                    'fixed_ips' : [
                    {'ip_address' : '10.20.0.40'}
                    ]
                }
            },

            instancers_port1[1] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : targets[1]},

                    'fixed_ips' : [
                    {'ip_address' : '10.60.0.10'}
                    ]
                }
            },

	    internal_routers[2] : {

                'type' : 'OS::Neutron::Router',

                'properties' : {

                    'name' : internal_routers[2]

                }
            },

            internal_rinterfaceAs[2] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[2]},

                    'port' : {'get_resource' : instancers_port0[2]}
                }
            },

            internal_rinterfaceBs[2] : {

                'type' : 'OS::Neutron::RouterInterface',

                'properties' : {

                    'router_id' : {'get_resource' : internal_routers[2]},

                    'port' : {'get_resource' : instancers_port1[2]}
                }
            },

            instancers_port0[2] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : sources[2]},

                    'fixed_ips' : [
                    {'ip_address' : '10.40.0.10'}
                    ]
                }
            },

            instancers_port1[2] : {

                'type' : 'OS::Neutron::Port',

                'properties' : {

                    'network' : {'get_resource' : targets[2]},

                    'fixed_ips' : [
                    {'ip_address' : '10.60.0.40'}
                    ]
                }
            },
        }
        }

# Export the expected YAML-file to the local folder.
with open('data.yaml', 'w') as outfile:
    yaml.dump(data, outfile)
