import sys


connectives=["not", "and", "or"]
globalbianliang=[]

def mysymbols(myjuzi):
    global symbols
    #print("qq",myjuzi)
    for elem in myjuzi:
        if(isinstance(elem,list)):
            symbols=mysymbols(elem)
        elif(elem not in connectives and elem not in symbols):
            symbols+=elem
    return symbols


def checkTrue(caonima):
    if(isinstance(caonima,list)):
        if(caonima[0]!="not"):
            here="("+checkTrue((caonima[1]));
            if len(caonima)>=3:
                for j in range(2,len(caonima)):
                    here+=" or "+checkTrue(caonima[j])
            here+=")"
            return here
        else:
            return "not(vari[" +str(symbols.index(caonima[1]))+ "])"

    else:
        str1= "vari[" +str(symbols.index(caonima))+  "]"
        return  str1




def pureSymbol(elems,fuhao):
    value=[]
    finallist=[]
    for i in range(len(fuhao)):
        value.append(-1)
    #print("total fuhao",fuhao)
    #print("total elems",elems)
    for elem in elems:
        #print("out elem",elem)
        #print("out elems",elems)
        if(isinstance(elem,list)):
            if(elem[0]=="not" and elem[1] in fuhao):
                xiabiao=fuhao.index(elem[1])
                if (value[xiabiao]==-1):
                    value[xiabiao]=0
                elif(value[xiabiao]==1):
                    value[xiabiao]=1000
            else:

                for temp in elem[1:len(elem)]:
                    #print("check it",temp)
                    flag=0
                    yuansu=""
                    if(isinstance(temp,list)):
                        #print("listins",temp)
                        if(temp[0]=="not"):
                            flag=1

                            yuansu=temp[1]
                        #print("yuansu",yuansu)

                    else:
                        #print("else")
                        yuansu=temp
                    if (len(yuansu)!=0 and yuansu in fuhao):
                        #print("fuhao",fuhao)
                        xiabiao=fuhao.index(yuansu)
                        #print("xiabiao",xiabiao)
                        if (flag==0):
                            if(value[xiabiao]==-1):
                                value[xiabiao]=1
                            elif(value[xiabiao]==0):
                                value[xiabiao]=-1000
                        else:
                            if (value[xiabiao]==-1):
                                value[xiabiao]=0
                            elif(value[xiabiao]==1):
                                value[xiabiao]=1000

        elif(elem in fuhao):
            xiabiao=fuhao.index(elem)
            if(value[xiabiao]==-1):
                value[xiabiao]=1
            elif(value[xiabiao]==0):
                value[xiabiao]=-1000

    for i in range(len(fuhao)):
        if(value[i]==1):
            finallist.append(["true",fuhao[i]])
        elif(value[i]==0):
            finallist.append(["false",fuhao[i]])
    return finallist



def myDPLL(symbols,clauses,vari):
    flag=1
    zhende=[]
    for elem in clauses:

        if(eval(checkTrue(elem))):

            zhende.append(elem)
        else:
            flag=0
            break
    #print("flag",flag)
    if flag==0:
        if (len(symbols)!=0):
            purelist=[]
            #print("usepuresymbol",symbols)
            #print("clauses",clauses)
            purelist=pureSymbol(clauses,symbols)
            #print("purelist", purelist)
            symbollist=[]
            if(len(purelist)!=0):
                for i in range(len(purelist)):
                    temp2=purelist[i]

                    xiabiao=symbols.index(temp2[1])
                    vari[xiabiao]=temp2[0]
                    symbollist.append(temp2[1])

                newcla=[tcla for tcla in clauses if not(tcla in zhende)]
                newsymb=[tcy for tcy in symbols if not (tcy in symbollist) ]
                if(len(newsymb)==0):
                    #print( "vari",vari)
                    return vari
                #print( "2vari",vari)
                return myDPLL(newsymb,newcla,vari)
    else:
        #print( "3vari",vari)
        return vari

def splitRule(symbols,clauses,vari):
    outlist=None
    flag=-1
    #print("clauses len",len(clauses))
    if(len(clauses)>2):

        for symbol in symbols:
            isIncude=0
            outlist=None
            tmp=[]
            xiabiao=symbols.index(symbol)
            vari[xiabiao]="true"
            flag=1
            #print("symbol",symbol)
            for i in range(len(clauses)):
                #print("i",clauses[i])
                for j in range(len(clauses[i])):
                    #print("jv",j)
                    print("j",clauses[i][j])

                    if(symbol in clauses[i][j]):
                        isIncude=1
                        #print("isInclude")
                        if(isinstance(clauses[i][j],list)):
                            newtmp=clauses[i]
                            newtmp.pop(j)
                            if(len(newtmp)==1 and newtmp[0] in connectives):
                                print("1 only one")
                                break
                            elif(len(newtmp)==2 and newtmp[0]=="or"):
                                print("1 only two",newtmp[1])
                                tmp.append(newtmp[1])
                                print("1 add tmp1",tmp)
                                break
                            else:
                                tmp.append(newtmp)
                            #print("tmp1",tmp)
                                break
                        else:
                            break
                if(isIncude==0):
                    print("isIncude=0")
                    tmp.append(clauses[i])
                print("tmp1-i",tmp)
            print("final tmp1",tmp)
            if(len(tmp)!=0):
                outlist=myDPLL(symbols,tmp,vari)
            if (outlist!=None):
                return (flag,outlist)
            else:
                outlist=None
                #print("false")
                tmp=[]
                xiabiao=symbols.index(symbol)
                vari[xiabiao]="false"
                flag=1
                isIncude=0
                #print("symbol",symbol)
                for i in range(len(clauses)):
                    print("i",clauses[i])
                    for j in range(len(clauses[i])):
                       # print("jv",j)
                        print("j",j,clauses[i][j])
                        if(symbol in clauses[i][j]):
                            isIncude=1
                            if(isinstance(clauses[i][j],list)):

                                break
                            else:
                                newtmp=[]

                                newtmp=clauses[i]
                                print("newtmp",newtmp)
                                newtmp.pop(j)
                                print("2 tmp2",newtmp)
                                if(len(newtmp)==1 and newtmp[0] in connectives):
                                    print("2 only one")
                                    break
                                if(len(newtmp)==2 and newtmp[0]!="not"):
                                    print("2 only two")
                                    tmp.append(newtmp[1])
                                    print("2 add tmp1",tmp)
                                    break
                                else:
                                    tmp.append(newtmp)
                                    print("2add tmp2",tmp)
                            #print("tmp1",tmp)
                                    break
                    if(isIncude==0):
                        tmp.append(clauses[i])
                    #print("tmp2",tmp)
                        print("tmp2-i",tmp)
                print("final tmp2",tmp)
                if(len(tmp)!=0):
                    outlist=myDPLL(symbols,tmp,vari)
                if (outlist!=None):
                    return (flag,outlist)

        return (flag,outlist)
    else:
        return (flag,outlist)










#inputFile = open(sys.argv[2])
inputFile=open("CNF_test_sentences.txt")
outputFile = open("CNF_satisfiability.txt", "w")

linenum=0
count=0
for line in inputFile:
    if(count==0):
        linenum=eval(line)
        count=1
    else:
        juzi=eval(line)
        symbols=[]

        vari=[]
        symbols=mysymbols(juzi)
        clauses=[]
        if(juzi[0]=="and"):
            for i in range(1,len(juzi)):
                clauses.append(juzi[i])
        else:
            clauses.append(juzi)


        #print "symbols",symbols
        #print("clauses",clauses)
        #for i in range(len(symbols)):
        #    vari.append("true")
        vari=["true" for i in range(len(symbols))]
        outcome=None
        #print("call")
        outcome=myDPLL(symbols,clauses,vari)
        #print("outcome",outcome)
        outcolist=[]

        if outcome!= None:
            # outputFile.write(str(outcome)+"\n")
            outcolist=["true"]
            for i in range(len(outcome)):
                tempstr=""

                tempstr=str(symbols[i]) + "=" + str(outcome[i])
                outcolist.append(tempstr)

            print(str(outcolist)+"\n")
            outputFile.write(str(outcolist)+"\n")
        else:
            newoutcome=None
            print("clauses",clauses)
            flag,newoutcome=splitRule(symbols,clauses,vari)
            print("newoutcome",newoutcome)
            if newoutcome!= None:

            # outputFile.write(str(outcome)+"\n")
                outcolist=["true"]
                for i in range(len(newoutcome)):
                    tempstr=""

                    tempstr=str(symbols[i]) + "=" + str(newoutcome[i])
                    outcolist.append(tempstr)
                print(str(outcolist)+"\n")
                outputFile.write(str(outcolist)+"\n")
            else:
                outcolist=["false"]
                print(str(outcolist)+"\n")
                outputFile.write(str(outcolist)+"\n")

inputFile.close()
outputFile.close()