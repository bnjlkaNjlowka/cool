def check_pal(n):
    #n=input('Введите число:')
    str_n=str(n)
    i=0
    #print(len(str_n))
    while i<len(str_n):
        if len(str_n)%2!=0:
            #print('нечетное число цифр')
            return 'нечетное число цифр'
            break
        elif str_n[i]!=str_n[-1-i]:
            #print('не палиндром')
            return 'не палиндром'
            break
        elif str_n[i]==str_n[-1-i] and i==len(str_n)-1:
            #print('палиндром')
            return 'палиндром'
        i=i+1

rem_num=0
for temp_num in range(999,99,-1):
    for temp_num2 in range(999,99,-1):
        if check_pal(temp_num*temp_num2)=='палиндром' and rem_num<temp_num*temp_num2:
            rem_num=temp_num*temp_num2
            break
print(rem_num)

#check_pal(1221)
