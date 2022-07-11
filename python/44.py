def ugol5_num(n):
    ans=[]
    for i in range(1,n+1):
        num=(3*i**2-i)/2
        ans.append(int(num))
    return ans

n=ugol5_num(10000)
for i1 in range(len(n)):
    for i2 in range(i1,len(n)):
        temp_num=n[i1]+n[i2]
        #print(temp_num)
        temp_n=(1+(1+24*temp_num)**(1/2))/6
        if temp_n==int(temp_n):
            temp_num=abs(n[i2]-n[i1])
            temp_n=(1+(1+24*temp_num)**(1/2))/6
            if temp_n==int(temp_n):
                print('Ответ к задаче 44:',temp_num)
