import numpy as np

# Read data
data = []
nDoc = 0
with open("/home/cuong/PycharmProjects/AnchorWord/Data/tiny.anchor") as f:
    for line in f:
        words = line.strip().split()
        if len(words) == 1:
            continue
        data.append(line.strip())
        nDoc += 1
print "Data: "
for item in data:
    print item


# Build dictionary
wordID = dict()
rwordID = dict()
nWord = 0
for doc in data:
    words = doc.split()
    for word in words:
        if word not in wordID:
            wordID[word] = nWord;
            rwordID[nWord] = word;
            nWord += 1
print "Dictionary: "
for item in rwordID:
    print str(item) + ': ' + str(rwordID[item])
print 'nWord: ' + str(nWord)

# Calculate word-doc matrix ( V x D matrix)
H_count = [[0 for col in range(nDoc)] for row in range(nWord)]
H_diag = [[0 for col in range(nWord)] for row in range(nWord)]
# for i in range(10):
#     for j in range(5):
#         H[i][j] = i
# for item in H:
#     print item
for col in range(nDoc):
    words = data[col].split()
    nd = len(words)      # Number of word in doc
    for word in words:
        row = wordID[word]
        H_count[row][col] += 1
    for row in range(nWord):
        if H_count[row][col] != 0:
            H_diag[row][row] += float(H_count[row][col]) / (nd * (nd - 1))
            H_count[row][col] = float(H_count[row][col]) / np.sqrt(nd * (nd - 1))
print "H_count: "
for item in H_count:
    print item

print "H_diag: "
for item in H_diag:
    print item
Q = np.subtract(np.dot(np.matrix(H_count), np.matrix(H_count).getT()), np.matrix(H_diag))
print "Q matrix: "
for item in Q.tolist():
    print item
