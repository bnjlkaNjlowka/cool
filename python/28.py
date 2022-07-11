n=int(input('Сторона квадрата:'))
num=1
summ=0
for i in range(2,n+1):
    if i%2==0:
        summ1=(i**2)+1
        summ2=(i**2)-num
        summ=summ+summ1+summ2
        num=num+2
    if i%2==1:
        summ1=(i**2-i)+1
        summ2=i**2
        summ=summ+summ1+summ2
print('Сумма цифр на диагоналях числовой спирали со стороной',n,':',summ+1)
