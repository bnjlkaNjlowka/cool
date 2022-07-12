import func

def clear_list(list_num):
    schet=0
    ans=[]
    for i in list_num:
        if i==list_num[0]:
            ans.append(i)
            temp_num=i
        if i!=temp_num:
            temp_num=i
            ans.append(i)
        else:
            continue
    return ans


def check_num(num1,num2):
    str_num1=func.preobr_num(num1)
    str_num2=func.preobr_num(num2)
    str_num1.sort()
    str_num2.sort()
    str_num1=clear_list(str_num1)
    str_num2=clear_list(str_num2)
    schet=-1
    if len(str_num1)!=len(str_num2):
        return 'не тоже самое'
    for i1 in str_num1:
        schet=schet+1
        for i2 in str_num2[schet::]:
            if i1!=i2:
                return 'не тоже самое'
            else:
                break
    return 'тоже самое'


def main():
    i=1
    temp_num=0
    while temp_num==0:
        for i1 in range(2,6):
            num1=i*i1
            num2=i*(i1+1)
            if check_num(num1,num2)=='не тоже самое':
                i=i+1
                break
            elif check_num(num1,num2)=='тоже самое' and i1==5:
                return i


print(main())
