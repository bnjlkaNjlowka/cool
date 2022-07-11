n=int(input('Введите число:'))
num=list(range(2,n))
i=0
prostie=0
temp_list=[]
p=2
while num[0]<n**(1/2):
    p=num[0]
    prostie=prostie+p
    temp_list=[]
    print('p',p)
    for temp_num in num:
        if temp_num%p!=0:
            temp_list.append(temp_num)
    num=temp_list
print(prostie+sum(temp_list))
