def ans_for_p(p):
    ans=[]
    for a in range(1,1000):
        for b in range(a,1000):
            c2=a**2+b**2
            if a+b+c2**(1/2)>p:
                break
            if c2**(1/2)==int(c2**(1/2)):
                if a+b+c2**(1/2)==p:
                    ans.append([a,b,c2**(1/2)])
            else:
                continue
    return len(ans)


n=int(input('Введите число:'))
max=0
ans=0
for i in range(1,n):
    temp_num=ans_for_p(i)
    if max<temp_num:
        max=temp_num
        ans=i
print('Максимальное число для данного периметра прямоугольного треугольника при периметре<',n,':',ans)
