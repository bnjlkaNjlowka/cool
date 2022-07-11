import func


def summirovanie_fact(n):
    summ=0
    for i in range(1,n):
        summ=summ+(func.factorial(n)/func.factorial(i))
    return int(summ)



def zamena(num):
    temp_list=[]
    str_num=str(num)
    summ_var=summirovanie_fact(len(str_num))
    return summ_var


def list_prost(n):
    list_prosst=[]
    for i in range(2,n+1):
        if func.check_prost(i)=='простое':
            list_prosst.append(i)
    return list_prosst


def proverka(n1,n2):
    



print(list_prost(100))
