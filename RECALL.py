RQ=list(input("relevant : ").split(" "))

AQ=list(input("answer set : ").split(" "))

RQ_AQ=[]
TOTAL_RELEVANT=len(RQ)
count=0
recall1=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
recall2=[]
precision=[]
for i in range(len(AQ)):
    if AQ[i] in RQ:
        count+=1
        recall2.append("%.2f" %(count/(i+1)))
        precision.append("%.2f" % (count/TOTAL_RELEVANT))
        print("Recall : "+ str(count/(i+1))+"  Precision : "+str(count/TOTAL_RELEVANT))

#interpolation
#average precision
avg_precison=[]
for i in range(len(precision)):
    sum=0
    for j in range(i+1):
        sum+=float(precision[j])

    avg_precison.append((sum/(i+1))*100)
print(avg_precison)

#recall
recall3=[]
for i in range(len(recall2)):

    print(recall2[i])

import matplotlib.pyplot as plt
plt.plot(recall2,precision,alpha=0.5)
plt.xlabel(recall2)
plt.ylabel(precision)
plt.title('My first graph!')
plt.show()
#3 5 9 25 39 44 56 71 89 123
#123 84 56 6 8 9 511 129 187 25 38 48 250 113 3

print ("har mean is :");
e_1=[];
e_2=[];
e_3=[];
re=recall3
p=precision
print ("E measures when b=1 \n");
for i in range(0,c):
    e_1.append(1-(2/((1/re[i])+(1/p[i]))));
print(e_1);


print ("E measures when b<1  \n");
l=int(input("enter b less than 1"));
for i in range(0,c):
    e_2.append(1-(1/((1/re[i])+(1/p[i]))));
print(e_2);

print ("E measures when b>1  \n");
l=int(input("enter b greater than 1"));
for i in range(0,c):
    e_3.append(1-((1+(l*l))/(((l*l)/re[i])+(1/p[i]))));
print(e_3);