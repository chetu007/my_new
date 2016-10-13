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
