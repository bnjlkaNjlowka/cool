i1=1
i2=1
i=2
num_str=0
n=int(input('Введите число:'))
while num_str!=n:
    temp_num=i1
    i1=i2
    i2=i2+temp_num
    #print(i2)
    i=i+1
    if len(str(i2))==n:
        num_str=n
print('Порядковый номер числа Фибоначчи, который содержит',n,'цифр:',i)
