def proverka_prostogo(n):
    if n==1:
        return 'не простое'
    for i in range(2,int((n)**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'


def ukototit_left(n):
    str_num=str(n)
    if str_num[1]=='0':
        return 0
    return int(str_num[1:])


def ukototit_right(n):
    str_num=str(n)
    if str_num[1]=='0':
        return 0
    return int(str_num[:len(str_num)-1])


def check_ans(n):
    num=n
    if proverka_prostogo(num)=='простое':
        for i in range(len(str(n))-1):
            num=ukototit_left(num)
            if num==0 or proverka_prostogo(num)=='не простое':
                return 0
            elif i==len(str(n))-2 and proverka_prostogo(num)=='простое':
                num=n
                for i in range(len(str(n))-1):
                    num=ukototit_right(num)
                    if num==0 or proverka_prostogo(num)=='не простое':
                        return 0
                    elif i==len(str(n))-2 and proverka_prostogo(num)=='простое':
                        #print(n)
                        return n
    else:
        return 0


ans=0
sum=0
i=10
while ans!=11:
    if check_ans(i)==i:
        ans=ans+1
        sum=sum+i
        i=i+1
    else:
        i=i+1
print('Сумма всех простых укорачиваемых чисел:',sum)
