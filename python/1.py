x=float(0)
i=float(0)
while i<1000:
    if i%3==0 or i%5==0:
        x=i+x
        i=i+1
        print(i)
    else:
        i=i+1
print('Сумма кратных',x)

