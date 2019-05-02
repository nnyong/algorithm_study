T=int(input())
for i in range(T):
    num=int(input())
    x=list(map(int, input().split()))

    dic={}
    for i in x:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    max_value=list(dic.values())[0]
    for key, value in dic.items():
        if value>=max_value:
            max_key=key
            max_value=value
    print(f'#{num} {max_key}')