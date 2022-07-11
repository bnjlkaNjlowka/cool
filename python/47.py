def Pdelt_num(n):
    Pdelt=[]
    ans=n
    i=2
    while ans!=1:
        if ans%i!=0:
            i=i+1
            continue
        ans=ans/i
        Pdelt.append(i)
    return Pdelt


def preobr_list(n):
    ans=[]
    n.sort()
    temp_num=n[0]
    temp_sum=1
    schet=0
    for i in n:
        if temp_num==i and schet!=len(n)-1:
            temp_sum=temp_sum*i
            schet=schet+1
        elif schet==len(n)-1 and temp_num==i:
            temp_sum=temp_sum*i
            ans.append(temp_sum)
            schet=schet+1
        elif schet==len(n)-1 and temp_num!=i:
            ans.append(temp_sum)
            ans.append(i)
        elif temp_num!=i:
            temp_num=i
            ans.append(temp_sum)
            temp_sum=i
            schet=schet+1
    return ans


def sravnenie_list(n1,n2,n3,n4):
    #if len(n1)!=len(n2) or len(n1)!=len(n3) or len(n1)!=len(n4):
    #    return 'не подходит'
    for i1 in n1:
        for i2 in n2:
            if i1==i2:
                return 'не подходит'
            else:
                for i3 in n3:
                    if i2==i3:
                        return 'не подходит'
                    else:
                        for i4 in n4:
                            if i3==i4:
                                return 'не подходит'
    return 'подходит'

#print(sravnenie_list([2,3,4,5],[6,7,8,9],[10,11,12,13],[14,15,16,17]))
ans=0
num=10
while ans==0:
    print(num)
    list1=preobr_list(Pdelt_num(num))
    #print(list1)
    if len(list1)!=4:
        num=num+1
        continue
    list2=preobr_list(Pdelt_num(num+1))
    print('1',list1)
    if len(list2)!=4:
        num=num+2
        continue
    list3=preobr_list(Pdelt_num(num+2))
    print('2',list2)
    if len(list3)!=4:
        num=num+3
        continue
    list4=preobr_list(Pdelt_num(num+3))
    print('3',list3)
    if len(list4)!=4:
        num=num+4
        continue
    if sravnenie_list(list1,list2,list3,list4)=='подходит':
        ans=ans+1
        print('asd',num)
    else:
        num=num+1
        print('cd')

print(list1,list2,list3,list4)
