from collections import namedtuple

Point =namedtuple('Point',['x','y'])

p=Point(10,20)

print(p[0],p[1])