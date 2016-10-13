# How to work with openstack
#
#It needs multiple options as: 
# nova: to create instance
# glance: to provide an OS for the vm
# cinder: to provide a storage to the vm
# keystone: to check the user credentials
# neutron: to establish a network

# all is needed is only a url, data, headers
# with that generate a response by requesting a post with the url, data and headers
# with that response generate a adminToken by response.json()

# Procedure to create a user vm
# First need to check with the credentials:

# Create a network to which the vm to be connected

# Assign an IP stream to the created network

# Create a volume, size of the volumes is indicated by the numerals; for ex: 1-tiny, 2-small, 3-large etc

# Create a instance and assign it a volume, connect to a network, assign an IP, provide an OS.
