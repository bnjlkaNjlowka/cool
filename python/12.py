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



def count_delt_num(Pdelt):
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
    return (len(delt2)+1)

n=int(input('Введите число:'))
temp_num=1
a=0
while a<n:
    num=int((temp_num*(temp_num+1))/2)
    temp_num=temp_num+1
    a=count_delt_num(Pdelt_num(num))
print('Треугольное число у которого больше',n,'делителей:',num)
