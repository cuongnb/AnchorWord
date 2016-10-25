import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pyhull import convex_hull

from sklearn import decomposition
from sklearn.manifold import TSNE


def constructQMatrix(data_path):
    # Read data
    data = []
    nDoc = 0
    with open(data_path) as f:
        for line in f:
            words = line.strip().split()
            if len(words) == 1:
                continue
            data.append(line.strip())
            nDoc += 1
    # print "Data: "
    # for item in data:
    #     print item

    # Build dictionary
    wordID = dict()
    rwordID = dict()
    nWord = 0
    for doc in data:
        words = doc.split()
        for word in words:
            if word not in wordID:
                wordID[word] = nWord
                rwordID[nWord] = word
                nWord += 1
    # print "Dictionary: "
    # for item in rwordID:
    #     print str(item) + ': ' + str(rwordID[item])
    # print 'nWord: ' + str(nWord)

    # Calculate word-doc matrix ( V x D matrix)
    H_count = [[0 for col in range(nDoc)] for row in range(nWord)]
    H_diag = [[0 for col in range(nWord)] for row in range(nWord)]
    for col in range(nDoc):
        words = data[col].split()
        nd = len(words)  # Number of word in doc
        for word in words:
            row = wordID[word]
            H_count[row][col] += 1
        for row in range(nWord):
            if H_count[row][col] != 0:
                H_diag[row][row] += float(H_count[row][col]) / (nd * (nd - 1))
                H_count[row][col] = float(H_count[row][col]) / np.sqrt(nd * (nd - 1))
    # print "H_count: "
    # for item in H_count:
    #     print item

    # print "H_diag: "
    # for item in H_diag:
    #     print item
    Q = np.subtract(np.dot(np.matrix(H_count), np.matrix(H_count).getT()), np.matrix(H_diag))
    # print "Q matrix: "
    # for item in Q.tolist():
    #     print item
    return Q.tolist(), rwordID


def tnse(data, n_com):
    tnse = TSNE(n_components=n_com)
    shrink_data = tnse.fit_transform(data)
    return shrink_data


def pca(data, n_com):
    pca = decomposition.PCA(n_components=n_com)
    shrink_data = pca.fit_transform(data)
    return shrink_data


def quickhull(data, n_com):
    convexhull = convex_hull.ConvexHull(data)
    res = []
    anchor = []
    for item in convexhull.simplices:
        res.append(item.coords)
        for i in range(n_com):
            p = []
            for j in range(n_com):
                p.append(item.coords[i][j])
            anchor.append(p)

    return res, anchor


def main():
    # Build word-occurrence matrix
    data_path = '/home/cuong/PycharmProjects/AnchorWord/Data/tiny.anchor'
    Q, idword = constructQMatrix(data_path)
    print 'Number of word: ' + str(len(idword))
    # for item in Q:
    #     print item
    # for item in idword:
    #     print str(item) + ': ' + str(idword[item])

    # Project data into low-dimension space
    n_components = 3
    new_data = tnse(Q, n_components)
    # print new_data

    # Find convex hull on low-dimension data
    hull, anchor = quickhull(new_data, n_components)

    # for item in anchor:
    #     print item

    # Plot the data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(new_data)):
        item = new_data[i]
        ax.scatter(item[0], item[1], item[2], color='r', marker='o', label=i)
        if list(item) in anchor:
            ax.text(item[0], item[1], item[2],  '%s' % (idword[i]), size=20, zorder=1, color='k')

    # Plot convex hull of data
    for item in hull:
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
    print 'Number of anchor word: ' + str(len(anchor))

if __name__ == '__main__':
    main()
