def numbers(num,delt,n=10):
    str_num='0.'
    for i in range(n):
        ans=(num*10)//delt
        num=(num*10)%delt
        str_num=str_num+str(ans)
    return str_num

#print(numbers(1,97,200))
n=int(input('Введите число:'))
temp_str=' '
max_num=0
temp_i1=0
for i in range(1,n):
    num_str=numbers(1,i,2000)
    temp_str=' '
    temp_i1=0
    for schet in range(1,len(num_str)-1):
        #print('schet',num_str[-schet])
        #print('adfgd',temp_str[0])
        if num_str[-schet]!=temp_str[0]:
            if schet==1:
                temp_str=num_str[-schet]
                continue
            temp_str=temp_str+num_str[-schet]
        elif num_str[-schet]==temp_str[0]:
            for i1 in range(0,len(temp_str)):
                #print('schet',schet)
                #print('123',temp_str)
                #print('as',i1)
                #print('aye',len(temp_str))
                #print('1',num_str[schet+i1])
                #print('2',temp_str[i1])
                if num_str[-schet-i1]!=temp_str[i1]:
                    temp_str=temp_str+num_str[-schet]
                    break
                elif num_str[-schet-i1]==temp_str[i1] and i1==((len(temp_str)))-1:
                    if max_num<len(temp_str):
                        max_num=len(temp_str)
                        #print('adfadf')
                        temp_i1=1
                        temp_i=i
                        aye=temp_str[::-1]
        if temp_i1==1:
            break
print('Число, у которого самое большое количество цифр в периоде, при делении им 1 до',n,':',temp_i)
