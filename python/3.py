n=int(input('Введите число:'))
delt=2
ans=n
while delt<ans:
    if ans%delt!=0:
        delt=delt+1
        continue
    ans=ans/delt
print(delt)
