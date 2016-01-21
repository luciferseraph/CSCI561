import sys
import os
inputFile = open(sys.argv[2])
#inputFile=open("sample_input_ec.txt")
#inputData=open(sys.argv[4])
#inputData=open("Risk_Factor_data.txt")
#[dirname,output]=os.path.split(sys.argv[2])


line=inputData.readline()

spl = line.strip().split('\t')
print(spl)
name=spl
num=10000
#num=3
length=len(spl)
income=[0,0,0,0]
exercise=[[0,0,0,0],[0,0,0,0]]
smoke=[[0,0,0,0],[0,0,0,0]]
bmi=[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]
bp=[[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]],[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]]
cholesterol=[[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]],[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]]
angina=[[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]],[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]]
attack=[[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]],[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]]
stroke=[[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]],[[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]]
diabetes=[[0,0,0,0],[0,0,0,0]]

for i in range(num):
    line=inputData.readline()
    spl=line.strip().split('\t')
    for k in range(length):
        if(name[k]=="income"):
            tmp=int(spl[k])
            if(tmp<25000):
                income[0]=income[0]+1
            elif(tmp>=25001 and tmp<=50000):
                income[1]=income[1]+1
            elif(tmp>=50001 and tmp<=75000):
                income[2]=income[2]+1
            else:
                income[3]=income[3]+1
        if(name[k]=="bmi"):
            tmp=spl[k]
            tmp1=spl[]
            tmp2=spl[]
            if(tmp=="underweight"):
                bmi[0]=bmi[0]+1
            elif(tmp=="normal"):
                bmi[1]=bmi[1]+1
            elif(tmp=="overweight"):
                bmi[2]=bmi[2]+1
            else:
                bmi[3]=bmi[3]+1
        if(name[k]=="exercise"):
            tmp=spl[k]
            if(tmp=="no"):
                exercise[0]=exercise[0]+1
            else:
                exercise[1]=exercise[1]+1
        if(name[k]=="smoke"):
            tmp=spl[k]
            if(tmp=="no"):
                smoke[0]=smoke[0]+1
            else:
                smoke[1]=smoke[1]+1
        if(name[k]=="bp"):
            tmp=spl[k]
            if(tmp=="no"):
                bp[0]=bp[0]+1
            else:
                bp[1]=bp[1]+1
        if(name[k]=="cholesterol"):
            tmp=spl[k]
            if(tmp=="no"):
                cholesterol[0]=cholesterol[0]+1
            else:
                cholesterol[1]=cholesterol[1]+1

        if(name[k]=="angina"):
            tmp=spl[k]
            if(tmp=="no"):
                angina[0]=angina[0]+1
            else:
                angina[1]=angina[1]+1
        if(name[k]=="attack"):
            tmp=spl[k]
            if(tmp=="no"):
                attack[0]=attack[0]+1
            else:
                attack[1]=attack[1]+1
        if(name[k]=="stroke"):
            tmp=spl[k]
            if(tmp=="no"):
                stroke[0]=stroke[0]+1
            else:
                stroke[1]=stroke[1]+1
        if(name[k]=="diabetes"):
            tmp=spl[k]
            if(tmp=="no"):
                diabetes[0]=diabetes[0]+1
            else:
                diabetes[1]=diabetes[1]+1
#print(income,exercise,smoke,bmi,bp,cholesterol,angina,attack,stroke,diabetes)
#print(income)
income=[float(item)/float(num) for item in income]
#print(income)
exercise=[float(item)/float(num) for item in exercise]
smoke=[float(item)/float(num) for item in smoke]
bmi=[float(item)/float(num) for item in bmi]
bp=[float(item)/float(num) for item in bp]
cholesterol=[float(item)/float(num) for item in cholesterol]
angina=[float(item)/float(num) for item in angina]
attack=[float(item)/float(num) for item in attack]
stroke=[float(item)/float(num) for item in attack]
diabetes=[float(item)/float(num) for item in diabetes]
print(income,exercise,smoke,bmi,bp,cholesterol,angina,attack,stroke,diabetes)
inputData.close()
query_num=eval(inputFile.readline())
query=[]
for n in range(query_num):
    tmp=eval(inputFile.readline())
    query.append(tmp)
print(query[0])
