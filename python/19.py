months=[31,28,31,30,31,30,31,31,30,31,30,31]
months_1=[31,29,31,30,31,30,31,31,30,31,30,31]
n=int(input('Введите год:'))
year=1901
summ_days=366
ans=0
while year!=n+1:
    for num_month in range(12):
        if year%4==0 and year%400!=0:
            summ_days=summ_days+months_1[num_month]
        elif year%4!=0:
            summ_days=summ_days+months[num_month]
        elif year%400==0:
            summ_days=summ_days+months_1[num_month]
        if summ_days%7==0:
            ans=ans+1
    year=year+1
print('Количество воскресений попадающие на первое число месяца с 1901 до',n,'годов:',ans)
