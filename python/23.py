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


big_num=[]
n=28124
for i in range(1,n):
    if i<sum(delt_num(Pdelt_num(i)))-i:
        big_num.append(i)
#print(big_num)
summ=0
aye=[]
temp_list=list(itertools.combinations_with_replacement(big_num,2))
for i in range(len(temp_list)):
    temp_num=sum(temp_list[i])
    if temp_num>n:
        continue
    aye.append(temp_num)

aye.sort()

i=0
schet=0
list_num_ans=[24]
while i!=len(aye):
    if aye[i]==list_num_ans[schet]:
        i=i+1
    else:
        list_num_ans.append(aye[i])
        i=i+1
        schet=schet+1

#print(list_num_ans)
summ_big_num=sum(list_num_ans)
summ_nat=int(n*(n+1)/2)
ans=summ_nat-summ_big_num
print(ans)
