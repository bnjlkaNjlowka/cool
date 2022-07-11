def last_10_num(n):
    str_num=str(n)
    if len(str_num)>=10:
        return str_num[-10:]
    else:
        return str_num[-len(str_num):]

n=int(input('Введите число:'))
ans=0
for i in range(n,0,-1):
    ans=int(last_10_num(ans))+int(last_10_num(i**i))

print('Последние 10 цифр суммы степеней собственных числе до','n:',ans)
