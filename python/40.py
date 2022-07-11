def post_num(n):
    str_num=''
    i=1
    while len(str_num)<n:
        str_num=str_num+str(i)
        i=i+1
    return str_num


str_num=list(post_num(1000000))
ans=int(str_num[1-1])*int(str_num[10-1])*int(str_num[100-1])*int(str_num[1000-1])*int(str_num[10000-1])*int(str_num[100000-1])*int(str_num[1000000-1])
print(ans)
