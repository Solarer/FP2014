import numpy as np
import matplotlib.pyplot as plt

def trapez(list):
    size=len(list)
    x=np.zeros(size)
    y=np.zeros(size)
    output=np.zeros(size)
    for pos,element in enumerate(list):
        x[pos]=element[0]
        y[pos]=element[1]
    print(x[0])
    print(y)

    for i in range(size-1,0,-1):
        # print(i)
        # print(np.absolute((x[i]-x[i-1]))/2*(y[i]+y[i-1]))
        output[i-1]+=output[i]+np.absolute((x[i]-x[i-1]))/2*(y[i]+y[i-1])

    out_file=open('output','w')
    for i,line in enumerate(output):
        print(i)
        out_file.write(str(x[i])+' '+str(output[i])+'\n')

input1=[]
input2=[]
file=open('int_data','r')
for cnt,line in enumerate(file):
    line=line.strip('\n').split()
    if(cnt<=41)and(cnt>0):
        input1.append((float(line[0]),float(line[1])))
    else:
        if(cnt>42):
            input2.append((float(line[0]),float(line[1])))

print('Input1: ',input1)
# print('Input2: ',input2)

# trapez(input1)
trapez(input2)

print('el1: ',input1[0])
