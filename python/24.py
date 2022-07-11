import itertools
n=int(input('Введите число:'))
nums='0123456789'
list_ans=list(itertools.permutations(nums))
temp_str=''
for i in list_ans[n-1]:
    temp_str=temp_str+i
print(temp_str)
