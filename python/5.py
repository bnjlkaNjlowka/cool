#delt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
inp=int(input('Введите число:'))
delt=[]
for scht in range(0,inp):
    delt.append(scht+1)
#print(delt)
i=0
n=inp
while i!=1:
    #print('n',n)
    for c in range(0,inp):
        if n%delt[c]!=0:
            n=n+inp
            break
        elif n%delt[c]==0 and c==inp-1:
            i=i+1
print('Число которое делится на числа от 1 до',inp,':',n)
