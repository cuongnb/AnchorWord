from pyhull import convex_hull
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



size = 200
x_axis = np.random.rand(size)
y_axis = np.random.rand(size)
z_axis = np.random.rand(size)
data = []
for i in range(0, size):
    data.append([int(x_axis[i] * 1000), int(y_axis[i] * 1000), int(z_axis[i] * 1000)])

print data
convex_hull = convex_hull.ConvexHull(data)
print "Convex hull"

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for item in data:
    ax.plot([item[0]], [item[1]], [item[2]], color='r', marker='o')

# List of anchor point
anchor = []
for c in convex_hull.simplices:
    item = c.coords
    print item
    if [item[0][0], item[0][1], item[0][2]] not in anchor:
        anchor.append([item[0][0], item[0][1], item[0][2]])
    if [item[1][0], item[1][1], item[1][2]] not in anchor:
        anchor.append([item[1][0], item[1][1], item[1][2]])
    if [item[2][0], item[2][1], item[2][2]] not in anchor:
        anchor.append([item[2][0], item[2][1], item[2][2]])
    ax.plot([item[0][0], item[1][0]], [item[0][1], item[1][1]], [item[0][2], item[1][2]], color='b')
    ax.plot([item[1][0], item[2][0]], [item[1][1], item[2][1]], [item[1][2], item[2][2]], color='b')
    ax.plot([item[2][0], item[0][0]], [item[2][1], item[0][1]], [item[2][2], item[0][2]], color='b')
plt.show()

print len(anchor)
print anchor