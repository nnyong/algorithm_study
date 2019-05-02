num=1
for i in range(T):
    w=list(map(int,input().split()))
    P=w[0]
    Q=w[1]
    R=w[2]
    S=w[3]
    W=w[4]    

    a_bill=P*W
    if W<=R:
        b_bill=Q
    else:
        b_bill=Q+(W-R)*S

    if a_bill<=b_bill:
        print(f'#{num} {a_bill}')
    else:
        print(f'#{num} {b_bill}')
    num+=1