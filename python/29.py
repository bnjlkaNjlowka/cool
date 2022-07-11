import itertools
n=int(input('Введите число:'))
a=list(range(2,n+1))
nums=list(itertools.product(a,repeat=2))

list_num=[0]
schet=0
temp_list=[]
for i in nums:
    num=i[0]**i[1]
    temp_list.append(num)

temp_list.sort()
for i in range(len(temp_list)):
    if temp_list[i]!=list_num[schet]:
        list_num.append(temp_list[i])
        schet=schet+1
list_num.remove(0)
#print(list_num)
print('Количество уникальных комбинаций для задачи 29:',len(list_num))
