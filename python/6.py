n=int(input('Введите число:'))
sum=0
sum_square=0
for num in range(1,n+1):
    sum=sum+num
square_sum=sum*sum
for num in range(1,n+1):
    sum_square=sum_square+(num*num)
print('Разница',square_sum-sum_square)
