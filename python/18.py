treug=[]
inp=[]
while inp!='':
    inp=input()
    treug.append(inp)
    #print(treug)
treug.remove('')
#i=1
#treug[i]=int(treug[i])
#print('iugiyg',(treug[1][2])==' ')
for i in range(len(treug)):
    temp_str=str('')
    temp_list=[]
    for schet in range(len(treug[i])):
        if treug[i][schet]!=' ' and schet!=(len(treug[i]))-1:
            temp_str=temp_str+treug[i][schet]
        elif treug[i][schet]==' ':
            temp_list.append(int(temp_str))
            temp_str=str('')
        elif schet==(len(treug[i]))-1:
            temp_str=temp_str+treug[i][schet]
            temp_list.append(int(temp_str))

    treug[i]=temp_list
print(treug)
summ_list=[]
summ=0
for i in range(0,1):
    summ=summ+treug[0][i]
    for i2 in range(0,2):
        summ2=summ+treug[1][i+i2]
        for i3 in range(2):
            summ3=summ+summ2+treug[2][i+i2+i3]
            for i4 in range(2):
                summ4=summ+summ2+summ3+treug[3][i+i2+i3+i4]
                for i5 in range(2):
                    summ5=summ+summ2+summ3+summ4+treug[4][i+i2+i3+i4+i5]
                    for i6 in range(2):
                        summ6=summ+summ2+summ3+summ4+summ5+treug[5][i+i2+i3+i4+i5+i6]
                        for i7 in range(2):
                            summ7=summ+summ2+summ3+summ4+summ5+summ6+treug[6][i+i2+i3+i4+i5+i6+i7]
                            for i8 in range(2):
                                summ8=summ+summ2+summ3+summ4+summ5+summ6+summ7+treug[7][i+i2+i3+i4+i5+i6+i7+i8]
                                for i9 in range(2):
                                    summ9=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+treug[8][i+i2+i3+i4+i5+i6+i7+i8+i9]
                                    for i10 in range(2):
                                        summ10=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+treug[9][i+i2+i3+i4+i5+i6+i7+i8+i9+i10]
                                        for i11 in range(2):
                                            summ11=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+summ10+treug[10][i+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11]
                                            for i12 in range(2):
                                                summ12=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+summ10+summ11+treug[11][i+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12]
                                                for i13 in range(2):
                                                    summ13=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+summ10+summ11+summ12+treug[12][i+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13]
                                                    for i14 in range(2):
                                                        summ14=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+summ10+summ11+summ12+summ13+treug[13][i+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14]
                                                        for i15 in range(2):
                                                            summ15=summ+summ2+summ3+summ4+summ5+summ6+summ7+summ8+summ9+summ10+summ11+summ12+summ13+summ14+treug[14][i+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15]
                                                            summ_list.append(summ15)
print(max(summ_list))
print(len(summ_list))
