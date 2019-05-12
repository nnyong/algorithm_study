import sys
sys.stdin=open('줄기세포.txt','r')

dy=[-1,0,1,0]
dx=[0,1,0,-1]

def isSafe(y,x):
    if y<(n+k) and y>=0 and x<(m+k) and x>=0:
        return True
    else:
        return False

def activate(y,x):
    global time
    for dir in range(4):
        new_y=y+dy[dir]
        new_x=x+dx[dir]
        if isSafe(new_y,new_x):
            if cell[new_y][new_x]==0:
                cell[new_y][new_x]=cell[y][x]
            elif cell[new_y][new_x]<cell[y][x] and cell[y][x]!=-4:
                cell[new_y][new_x]=cell[y][x]

T=int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc))
    n,m,k=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(n)]
    print(data)

    cell=[[0]*(m+k) for _ in range(n+k)]
    act=[[0]*(m+k) for _ in range(n+k)]
    stat=[[0]*(m+k) for _ in range(n+k)]

    for y in range(n):
        for x in range(m):
            cell[y+k//2][x+k//2]=data[y][x]

    time=0

    for i in range(3):
        for y in range(n+k):
            for x in range(m+k):
                if act[y][x]<0: #활성화가 되어있다는 의미. 즉, 확산가능!
                    activate(y,x)
                    act[y][x]=0 #확산 후, 비활성화 상태!
                if cell[y][x]>0 and cell[y][x]==stat[y][x]: #활성화 조건
                    act[y][x]=-cell[y][x] # 활성화 배열에 cell값 음수값으로 지정.
                    stat[y][x]=-stat[y][x] #상태정보 cell값 음수값으로 지정. 다시 시간 세기 위해!
                if cell[y][x]>0 and stat[y][x]!=cell[y][x]: #값이 같아질때까지 시간 +하기 위해!
                    stat[y][x]+=1 # 각 셀마다 시간 증가
                    if stat[y][x]==0: # 상태가 0이 되었다는 건! 활성화 후, 시간이 지났다는 의미!!
                        # stat[y][x]=987654321 #다시 시간 셀 필요 없는 셀!
                        # act[y][x]=3 #죽음
                        cell[y][x]=-3

        print('-----------------cell------------------')
        for c in cell:
            print(c)
        print('-----------------act-------------------')
        for a in act:
            print(a)
        print('***************상태정보***************')
        for s in stat:
            print(s)
        print('=================={}시간 끝==================='.format(time))
        time+=1