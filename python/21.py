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

def summ_delt_num(delt_num):
    delt_num.pop()
    summ_delt=0
    for temp_num in delt_num:
        summ_delt=summ_delt+temp_num

    return summ_delt

n=int(input('Введите число:'))
ans=0
temp_list=[]
for i in range(1,n):
    temp_num=sum(delt_num(Pdelt_num(i)))
    temp_list.append(temp_num)
for i1 in range (len(temp_list)):
    for i2 in range (i1+2,len(temp_list),2):
        if temp_list[i1-1]-i1+1==i2 and temp_list[i2-1]-i2+1==i1:
            ans=ans+i1+i2


print('Сумма дружественных числе меньше',n,':',ans)
