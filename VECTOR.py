import math
d = []

with open("doc1.txt", 'r') as myfile:
    doc1 = myfile.read()
d.append(doc1)

with open("doc2.txt", 'r') as myfile:
    doc2 = myfile.read()
d.append(doc2)

with open("doc3.txt", 'r') as myfile:
    doc3 = myfile.read()  # type: str
d.append(doc3)

with open("doc4.txt", 'r') as myfile:
    doc4 = myfile.read()  # type: str
d.append(doc4)

with open("doc5.txt", 'r') as myfile:
    doc5 = myfile.read()

d.append(doc5)
with open("doc6.txt", 'r') as myfile:
    doc6 = myfile.read()
d.append(doc6)

with open("doc7.txt", 'r') as myfile:
    doc7 = myfile.read()  # type: str
d.append(doc7)

with open("doc8.txt", 'r') as myfile:
    doc8 = myfile.read()  # type: str
d.append(doc8)

with open("doc9.txt", 'r') as myfile:
    doc9 = myfile.read()  # type: str
d.append(doc9)
with open("doc10.txt", 'r') as myfile:
    doc10 = myfile.read()  # type: str
d.append(doc10)


T = 10

q="Circling round the earth"
s = ""
l = []
w1 = set()

for i in range(len(d)):
    l1 = d[i].split()
    for i in range(len(l1)):
        w1.add(l1[i])

l2=q.split();
for i in range(len(l2)):
    w1.add(l2[i])


w1 = list(w1)
#print(w1)
idf = []
for i in range(len(w1)):
    count = 0
    for j in range(len(d)):
        if w1[i] in d[j].split():
            count += 1

    val = math.log2(len(d) / count)

    idf.append([w1[i], val])




print(idf)
m = []

for i in range(len(d)):
    m1 = []
    for j in range(len(w1)):
        m1.append([w1[j], d[i].split().count(w1[j])])
    m.append(m1)


max1 = -1
m1 = []

for j in range(len(w1)):
    max1 = max(max1 , q.split().count(w1[j]))
    m1.append([w1[j], q.split().count(w1[j])])
m.append(m1)

#normalized tf

for i in range(len(m)):
    max1 = -1
    for j in range(len(m[i])):
        #max1=-1;
        #print(str(m[i][j])+"  "+str(m[i][j][1]))
        max1=max(max1,m[i][j][1])


    for j in range(len(m[i])):
        #max1=-1;
        #print(str(m[i][j])+"  "+str(m[i][j][1]))
        m[i][j][1]/=max1



#for i in range(len(m)):
 #   k = m[i]
  #  print(k)
    # for j in range(len(k))

#tf*idf
for i in range(len(m)):

    # print(k)
    for j in range(len(m[i])):
        t = m[i][j]
        for k in range(len(idf)):
            if idf[k][0] == m[i][j][0]:

                m[i][j][1] = idf[k][1] * m[i][j][1]

#dot product
wt_l=[]
for i in range(len(m)-1):
    wt=0
    for j in range(len(m[i])):
        if m[i][j][0]==m[len(m)-1][j][0]:
            wt+=m[i][j][1]*m[len(m)-1][j][1]
    wt_l.append(wt)
print(wt_l)

l1=[]
for  i in range(len(m)):
    l=0
    for j in range(len(m[i])):
        l+=m[i][j][1]*m[i][j][1]
    l=math.sqrt(l)
    l1.append(l)
print(l1)

#cosine similarity
cos_sim={}
for i in range(len(wt_l)):
    cos_sim[i]=(wt_l[i]/(l1[i]*l1[len(l1)-1]))
print(cos_sim)
