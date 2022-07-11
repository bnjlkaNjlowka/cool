def provernut_num(n):
    str_num=list(str(n))
    temp_liststr1=str_num
    temp_liststr2=liststr_iz_0(len(str_num))
    for i2 in range(len(str_num)):
        if i2!=len(str_num)-1:
            temp_liststr2[i2+1]=temp_liststr1[i2]
        elif i2==len(str_num)-1:
            temp_liststr2[0]=temp_liststr1[i2]
    return iz_liststr_v_int(temp_liststr2)


def liststr_iz_0(n):
    temp_str=list('')
    for i in range(n):
        temp_str.append('0')
    return temp_str

def iz_liststr_v_int(list_str):
    temp_str=''
    for i in list_str:
        temp_str=temp_str+i
    return int(temp_str)


def proverka_prostogo(n):
    for i in range(2,int((n)**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'


def proverka_krug_prost(n):
    if proverka_prostogo(n)=='не простое':
        return 'вообще не простое'
    for i1 in range(len(str(n))-1):
        n=provernut_num(n)
        if proverka_prostogo(n)=='не простое':
            return 'не круговое'
    return 'круговое'



n=int(input('Введите число:'))
schet=1
for i in range(3,n,2):
    if proverka_krug_prost(i)=='круговое':
        #print(i)
        schet=schet+1

print('Количество простых круговых чисел меньше',n,':',schet)
