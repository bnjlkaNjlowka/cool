print('Введите числа:')
num=[]
inp=0
sum=[]
for schet in range(52):
    sum.append(0)
while inp!='':
    inp=input()
    num.append(inp)
num.remove('')
#print('as',len(num))
for i in range(1,51):
    for temp_num in num:
        sum[i-1]=sum[i-1]+int(temp_num[-i])
    print('asd',i,sum[i-1])
    if sum[i-1]>=10:
        sum[i]=sum[i]+sum[i-1]//10
        sum[i-1]=sum[i-1]%10
        if sum[i]>=10:
            sum[i+1]=sum[i+1]+(sum[i]//10)
            sum[i]=sum[i]%10
sum.reverse()
print('Последние 10 чисел суммы введенных чисел',sum[0:10])
