from sklearn import decomposition
from sklearn.manifold import TSNE

data = [[-0.5, -0.5], [-0.5, 0.5], [0.5, -0.5], [0, 0], [0.3, 0.25]]
tnse = TSNE(n_components=2)
shrink_data = tnse.fit_transform(data)
print "TNSE"
print shrink_data
print '\n'

# pca = decomposition.PCA(n_components=2)
# a2 = pca.fit_transform(a)
# print "PCA"
# print a2