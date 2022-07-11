def check_prost(n):
    for i in range(2,int((n)**(1/2))+1):
        if n%i==0:
            return 'не простое'
    return 'простое'


def list_prost(n):
    prost_list=[]
    for i in range(2,n):
        if check_prost(i)=='простое':
            prost_list.append(i)
    return prost_list


def sum_prost(n):
    prost_list=list_prost(n)
    max_num=0
    for i in range(len(prost_list)):
        temp_num=0
        schet=0
        #print(i)
        for i2 in prost_list[i::]:
            #print(prost_list[i::])
            temp_num=temp_num+i2
            schet=schet+1
            if temp_num<n:
                proverka=check_prost(temp_num)
                if proverka=='простое':
                    if schet>max_num:
                        max_num=schet
                        temp_prost=temp_num
            else:
                break
    print('Максимальное кол-во последовательных простых чисел:',max_num,', Простое число, которое можно записать суммой тех простых чисел:',temp_prost)


num=int(input('Введите число:'))

sum_prost(num)
