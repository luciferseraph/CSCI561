import sys
import os
def marginalutility(prob,disease,patient,disease_num,patient_num):
    marginal=[]
    for k in range(patient_num):

        each_patient=patient[k]
        each_prob=prob[k]
        dis_marginal={}
        for n in range(disease_num):
            test=each_patient[n]

            #print(test)

            symptom_num=disease[n][1]
            symptom_list=disease[n][3]
            p_symptom_disease=disease[n][4]
            p_symptom_not_disease=disease[n][5]
            #print(symptom_list)
            disease_name=each_prob[n][0]
            p_under_disease=each_prob[n][1]
            p_under_not_disease=each_prob[n][2]-p_under_disease
            disease_posterior=each_prob[n][3]
            increase_name='none'
            increase_flag='N'
            increase_delta=0
            decrease_name='none'
            decrease_flag='N'
            decrease_delta=0
            for i in range(symptom_num):

                if(test[i]=='U'):

                    pa_d=p_symptom_disease[i]
                    pa_not_d=p_symptom_not_disease[i]

                    #true
                    tmp=(p_under_disease*pa_d)/(p_under_disease*pa_d+p_under_not_disease*pa_not_d)
                    #increase
                    if(symptom_list[i]=="rakpcs" or symptom_list[i]=="rncj" ):
                        print(symptom_list[i],pa_d,pa_not_d,tmp)
                    if((tmp-disease_posterior)>increase_delta):
                        if(increase_name=="rakpcs"):

                            print(symptom_list[i],increase_name)
                            print((tmp-disease_posterior),increase_delta)
                        increase_name=symptom_list[i]
                        increase_flag='T'
                        increase_delta=tmp-disease_posterior
                    elif((tmp-disease_posterior)==increase_delta and increase_delta!=0 ):

                        if(cmp(symptom_list[i],increase_name)<0):
                            increase_name=symptom_list[i]
                            increase_flag='T'
                    #decrease
                    elif((tmp-disease_posterior)<decrease_delta):
                        decrease_name=symptom_list[i]
                        decrease_flag='T'
                        decrease_delta=tmp-disease_posterior
                    elif((tmp-disease_posterior)==decrease_delta and decrease_delta!=0 ):
                        if(cmp(symptom_list[i],decrease_name)<0):
                            decrease_name=symptom_list[i]
                            decrease_flag='T'

                    #false
                    tmp=p_under_disease*(1-pa_d)/(p_under_disease*(1-pa_d)+p_under_not_disease*(1-pa_not_d))
                    #increase
                    if((tmp-disease_posterior)>increase_delta):
                        increase_name=symptom_list[i]
                        increase_flag='F'
                        increase_delta=tmp-disease_posterior
                    elif((tmp-disease_posterior)==increase_delta and increase_delta!=0):
                        if(cmp(symptom_list[i],increase_name)<0):
                            increase_name=symptom_list[i]
                            increase_flag='F'
                    #decrease
                    elif((tmp-disease_posterior)<decrease_delta):
                        decrease_name=symptom_list[i]
                        decrease_flag='F'
                        decrease_delta=tmp-disease_posterior
                    elif((tmp-disease_posterior)==decrease_delta and decrease_delta!=0):
                        if(cmp(symptom_list[i],decrease_name)<0):
                            decrease_name=symptom_list[i]
                            decrease_flag='F'
            #print(increase_name,increase_flag,decrease_name,decrease_flag)
            value=[increase_name,increase_flag,decrease_name,decrease_flag]
            dis_marginal.setdefault(disease_name,[]).extend(value)
        #print(dis_marginal)
        marginal.append(dis_marginal)
    return marginal






def min_max(prob,disease,patient,disease_num,patient_num):
    total_minmax=[]
    for k in range(patient_num):

        each_patient=patient[k]
        each_minmax={}
        for n in range(disease_num):
            this_disease=disease[n]
            disease_name_sub=this_disease[0]
            symptom_num_sub=this_disease[1]
            p_disease=this_disease[2]
            symptom_name=this_disease[3]
            p_symptom_disease=this_disease[4]
            p_symptom_not_disease=this_disease[5]
            each_prob=prob[k][n]
            lab_result=each_patient[n]
            p_min=each_prob[3]
            p_max=each_prob[3]
            p_under_disease=each_prob[1]#positive
            p_under_not_disease=each_prob[2]-p_under_disease#negative
            p_max_dis=p_under_disease
            p_max_nodis=p_under_not_disease
            p_min_dis=p_under_disease
            p_min_nodis=p_under_not_disease
            for j in range(symptom_num_sub):
                if (lab_result[j]=='U'):
                    #max
                    p_max_dis_1=p_max_dis*p_symptom_disease[j]
                    p_max_nodis_1=p_max_nodis*p_symptom_not_disease[j]
                    p_max_1=p_max_dis_1/(p_max_dis_1+p_max_nodis_1)
                    p_max_dis_2=(p_max_dis*(1-p_symptom_disease[j]))
                    p_max_nodis_2=p_max_nodis*(1-p_symptom_not_disease[j])
                    p_max_2=p_max_dis_2/(p_max_dis_2+p_max_nodis_2)
                    if(p_max_1>p_max_2):
                        p_max=p_max_1
                        p_max_dis=p_max_dis_1
                        p_max_nodis=p_max_nodis_1
                    else:
                        p_max=p_max_2
                        p_max_dis=p_max_dis_2
                        p_max_nodis=p_max_nodis_2

                    #min
                    p_min_dis_1=p_min_dis*p_symptom_disease[j]
                    p_min_nodis_1=p_min_nodis*p_symptom_not_disease[j]
                    p_min_1=p_min_dis_1/(p_min_dis_1+p_min_nodis_1)
                    p_min_dis_2=(p_min_dis*(1-p_symptom_disease[j]))
                    p_min_nodis_2=p_min_nodis*(1-p_symptom_not_disease[j])
                    p_min_2=p_min_dis_2/(p_min_dis_2+p_min_nodis_2)

                    if(p_min_1<p_min_2):
                        p_min=p_min_1
                        p_min_dis=p_min_dis_1
                        p_min_nodis=p_min_nodis_1
                    else:
                        p_min=p_min_2
                        p_min_dis=p_min_dis_2
                        p_min_nodis=p_min_nodis_2


                    #special case
                    if(p_min>p_max):
                        p_max,p_min=p_min,p_max
                        p_max_dis,p_min_dis=p_min_dis,p_max_dis
                        p_max_nodis,p_min_nodis=p_min_nodis,p_max_nodis

            tmp=["%.4f" %p_min,"%.4f" %p_max]
            each_minmax.setdefault(disease_name_sub,[]).extend(tmp)
        total_minmax.append(each_minmax)
    return total_minmax











def p_has_disease(disease,patient,disease_num,patient_num):
    prob_all=[]
    unknow_all=[]
    for k in range(patient_num):

        prob_each=[]
        unknow_each=[]
        for n in range(disease_num):
            this_disease=disease[n]
            disease_name_sub=this_disease[0]
            symptom_num_sub=this_disease[1]
            p_disease=this_disease[2]
            symptom_name=this_disease[3]
            p_symptom_disease=this_disease[4]
            p_symptom_not_disease=this_disease[5]
            lab_results=patient[k][n]
            under_positive=1
            under_negative=1

            symptom_unknow=[]

            for j in range(0,symptom_num_sub):

                if(lab_results[j]=='T'):
                    under_positive=under_positive*p_symptom_disease[j]
                    under_negative=under_negative*p_symptom_not_disease[j]
                elif(lab_results[j]=='F'):
                    under_positive=under_positive*(1-p_symptom_disease[j])
                    under_negative=under_negative*(1-p_symptom_not_disease[j])
                else:
                    symptom_unknow.append(symptom_name[j])

            numerator=under_positive*p_disease
            denominator=under_positive*p_disease+under_negative*(1-p_disease)
            posterior=numerator/denominator
            prob=[disease_name_sub,numerator,denominator, posterior]
            #disease_unknow.append(symptom_unknow)

            prob_each.append(prob)
            unknow_each.append(symptom_unknow)
        prob_all.append(prob_each)
        unknow_all.append(unknow_each)

    return (prob_all,unknow_all)





inputFile = open(sys.argv[2])
#inputfilename="abc.txt"
#inputFile = open("10case.txt")
#[dirname,output]=os.path.split(sys.argv[2])
#outfilename=priorname+"_inference"+extension

#output=output.replace('.txt','')
#output=output+"_inference.txt"

line=inputFile.readline()
spl = line.strip().split(' ')
disease_num=int(spl[0])
patient_num=int(spl[1])

spl=line.strip().split(' ')
disease=[]
for n in range(0,disease_num):
    each_disease=[]
    for i in range(0,4):
        line=inputFile.readline()
        if i ==0:
            spl = line.strip().split(' ')
            disease_name=spl[0]
            symptom_num=int(spl[1])
            prob_d=float(spl[2])
            each_disease.append(disease_name)
            each_disease.append(symptom_num)
            each_disease.append(prob_d)
        elif i==3:
            spl=eval(line)
            each_disease.append(spl)
            disease.append(each_disease)
        else:
            spl=eval(line)
            each_disease.append(spl)

patient=[]
for k in range(0,patient_num):
    each_patient=[]
    for n in range(0,disease_num):
        line=inputFile.readline()
        if n==disease_num-1:
            spl=eval(line)
            each_patient.append(spl)
            patient.append(each_patient)
        else:
            spl=eval(line)
            each_patient.append(spl)

#print(outfilename)

inputFile.close()
prob,unknow=p_has_disease(disease,patient,disease_num,patient_num)
'''for k in range(0,patient_num):
    name="Patient-"+str(k+1)+":"
    print(name)
    for n in range(0,disease_num):
        print("%.4f" %prob[k][n][3]),

for k in range(patient_num):
    for n in range(disease_num):
        print(unknow[k][n])
'''
p_d_a=[]
for k in range(patient_num):
    each_pda={}
    for n in range(disease_num):
        name=prob[k][n][0]
        pda=("%.4f" %prob[k][n][3])


        each_pda[name]=pda
    p_d_a.append(each_pda)
#print(p_d_a)


print(patient[0][5])
minmax=min_max(prob,disease,patient,disease_num,patient_num)

marginal=marginalutility(prob,disease,patient,disease_num,patient_num)
output="10case_inference.txt"
outputFile = open(output, "w")
for k in range(patient_num):
    name="Patient-"+str(k+1)+":"+"\n"
    outputFile.write(name)
    outputFile.write(str(p_d_a[k])+"\n")
    outputFile.write(str(minmax[k])+"\n")
    outputFile.write(str(marginal[k])+"\n")
outputFile.close()
