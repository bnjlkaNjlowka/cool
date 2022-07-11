def check_ans():
    ans=[]
    list_delt=[2,3,5,7,11,13,17]
    for i1 in range(17,1000,17):
        temp_str=str(i1)
        if len(temp_str)==2:
            temp_str=temp_str[::-1]
            temp_str=temp_str+'0'
            temp_str=temp_str[::-1]
        for i2 in range(10):
            temp_str2=temp_str[0:2]
            temp_str2=temp_str2[::-1]
            temp_str2=temp_str2+str(i2)
            temp_str2=temp_str2[::-1]
            if len(temp_str2)==2:
                temp_str2=temp_str2[::-1]
                temp_str2=temp_str2+'0'
                temp_str2=temp_str2[::-1]
            if int(temp_str2)%13==0:
                for i3 in range(10):
                    temp_str3=temp_str2[0:2]
                    temp_str3=temp_str3[::-1]
                    temp_str3=temp_str3+str(i3)
                    temp_str3=temp_str3[::-1]
                    if len(temp_str3)==2:
                        temp_str3=temp_str3[::-1]
                        temp_str3=temp_str3+'0'
                        temp_str3=temp_str3[::-1]
                    if int(temp_str3)%11==0:
                        for i4 in range(10):
                            temp_str4=temp_str3[0:2]
                            temp_str4=temp_str4[::-1]
                            temp_str4=temp_str4+str(i4)
                            temp_str4=temp_str4[::-1]
                            if len(temp_str4)==2:
                                temp_str4=temp_str4[::-1]
                                temp_str4=temp_str4+'0'
                                temp_str4=temp_str4[::-1]
                            if int(temp_str4)%7==0:
                                for i5 in range(10):
                                    temp_str5=temp_str4[0:2]
                                    temp_str5=temp_str5[::-1]
                                    temp_str5=temp_str5+str(i5)
                                    temp_str5=temp_str5[::-1]
                                    if len(temp_str5)==2:
                                        temp_str5=temp_str5[::-1]
                                        temp_str5=temp_str5+'0'
                                        temp_str5=temp_str5[::-1]
                                    if int(temp_str5)%5==0:
                                        for i6 in range(10):
                                            temp_str6=temp_str5[0:2]
                                            temp_str6=temp_str6[::-1]
                                            temp_str6=temp_str6+str(i6)
                                            temp_str6=temp_str6[::-1]
                                            if len(temp_str6)==2:
                                                temp_str6=temp_str6[::-1]
                                                temp_str6=temp_str6+'0'
                                                temp_str6=temp_str6[::-1]
                                            if int(temp_str6)%3==0:
                                                for i7 in range(10):
                                                    temp_str7=temp_str6[0:2]
                                                    temp_str7=temp_str7[::-1]
                                                    temp_str7=temp_str7+str(i7)
                                                    temp_str7=temp_str7[::-1]
                                                    if len(temp_str7)==2:
                                                        temp_str7=temp_str7[::-1]
                                                        temp_str7=temp_str7+'0'
                                                        temp_str7=temp_str7[::-1]
                                                    if int(temp_str7)%2==0:
                                                        temp_num=temp_str7+temp_str6[2]+temp_str5[2]+temp_str4[2]+temp_str3[2]+temp_str2[2]+temp_str[2]
                                                        ans.append(temp_num)
                                                        #print(temp_num)
    return ans


def check_pan(n):
    str_num=str(n)
    str_num=list(str_num)
    str_num.sort()
    temp_num=0
    for i in str_num:
        if i==str(temp_num):
            temp_num=temp_num+1
        else:
            return 'Не пан-цифровое число'
    return 'Пан-цифровое число'


def preobr_list(n):
    ans=[]
    for i in n:
        for schet in range(1,10):
            temp_num=i[::-1]
            temp_num=temp_num+str(schet)
            temp_num=temp_num[::-1]
            ans.append(int(temp_num))
            #print(temp_num)
    return ans



list_ans=check_ans()
list_ans=preobr_list(list_ans)
summ=0
for i in list_ans:
    if check_pan(i)=='Пан-цифровое число':
        summ=summ+i
        #print(i)
print('Ответ к задаче 43:',summ)
