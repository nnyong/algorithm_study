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

    act = [[0] * (m + k) for _ in range(n + k)]
    # ---------------------------------------------------
    time=0
    for i in range(3):
        time+=1
        # 확산
        for y in range(n+k):
            for x in range(m+k):
                if act[y][x] < 0:  # 활성화된 상태면?! 확산해라
                    activate(y, x)
        print('---------------확산 후----------------')
        print('-----------------cell------------------')
        for c in cell:
            print(c)
        print('-----------------act-------------------')
        for a in act:
            print(a)
        print('***************상태정보***************')
        for s in stat:
            print(s)
        # 상태정보 업데이트
        for y in range(n + k):
            for x in range(m + k):
                if cell[y][x]>0:
                    stat[y][x]+=1
                if stat[y][x]<0:
                    stat[y][x]-=1
                    if stat[y][x]==-cell[y][x]:
                        cell[y][x]=-4

        print('---------------상태 업데이트 후----------------')
        print('***************상태정보***************')
        for s in stat:
            print(s)
        # 활성화
        for y in range(n + k):
            for x in range(m + k):
                if stat[y][x]>0 and stat[y][x]==cell[y][x]: #활성화하기!
                    act[y][x]=-cell[y][x]
                    stat[y][x] = -1
        print('---------------활성화 후----------------')
        print('---------------{}시간 후----------------'.format(time))
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


