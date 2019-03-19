import operator
import math

d = []

def preprocess(input_str):
    import re
    from nltk.tokenize import sent_tokenize, word_tokenize
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize

    input_str = input_str.lower()
    input_str = re.sub(r'\d+', '', input_str)
    input_str = input_str.translate(str.maketrans("", "", string.punctuation))
    input_str = str(input_str.strip())
    input_str = word_tokenize(input_str)
    stop_words = set(stopwords.words('english'))
    input_str = [i for i in input_str if not i in stop_words]

    s = ""
    stemmer = PorterStemmer()
    for word in input_str:
        s += (stemmer.stem(word) + " ")
    return s


def file(i):
    with open("doc" + str(i) + ".txt", 'r') as myfile:
        FILE = myfile.read()
        FILE_PREPROCESS = preprocess(FILE)
        return FILE_PREPROCESS


d = []
for i in range(10):
    d.append(file(str(i + 1)))

T = 10
q = "home"
s = ""
l = []
w1 = set()

# words in documents and query
for i in range(len(d)):
    l1 = d[i].split()
    for i in range(len(l1)):
        w1.add(l1[i])
l2 = q.split()
for i in range(len(l2)):
    w1.add(l2[i])
w1 = list(w1)

# idf
idf = []
for i in range(len(w1)):
    count = 0
    for j in range(len(d)):
        if w1[i] in d[j].split():
            count += 1
    val = math.log2(len(d) / count)
    idf.append([w1[i], val])
print(idf)

# [word,count in a document]
m = []
for i in range(len(d)):
    m1 = []
    for j in range(len(w1)):
        m1.append([w1[j], d[i].split().count(w1[j])])
    m.append(m1)
print(m)

# [word,count in query]
max1 = -1
m1 = []
for j in range(len(w1)):
    max1 = max(max1, q.split().count(w1[j]))
    m1.append([w1[j], q.split().count(w1[j])])
m.append(m1)

# normalized tf
for i in range(len(m)):
    max1 = -1  # max value
    for j in range(len(m[i])):
        max1 = max(max1, m[i][j][1])  # max occurrence in a document
    for j in range(len(m[i])):
        m[i][j][1] /= max1  # normalized value

#m[i] is vector for individual document
# tf*idf
for i in range(len(m)):
    for j in range(len(m[i])):
        t = m[i][j]
        for k in range(len(idf)):
            if idf[k][0] == m[i][j][0]: #comparing words for idf value
                m[i][j][1] = idf[k][1] * m[i][j][1]

# dot product
wt_l = []
for i in range(len(m) - 1):
    wt = 0
    for j in range(len(m[i])):
        if m[i][j][0] == m[len(m) - 1][j][0]: # if the words are same in document and query
            wt += m[i][j][1] * m[len(m) - 1][j][1] # last entry is query
    wt_l.append(wt)
print(wt_l)

#similarity matrix
sim_wt_l = []
for i in range(len(m)-1):
    wt = 0
    for j in range(len(m)-1):
        for k in range(len(m[i])):
            if m[i][k][0] == m[j][k][0]: # if the words are same in document and query
                wt += m[i][k][1] * m[j][k][1] # last entry is query
    sim_wt_l.append(wt)
print(sim_wt_l)

#length of documents and query , last entry is of query
l1 = []
for i in range(len(m)-1):
    l = 0
    for j in range(len(m[i])):
        l += m[i][j][1] * m[i][j][1]
    l = math.sqrt(l)
    l1.append(l)
print(l1)

# cosine similarity
cos_sim = {}
for i in range(len(wt_l)):
    cos_sim[i] = (wt_l[i] / (l1[i] * l1[len(l1) - 1]))
print(cos_sim)
