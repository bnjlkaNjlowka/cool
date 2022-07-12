import func

def zamena_chisel(num,list_num):
    list_chisel=[]
    str_num=func.preobr_num(num)
    for i in range(0,10):
        for i2 in list_num:
            str_num[i2]=str(i)
        temp_num=func.obr_preobr_num(str_num)
        list_chisel.append(int(temp_num))
    return list_chisel


def check_3_chisel(num):
    str_num=str(num)
    ans=[]
    schet1=0
    for i1 in str_num:
        schet1=schet1+1
        schet2=schet1
        for i2 in str_num[schet1::]:
            schet2=schet2+1
            if i2==i1:
                schet3=schet2
                for i3 in str_num[schet2::]:
                    schet3=schet3+1
                    if i3==i2:
                        temp_ans=[]
                        temp_ans.append(schet1-1)
                        temp_ans.append(schet2-1)
                        temp_ans.append(schet3-1)
                        ans.append(temp_ans)
    return ans



def list_prost(num):
    ans=[]
    for i in range(2,num):
        if func.check_prost(i)=='простое':
            ans.append(i)
    return ans



def check_spisok(list_num):
    schet=0
    for i in list_num:
        if func.check_prost(i)=='простое':
            if len(str(i))==len(str(list_num[1])):
                schet=schet+1
    return schet




def min_prost_in_list(list_num):
    for i in list_num:
        if func.check_prost(i)=='простое':
            return i

prostie=list_prost(10**6)




def main():
    for i in prostie:
        if i<1000:
            continue
        temp_list=check_3_chisel(i)
        if temp_list!=[]:
            for i2 in temp_list:
                list_for_check=zamena_chisel(i,i2)
                if check_spisok(list_for_check)==8:
                    return list_for_check


print('Наименьшее простое число, которое обладает необходимым свойством:',min_prost_in_list(main()))
