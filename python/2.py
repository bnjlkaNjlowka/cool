Num1=1
Num2=1
n=int(input('Введите число:'))
sum=0
while Num2<n:
    if Num2%2==0:
        sum=sum+Num2
    tmp=Num2
    Num2=Num1+Num2
    Num1=tmp
    print(Num2)
print('Сумма четных чисел Фибоначчи не превышающие',n,':',sum)
