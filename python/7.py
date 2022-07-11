n=int(input('Введите число:'))
prostie=[2,3]
i=1
num=3
while i!=n-1:
    #print('ii',i)
    for scht in range(0,i+1):
        if num%prostie[scht]==0:
            #print(num)
            num=num+2
            break
        elif num%prostie[scht]!=0 and scht==i:
            #print('p')
            prostie.append(num)
            num=num+2
            i=i+1
            #print('i',i)
print(n,'- ое простое число:',prostie[n-1])
