def summ_num(num):
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum=sum+int(num[i])
    return sum

n=int(input('Степень двойки:'))
ans=summ_num(2**n)
print('Сумма цифр 2 в степени',n,':',ans)
