import sys


connectives = ["not", "and", "or", "implies", "iff"]


def cnfConvert(originlist):
   
    templist=[]
    if originlist[0] not in connectives:
        return originlist[0]
    
        
    elif originlist[0]== "and":
        templist=["and"]
        for i in range(1,len(originlist)):
            templist.append(cnfConvert(originlist[i]))

#return templist
    
    elif originlist[0]== "not":
        templist=["not"]
        templist.append(cnfConvert(originlist[1]))
# return templist


    elif originlist[0]== "or":
        templist=["or"]
        
        for i in range(1,len(originlist)):
            templist.append(cnfConvert(originlist[i]))
        

# return templist


    elif originlist[0]== "implies":
        templist=["or",["not",cnfConvert(originlist[1])],cnfConvert(originlist[2])]
# return templist
        
    elif originlist[0]== "iff":
        elem1=cnfConvert(["or",["not",cnfConvert(originlist[1])],cnfConvert(originlist[2])])
        elem2=cnfConvert(["or",["not",cnfConvert(originlist[2])],cnfConvert(originlist[1])])
        templist=["and", elem1,elem2]
# return templist
    return cnfImprove(templist)

def cnfImprove(originlist):
    
   
   

    if originlist[0]== "and":
        templist=["and"]
        resultlist=["and"]
        for i in range(1,len(originlist)):
            templist.append(cnfImprove(originlist[i]))
    
        for temp in templist[1:len(templist)]:
            flag=0
            if temp[0]=="and":
                flag=1
                temp.pop(0);
            
            if flag==0:
                resultlist.append(temp)
            else:
                for elem in temp:
                    resultlist.append(elem)
        return resultlist
    
    
    
    elif originlist[0]== "not":
        
        backlist=cnfImprove(originlist[1])
        if backlist[0] == "not":
            return backlist[1]
    
        elif backlist[0]== "and":
            templist=["or", cnfImprove(["not",backlist[1]]), cnfImprove(["not",backlist[2]])]
            return templist
        elif backlist[0] == "or":
            templist=["and",cnfImprove(["not",backlist[1]]),cnfImprove(["not",backlist[2]])]
            return templist
        else:
            return["not",backlist[0]]


    elif originlist[0]== "or":
        templist=["or"]
        resultlist=["or"]
        for i in range(1,len(originlist)):
            templist.append(cnfImprove(originlist[i]))

        for temp in templist[1:len(templist)]:
            flag=0
            if(temp[0]=="or"):
                flag=1
                temp.pop(0);

            if flag==0:
                resultlist.append(temp)
            else:
                for elem in temp:
                    resultlist.append(elem)
        return resultlist

    elif originlist[0] not in connectives:
        return originlist

def isEqual(first,second):
    
    if(len(first)!=len(second)):
        return False
   
    elif((not(isinstance(first,list))) and (not(isinstance(second,list)))):
        if(first==second):
            return True
        else:
            return False


    elif(isinstance(first,list) and isinstance(second,list)):
        for elem in first:
            if elem not in second:
                return False
        return True
    
    else:
        return False



def removeEqual(originlist):
    finallist=[originlist[0]]
    if(originlist[0] in connectives):
        #print originlist
        if(len(originlist)==3):
            originlist[1]=removeEqual(originlist[1])
            originlist[2]=removeEqual(originlist[2])
            if(isEqual(originlist[1],originlist[2])):
                return originlist[1]
        for i in range(1,len(originlist)):
            if(isinstance(originlist[i],list)):
                originlist[i]=removeEqual(originlist[i])

        finallist.append(originlist[1])
      
        for i in range(2,len(originlist)):
            #if false
            flag=0
            for elem in finallist:
                if (isEqual(elem,originlist[i])):
                    flag=1
                    break;
            if flag==0:
                finallist.append(originlist[i])
                    #print finallist
        if(len(finallist)==2 and finallist[0]!="not"):
            return finallist[1]
        return finallist
        
    else:
        return originlist



def CNF2(originlist):
    for j in range(len(originlist)):
        if(isinstance(originlist[j],list)):
            originlist[j]=CNF2(originlist[j])
    if(originlist[0]=="or"):
        finallist=originlist
        templist=originlist
        for i in range(1,len(templist)):
            
                if(originlist[i][0]=="and"):
                    
                    finallist=[]
                    finallist.append("and")
                    sublist=[]
                    sublist+=templist[i]
                    templist.pop(0)
                   
                    templist.pop(i-1)
                    
                    for j in range(len(sublist)):
                        if j==0:
                            continue
                        nowlist=[]
                        nowlist.append("or")
                        nowlist.append(sublist[j])
                        nowlist.extend(templist)
                        finallist.append(CNF2(nowlist))
                            # print finallist
                    break
                    
                    
                    '''finallist=["and"]
                    for cao in listand:
                            finallist.append(CNF2(["or",cao]+listor))
                    break;'''
        return finallist;




    return originlist;
                    
inputFile = open("sentences_test.txt")
#inputFile = open(sys.argv[2])
outputFile = open("sentences_CNF.txt","w")
flag = 0
givenline = 0
linenum=0
count=0


for line in inputFile:
    if flag==0:
        givenline=int(line)
        flag=1
    else:
        count+=1
        mylist = eval(line)
        rawlist = cnfConvert(mylist)
        #print rawlist
        betterlist=CNF2(rawlist)
        #        print betterlist
#   alist=removeEqual(betterlist)
#print alist
        bestlist=removeEqual(cnfImprove(CNF2(removeEqual(betterlist))))
        #print bestlist
        outputFile.write(str(bestlist)+"\n")

inputFile.close()
outputFile.close()


