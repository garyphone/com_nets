# Network Topology

This folder is described to build network topology in the OpenStack by using HEAT template.

* "import.py" is used to import the XML-file in order to read the information about the 
  geographical nodes and edges.

* "export.py" is used to export the YAML-file, which it will be launched by Stacks in the 
  OpenStack.

* "dict.py" is used to test and verify the real situation in building YAML-file with variables.

* "xml2yaml.py" is a converter, which I can transfer the XML-file to the YAML-file directly in a 
  Python program.

* examples folder is shown that some examples have been transfered by "xml2yaml.py" automatically.
