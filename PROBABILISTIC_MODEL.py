import operator
d = []
def preprocess(input_str):
    import re
    from nltk.tokenize import sent_tokenize, word_tokenize
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize


    # case
    input_str = input_str.lower()
    # numbers
    result = re.sub(r'\d+', '', input_str)
    # punctuations
    input_str = input_str.translate(str.maketrans("", "", string.punctuation))
    # space
    input_str = str(input_str.strip())

    # tokenize
    # input_str= sent_tokenize(input_str)
    input_str = word_tokenize(input_str)

    # stop words removal
    stop_words = set(stopwords.words('english'))
    input_str = [i for i in input_str if not i in stop_words]
    # print(input_str)

    # stemming
    s=""
    stemmer = PorterStemmer()
    for word in input_str:
        s+=(stemmer.stem(word)+" ")
    return s

with open("doc1.txt", 'r') as myfile:
    doc1 = myfile.read()
    doc1=preprocess(doc1)
d.append(doc1)

with open("doc2.txt", 'r') as myfile:
    doc2 = myfile.read()
    doc2=preprocess(doc2)
d.append(doc2)

with open("doc3.txt", 'r') as myfile:
    doc3 = myfile.read()
    doc3=preprocess(doc3) # type: str
d.append(doc3)

with open("doc4.txt", 'r') as myfile:
    doc4 = myfile.read()  # type: str
    doc4=preprocess(doc4)
d.append(doc4)

with open("doc5.txt", 'r') as myfile:
    doc5 = myfile.read()
    doc5=preprocess(doc5)

d.append(doc5)
with open("doc6.txt", 'r') as myfile:
    doc6 = myfile.read()
    doc6=preprocess(doc6)
d.append(doc6)

with open("doc7.txt", 'r') as myfile:
    doc7 = myfile.read()  # type: str
    doc7=preprocess(doc7)
d.append(doc7)

with open("doc8.txt", 'r') as myfile:
    doc8 = myfile.read()  # type: str
    doc8=preprocess(doc8)
d.append(doc8)

with open("doc9.txt", 'r') as myfile:
    doc9 = myfile.read()  # type: str
    doc9=preprocess(doc9)
d.append(doc9)
with open("doc10.txt", 'r') as myfile:
    doc10 = myfile.read()  # type: str
    doc10=preprocess(doc10)
d.append(doc10)


T = 10

relevant = [d[0], d[1], d[2], d[3], d[4],d[5],d[6],d[7],d[8],d[9]]
rel = d[0] + d[1] + d[2] + d[3] + d[4]+d[5]+d[6]+d[7]+d[8]+d[9]

words = []
s = ""
#with open("t1.txt", 'r') as myfile:
 #   q = myfile.read()  # type: str

q=input()
for i in range(T):
    s += d[i]
s += q

words.append(list(s.split()))

words1 = list(set(list(s.split())))

# print(words1)
# q="ach"



N1_W = []  # COUNT OF TERMS IN  DOCUMENTS
for i in range(len(words1)):
    count = 0
    for j in range(len(relevant)):
        if words1[i] in relevant[j]:
            count += 1
    N1_W.append([(words1[i]), count,((T-count+0.5)/(count+0.5))])

print(N1_W)

final = {}

for i in range(len(d)):
    d1=set(d[i].split())

    d2=set(q.split())

    d3=list(d1&d2)

    res=1
    for j in range(len(d3)):
        for k in range(len(N1_W)):
            if((d3[j])==N1_W[k][0]):
                res*=N1_W[k][2]

    final[i] = res
    print(res)



sorted_x = sorted(final.items(), key=operator.itemgetter(1),reverse=True)

print(sorted_x)
# NEW DOC = D6


