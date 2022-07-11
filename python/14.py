def count_i(num):
    i=0
    while num!=1:
        if num%2==0:
            num=int(num/2)
            i=i+1
        else:
            num=(num*3)+1
            i=i+1
    return i+1

n=int(input('Введите число:'))
max_count_i=0
for temp_num in range(1,n):
    #print(count_i(temp_num))
    if max_count_i<count_i(temp_num):
        max_count_i=count_i(temp_num)
print(max_count_i)
