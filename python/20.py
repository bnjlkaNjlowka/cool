def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans=ans*i
    return ans

n=int(input('Введите число:'))
num=str(factorial(n))
summ_num=0
for i in range(len(num)):
    summ_num=summ_num+int(num[i])
print('Сумма цифр факториала',n,':',summ_num)
