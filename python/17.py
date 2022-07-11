def num_v_slovo(num):
    num=str(num)
    num1='0'
    if len(num)==1:
        num=num1+num
    slovo=''
    i=1
    for i in range(len(num),0,-1):
        if i==4:
            if num[-4]=='1':
                slovo=slovo+'тысяча'
        elif i==3:
            if num[-3]=='1':
                slovo=slovo+'сто'
            elif num[-3]=='2':
                slovo=slovo+'двести'
            elif num[-3]=='3':
                slovo=slovo+'триста'
            elif num[-3]=='4':
                slovo=slovo+'четыреста'
            elif num[-3]=='5':
                slovo=slovo+'пятьсот'
            elif num[-3]=='6':
                slovo=slovo+'шестьсот'
            elif num[-3]=='7':
                slovo=slovo+'семьсот'
            elif num[-3]=='8':
                slovo=slovo+'восемьсот'
            elif num[-3]=='9':
                slovo=slovo+'девятьсот'
        elif i==2 and num[-2]!='1':
            if num[-2]=='2':
                slovo=slovo+'двадцать'
            elif num[-2]=='3':
                slovo=slovo+'тридцать'
            elif num[-2]=='4':
                slovo=slovo+'сорок'
            elif num[-2]=='5':
                slovo=slovo+'пятьдесят'
            elif num[-2]=='6':
                slovo=slovo+'шестьдесят'
            elif num[-2]=='7':
                slovo=slovo+'семьдесят'
            elif num[-2]=='8':
                slovo=slovo+'восемьдесят'
            elif num[-2]=='9':
                slovo=slovo+'девяносто'
        elif i==2 and num[-2]=='1':
            if num[-1]=='0':
                slovo=slovo+'десять'
            elif num[-1]=='1':
                slovo=slovo+'одиннадцать'
            elif num[-1]=='2':
                slovo=slovo+'двенадцать'
            elif num[-1]=='3':
                slovo=slovo+'тринадцать'
            elif num[-1]=='4':
                slovo=slovo+'четырнадцать'
            elif num[-1]=='5':
                slovo=slovo+'пятнадцать'
            elif num[-1]=='6':
                slovo=slovo+'шестнадцать'
            elif num[-1]=='7':
                slovo=slovo+'семьнадцать'
            elif num[-1]=='8':
                slovo=slovo+'восемьнадцать'
            elif num[-1]=='9':
                slovo=slovo+'девятнадцать'
        elif i==1 and num[-2]!='1':
            if num[-1]=='1':
                slovo=slovo+'один'
            elif num[-1]=='2':
                slovo=slovo+'два'
            elif num[-1]=='3':
                slovo=slovo+'три'
            elif num[-1]=='4':
                slovo=slovo+'четыре'
            elif num[-1]=='5':
                slovo=slovo+'пять'
            elif num[-1]=='6':
                slovo=slovo+'шесть'
            elif num[-1]=='7':
                slovo=slovo+'семь'
            elif num[-1]=='8':
                slovo=slovo+'восемь'
            elif num[-1]=='9':
                slovo=slovo+'девять'

    return slovo





n=int(input('Введите число:'))
sum_bukv=0
for i in range(1,n+1):
    sum_bukv=sum_bukv+len(num_v_slovo(i))
print('Количество букв необходимых, чтобы записать все числа от 1 до',n,'включительно:',sum_bukv)
