def check_pan(n):
    str_num=list(str(n))
    str_num.sort()
    temp_num=''
    for i in str_num:
        if i=='0':
            return 'Не пан-цифровое число'
        elif temp_num!=i:
            temp_num=i
        elif temp_num==i:
            return 'Не пан-цифровое число'
    return 'Пан-цифровое число'


def proizv(num,n):
    n=list(range(1,n+1))
    str_proizv=''
    for i in n:
        str_proizv=str_proizv+str(num*i)
    return str_proizv

str_proizv='12'
max_proizv=0
for i in range(2,10):
    num=1
    print(i)
    while len(str_proizv)<10:
        str_proizv=proizv(num,i)
        if check_pan(int(str_proizv))=='Пан-цифровое число' and max_proizv<int(str_proizv):
            max_proizv=int(str_proizv)
            num=num+1
        else:
            num=num+1
print('Самое большое пан-цифровое число, которое можно получить произведением числа и последовательностью 1<n<10:',max_proizv)
