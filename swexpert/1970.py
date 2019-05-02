T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    money={50000:0,10000:0,5000:0,1000:0,500:0,100:0,50:0,10:0}
    
    for key in money.keys():
        quo=n//key
        money[key]=quo
        n=n%key
    print(f'#{test_case}')
    for value in money.values():
        print(value,end=" ")
    print()