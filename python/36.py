def check_palindrom(n):
    str_num=str(n)
    for i in range(len(str_num)//2):
        if str_num[i]!=str_num[-1-i]:
            return 'не палиндром'
    return 'палиндром'


def iz_10_v_2(n):
    str_num=''
    while n!=1:
        str_num=str_num+str(n%2)
        n=n//2
    str_num=str_num+str(n%2)
    str_num=str_num[::-1]
    return int(str_num)


n=int(input('Введите число:'))
ans=0
for i in range(1,n):
    if check_palindrom(i)=='палиндром' and check_palindrom(iz_10_v_2(i))=='палиндром':
        print('i',i)
        print('2',iz_10_v_2(i))
        ans=ans+i
print('Сумма чисел, которые являются палиндромами по оснаванию 10 и 2, и меньше',n,':',ans)
