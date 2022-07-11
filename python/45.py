def check_ans(n):
    num1=(1+(1+24*n)**(1/2))/6
    if num1==int(num1):
        num2=(1+(1+8*n)**(1/2))/4
        if num2==int(num2):
            return 'и пятиугольное, и шестиугольное'
    return 'нет'


ans=0
n=286
while ans==0:
    x=(n**2+n)/2
    if check_ans(x)=='и пятиугольное, и шестиугольное':
        ans=x
        print('2-ое треугольное и пятиугольное, и шестиугольное число:',ans)
    else:
        n=n+1
