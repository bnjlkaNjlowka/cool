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

