def summ_num_of_letters(slovo):
    summ=0
    for temp_letter in slovo:
        if temp_letter=='A':
            summ=summ+1
        elif temp_letter=='B':
            summ=summ+2
        elif temp_letter=='C':
            summ=summ+3
        elif temp_letter=='D':
            summ=summ+4
        elif temp_letter=='E':
            summ=summ+5
        elif temp_letter=='F':
            summ=summ+6
        elif temp_letter=='G':
            summ=summ+7
        elif temp_letter=='H':
            summ=summ+8
        elif temp_letter=='I':
            summ=summ+9
        elif temp_letter=='J':
            summ=summ+10
        elif temp_letter=='K':
            summ=summ+11
        elif temp_letter=='L':
            summ=summ+12
        elif temp_letter=='M':
            summ=summ+13
        elif temp_letter=='N':
            summ=summ+14
        elif temp_letter=='O':
            summ=summ+15
        elif temp_letter=='P':
            summ=summ+16
        elif temp_letter=='Q':
            summ=summ+17
        elif temp_letter=='R':
            summ=summ+18
        elif temp_letter=='S':
            summ=summ+19
        elif temp_letter=='T':
            summ=summ+20
        elif temp_letter=='U':
            summ=summ+21
        elif temp_letter=='V':
            summ=summ+22
        elif temp_letter=='W':
            summ=summ+23
        elif temp_letter=='X':
            summ=summ+24
        elif temp_letter=='Y':
            summ=summ+25
        elif temp_letter=='Z':
            summ=summ+26
    return summ



with open('p022_names.txt') as temp_thing:
    names=temp_thing.read()
list_names=[]
i=0
while i<=len(names)-1:
    if names[i]=='"':
        temp_str=''
        while names[i+1]!='"':
            temp_str=temp_str+names[i+1]
            i=i+1
        list_names.append(temp_str)
        i=i+2
    i=i+1
list_names.sort()

score=0
for i in range(len(list_names)):
    score=(i+1)*summ_num_of_letters(list_names[i])+score
print('Сумма "очков" спика:',score)
