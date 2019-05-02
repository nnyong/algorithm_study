T=int(input())
rep=[]
for i in range(T):
    rep.append(int(input()))
num=1
for i in rep:
    x=i
    l=[]
    for i in range(x):
            l.append([0]*x)

    n=0
    row=0
    col=-1
    s=1
    k=x
    while True:
        for i in range(k):
            n+=1
            col+=s
            l[row][col]=n
        k-=1
        if k==0:
            break
        for i in range(k):
            n+=1
            row+=s
            l[row][col]=n
        s=-s    

    print(f'#{num}')
    num+=1
    for i in l:
        for j in i:
            print(j,end=" ")
        print()