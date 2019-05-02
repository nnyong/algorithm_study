# 어디에 단어가 들어갈 수 있을까
T=int(input())
for test_case in range(1,T+1):
    n,k=map(int, input().split())
    l1=[]
    for i in range(n):
        l1.append(list(map(int,input().split())))
    l2=[]
    for i in range(len(l1)): #0,1,2,3,4
        l=[]
        for j in range(len(l1)): #0,1,2,3,4
            l.append(l1[j][i])
        l2.append(l)

    cnt=0
    for i in l1:
        length=0
        for j in i:
            if j==0:
                if length==k:
                    cnt+=1
                length=0
            else:
                length+=1
        if length==k:
            cnt+=1
    for i in l2:
        length=0
        for j in i:
            if j==0:
                if length==k:
                    cnt+=1
                length=0
            else:
                length+=1
        if length==k:
            cnt+=1
    print(f'#{test_case} {cnt}')

# 2
# 5 3
# 0 0 1 1 1
# 1 1 1 1 0
# 0 0 1 0 0
# 0 1 1 1 1
# 1 1 1 0 1
# 5 3
# 1 0 0 1 0
# 1 1 0 1 1
# 1 0 1 1 1
# 0 1 1 0 1
# 0 1 1 1 0