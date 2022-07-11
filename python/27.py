def prime_num(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return 'составное'
    return 'простое'


def ure(n,a,b):
    num=n**2+a*n+b
    return num

num=int(input('Коэффициенты не превышают по модулю:'))
P_list=[]
for i in range(2,num):
    if prime_num(i)=='простое':
        P_list.append(i)

n_max=0
for a in range(-num,num):
    for b in P_list:
        n=0
        if ure(n,a,b)<0:
            continue
        while prime_num(ure(n,a,b))=='простое':
            n=n+1
            if ure(n,a,b)<0:
                break
        if n_max<n:
            n_max=n
            a_max=a
            b_max=b
print('Произведение коэффициентов a и b квадратичного уравнения, при которых можно получить максимальное значение простых чисел:',a_max*b_max)
