def sokr_drob(n1,n2):
    temp_str_n1=str(n1)
    temp_str_n2=str(n2)
    str_n1=list(temp_str_n1)
    str_n2=list(temp_str_n2)
    temp_str1=str_n1
    temp_str2=str_n2
    for i1 in str_n1:
        for i2 in str_n2:
            #print('1',str_n1,i1)
            #print('2',str_n2,i2)
            if i1==i2 and (i1!='0' and i2!='0'):
                str_n1.remove(i1)
                str_n2.remove(i2)
                break
    temp_list=[str_n1,str_n2]
    nums=[]
    for i in temp_list:
        temp_str=''
        for schet in i:
            temp_str=temp_str+schet
        nums.append(int(temp_str))
    #print(nums)
    return nums


def Pdelt_num(n):
    list_Pdelt=[1]
    delt=2
    i=0
    ans=n
    while ans!=1:
        if ans%delt!=0:
            delt=delt+1
            continue
        else:
            list_Pdelt.append(delt)
            ans=ans/delt
            i=i+1
    #list_Pdelt.remove(1)
    return list_Pdelt



def check_ans(n1,n2):
    temp_nums=sokr_drob(n1,n2)
    #print(temp_nums)
    nums=[]
    Nums=[]
    if (temp_nums[0]==0 or temp_nums[1]==0) or (temp_nums[0]==n1):
        return 0
    Nums1=Pdelt_num(n1)
    Nums2=Pdelt_num(n2)
    #print(Pdelt_num(n1))
    #print(Pdelt_num(n2))
    num1=Pdelt_num(temp_nums[0])
    num2=Pdelt_num(temp_nums[1])
    #print('a',Pdelt_num(temp_nums[1]))
    nums.append(num1)
    nums.append(num2)
    Nums.append(Nums1)
    Nums.append(Nums2)
    #print(nums[1][1:])
    for i1 in nums[0][1:]:
        for i2 in nums[1][1:]:
            if i1==i2:
                nums[0].remove(i1)
                nums[1].remove(i2)
                break
    for i1 in Nums[0][1:]:
        for i2 in Nums[1][1:]:
            if i1==i2:
                Nums[0].remove(i1)
                Nums[1].remove(i2)
                break
    rnum1=1
    rnum2=1
    for i1 in nums[0]:
        rnum1=i1*rnum1
    for i2 in nums[1]:
        rnum2=i2*rnum2
    rNum1=1
    rNum2=1
    for i1 in Nums[0]:
        rNum1=i1*rNum1
    for i2 in Nums[1]:
        rNum2=i2*rNum2
    rnums=[]
    rnums.append(rnum1)
    rnums.append(rnum2)
    rNums=[]
    rNums.append(rNum1)
    rNums.append(rNum2)
    #print(rnums)
    #print(rNums)
    if (temp_nums[0]/temp_nums[1])<1 and (rNum1==rnum1 and rNum2==rnum2):
        #print(rnums)
        #print(rNums)
        #print('n',n1,n2)
        return 1
    #print(rnums)
    return 0\

def sokr_drob1(n1,n2):
    num1=[]
    num1.append(Pdelt_num(n1))
    num1.append(Pdelt_num(n2))
    for i1 in num1[0][1:]:
        for i2 in num1[1][1:]:
            if i1==i2:
                num1[0].remove(i1)
                num1[1].remove(i2)
                break
    rnum1=1
    rnum2=1
    for i1 in num1[0]:
        rnum1=rnum1*i1
    for i2 in num1[1]:
        rnum2=rnum2*i2
    rnum=[]
    rnum.append(rnum1)
    rnum.append(rnum2)
    return rnum

#print(sokr_drob1(49,98))
i2=11
ans1=1
ans2=1
while i2!=100:
    for i1 in range(10,i2):
        if check_ans(i1,i2)==1:
            #print(i1,i2)
            ans1=ans1*i1
            ans2=ans2*i2
    i2=i2+1
print('Ответ к задаче 33:',sokr_drob1(ans1,ans2)[1])
