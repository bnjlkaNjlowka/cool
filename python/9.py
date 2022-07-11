i=int(input('Введите число:'))
for m in range(2,i):
    #print('m',m)
    for n in range(1,m):
        if 2*(m**2)+2*m*n==i:
            #print('n',n)
            break
    if 2*(m**2)+2*m*n==i:
        break
    elif 2*(m**2)+2*m*n!=i and m==i-1:
        print('gg')
        exit()
a=m**2-n**2
b=2*m*n
c=m**2+n**2
print('a =',a,'b =',b,'c =',c)
print('Произведение abc',a*b*c)
