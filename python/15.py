def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans=ans*i
    return ans

n=int(input('Введите число:'))
ans=int((factorial(2*n))/((factorial(n))*(factorial(n))))
print('Количество путей в нижний правый угол для квадрата со стороной',n,':',ans)
