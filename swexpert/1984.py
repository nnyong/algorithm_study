# 중간 평균값 구하기
T=int(input())
for test_case in range(1,T+1):
    l=list(map(int,input().split()))
    l.sort()
    l.remove(l[0])
    l.remove(l[len(l)-1])
    sum=0
    for i in l:
        sum+=i
    mean=int(round(sum/len(l),0))
    # mean=int(round(np.mean(l),0))
    print(f'#{test_case} {mean}')