#
# A few operations on the BST
#

# Select here which implementation you want to use:
# Old one:
#import bst
# New one
import nrbst as bst

d = bst.dict()

d[7] = "CS206"
d[3] = "CS109"

print("d = %s" % d)
print("d[3] = %s" % d[3])
print("d[7] = %s" % d[7])

d[7] = "CS206A"

print("d = %s" % d)
print("d[3] = %s" % d[3])
print("d[7] = %s" % d[7])

d[13] = "CS300"
d[29] = "CS500"

print("d = %s" % d)

del d[13]

print("d = %s" % d)

d[5] = "CS101"
d[19] = "CS492"
d[17] = "CS408"
d[11] = "CS220"

print("d = %s" % d)

del d[17]

print("d = %s" % d)

print("First key is %s" % d.firstkey())
print("Last key is %s" % d.lastkey())

print("Now testing an unbalanced insertion order:")
e = bst.dict()
n = 1010
for i in range(1, n):
  e[i] = str(i)

print("First key is %s" % e.firstkey())
print("Last key is %s" % e.lastkey())

del e[n//2]

