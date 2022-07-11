def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans=ans*i
    return ans

def check_ans(n):
    str_num=str(n)
    ans=0
    for i in str_num:
        ans=ans+factorial(int(i))
    if n==ans:
        return 'кулл'
    else:
        return 'не кулл'


ans=0
for i in range(3,1000000):
    if check_ans(i)=='кулл':
        print(i)
        ans=ans+i
print('Сумма чисел, которые можно предствить как сумму факториалов их цифр:',ans)
