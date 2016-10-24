from pyhull import convex_hull
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import numpy as np
from sklearn import decomposition

# data = [[-0.5, -0.5], [-0.5, 0.5], [0.5, -0.5], [0, 0], [0.3, 0.25]]
# tnse = TSNE(n_components=2)
# a1 = tnse.fit_transform(a)
# print "TNSE"
# print a1
# print '\n'
#
# pca = decomposition.PCA(n_components=2)
# a2 = pca.fit_transform(a)
# print "PCA"
# print a2
size = 20
x_axis = np.random.rand(size)
y_axis = np.random.rand(size)
data = []
for i in range(0, size):
    data.append([x_axis[i], y_axis[i]])

convex_hull = convex_hull.ConvexHull(data)
print "Convex hull"
print convex_hull.dim
for item in convex_hull.simplices:
    c = item.coords
    plt.plot([c[0][0], c[1][0]], [c[0][1], c[1][1]], color='r')


plt.scatter(x_axis, y_axis)
plt.show()