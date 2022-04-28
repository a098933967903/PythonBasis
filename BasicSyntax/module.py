'''
import sys as system # as -> rename

print(system.platform)
print(system.maxsize)
'''



#Customize import
'''
import modules.geometry as geomtry

print(geomtry.distance(0,0,3,4))
'''

'''
import sys as system

print(system.path)

system.path.append("modules")
# -> We could find the path to show in lists of system.path 

print(system.path)

import geometry

print(geometry.distance(0,0,3,4))
'''


