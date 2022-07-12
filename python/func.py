def check_prost(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'


def factorial(n):
    summ=1
    for i in range(1,n+1):
        summ=summ*i
    return summ

def preobr_num(num):
    str_num=str(num)
    ans=[]
    for i in str_num:
        ans.append(i)
    return ans

def obr_preobr_num(num):
    ans=''
    for i in num:
        ans=ans+i
    return ans
