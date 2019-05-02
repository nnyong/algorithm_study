from datetime import datetime
T=int(input())
for test_case in range(1,T+1):
    m1, d1, m2, d2=map(int,input().split())
    date_format='%m/%d'
    date1=datetime.strptime(str(m1)+'/'+str(d1),date_format)
    date2=datetime.strptime(str(m2)+'/'+str(d2),date_format)
    delta=date2-date1
    result=delta.days+1
    print(f'#{test_case} {result}')