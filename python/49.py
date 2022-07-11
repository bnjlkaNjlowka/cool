import itertools

def perestanovka(n):
    str_num=str(n)
    list_num=list(itertools.permutations(str_num))
    return list_num

def check_perestanovka(n1,n2):
    list_num=perestanovka(n1)
    str_num2=str(n2)
    temp_str_num2=[]
    for i in str_num2:
        temp_str_num2.append(i)
    for i in list_num:
        temp_list=[]
        for i2 in i:
            temp_list.append(i2)
        if temp_list==temp_str_num2:
            return 'кулл'
    return 'не кулл'


def proverka_prost(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'


for i1 in range(1000,9999):
    if proverka_prost(i1)=='простое':
        for schet in range(2,5000):
            if proverka_prost(i1+schet)=='простое' and check_perestanovka(i1,i1+schet)=='кулл':
                if proverka_prost(i1+2*schet)=='простое'and check_perestanovka(i1,i1+2*schet)=='кулл':
                    print('Числа удовлетворяющие условие 49 задачи:',i1,i1+schet,i1+2*schet,schet)
