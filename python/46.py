def check_prost(n):
    if n==1:
        return 'простое'
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'



list_Pdelt=[]
for i in range(2,10**6):
    if check_prost(i)=='простое':
        list_Pdelt.append(i)






def check_ans(n):
    for i1 in list_Pdelt:
        i2=1
        ans=1
        while ans<n:
            ans=i1+2*i2**2
            i2=i2+1
            if ans==n:
                return 'кулл'
    return 'не кулл'


ans=0
i=35
while ans==0:
    print(i)
    if check_prost(i)=='простое':
        i=i+2
        continue
    elif check_ans(i)=='не кулл':
        print('sd',i)
        ans=ans+1
    i=i+2
