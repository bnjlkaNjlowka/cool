def ans(num,n):
    num_str=str(num)
    num_list=[]
    summ_num=0
    for i in num_str:
        num_list.append(int(i))
    for i in num_list:
        summ_num=summ_num+(i**n)
    return summ_num

i=1
n=5
num=1
summ_ans=0
while i<=len(str(num)):
    num=i*(9**n)
    i=i+1

for schet in range(10,num):
    if schet==ans(schet,n):
        summ_ans=summ_ans+schet
print(summ_ans)
