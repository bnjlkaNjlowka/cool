def count_sum(n):
    schet=0
    for i2 in range(int(n/2),-1,-1):
        sum=2*i2
        sum2=sum
        if sum==n:
            schet=schet+1
            continue
        #print('2',sum)
        for i5 in range(int((n-sum2)/5),-1,-1):
            sum5=sum+5*i5
            #print('5',sum)
            if sum5==n:
                schet=schet+1
                continue
            for i10 in range(int((n-sum5)/10),-1,-1):
                sum10=sum5+10*i10
                if sum10==n:
                    schet=schet+1
                    continue
                for i20 in range(int((n-sum10)/20),-1,-1):
                    sum20=sum10+20*i20
                    if sum20==n:
                        schet=schet+1
                        continue
                    for i50 in range(int((n-sum20)/50),-1,-1):
                        sum50=sum20+50*i50
                        if sum50==n:
                            schet=schet+1
                            continue
                        for i100 in range(int((n-sum50)/100),-1,-1):
                            sum100=sum50+100*i100
                            if sum100==n:
                                schet=schet+1
                                continue
                            for i200 in range(int(n/200),-1,-1):
                                sum200=sum100+200*i200
                                if sum200==n:
                                    schet=schet+1
                                    continue

    return schet

schet=0
n=int(input('Введите число:'))
for i in range(n,-1,-1):
    temp_num=n-i
    #print(i)
    schet=schet+count_sum(temp_num)

print('Количество способов, которыми можно получить',n,'из набора данных монет:',schet)
