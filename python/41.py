def check_pan(n):
    str_num=list(str(n))
    str_num.sort()
    if str_num[0]!='1':
        return 'Не пан-цифровое число'
    temp_num=str(1)
    for i in str_num:
        if i=='0':
            return 'Не пан-цифровое число'
        elif temp_num==i:
            temp_num=str(int(temp_num)+1)
        elif temp_num!=i:
            return 'Не пан-цифровое число'
    return 'Пан-цифровое число'

def proverka_prostogo(n):
    for i in range(2,int((n)**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'



list_pan=[]
for i in range(11,1000000000,2):
    if check_pan(i)=='Пан-цифровое число':
        print(i)
        list_pan.append(i)


for i in list_pan[::-1]:
    if proverka_prostogo(i)=='простое':
        print('Ответ',i)
        break
