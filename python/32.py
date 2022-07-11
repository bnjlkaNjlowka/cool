import itertools
def Pdelt_num(n):
    list_Pdelt=[1]
    delt=2
    i=0
    ans=n
    while ans!=1:
        if ans%delt!=0:
            delt=delt+1
            continue
        else:
            list_Pdelt.append(delt)
            ans=ans/delt
            i=i+1
    list_Pdelt.remove(1)
    return list_Pdelt



def delt_num(Pdelt):
    aye=[]
    for i in range(1,len(Pdelt)+1):
        aye.append(list(itertools.combinations(Pdelt,i)))
    delt=[]
    for spisok1 in range(len(aye)):
        for spisok2 in range(len(aye[spisok1])):
            temp_num=1
            for spisok3 in range(len(aye[spisok1][spisok2])):
                temp_num=temp_num*aye[spisok1][spisok2][spisok3]
                delt.append(temp_num)
    i=0
    delt2=[]
    delt.sort()
    while i!=len(delt):
        if delt.count(delt[i])!=1:
            delt2.append(delt[i])
            i=i+delt.count(delt[i])
        else:
            delt2.append(delt[i])
            i=i+1
    return delt2


def check_ans(n):
    delt_n=delt_num(Pdelt_num(n))
    #print(delt_n)
    for i in range(0,len(delt_n)-1):
        proizv=delt_n[i]*delt_n[len(delt_n)-2-i]
        str_num1=str(delt_n[i])
        str_num2=str(delt_n[len(delt_n)-2-i])
        str_proizv=str(proizv)
        temp_sum=str_num1+str_num2+str_proizv
        str_sum=list(temp_sum)
        str_sum.sort()
        schet=1
        if len(str_sum)!=9:
            continue
        for b in str_sum:
            if b==str(schet):
                schet=schet+1
            else:
                break
            if b==str(len(str_sum)):
                return 'Пан-цифровое произведение'
    return 'Не панцифровое произведение'



ans=0
for i in range(2,10000,2):
    temp_str=check_ans(i)
    #print(i)
    if temp_str=='Пан-цифровое произведение':
        ans=ans+i
        #print(i)
print('Сумма пан-цифровых произведений:',ans)
