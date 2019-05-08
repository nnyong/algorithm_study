import sys,itertools
sys.stdin=open('연구소3.txt','r')

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def isSafe(y, x):
    if y < n and y >= 0 and x < n and x >= 0:
        return True
    else:
        return False

# 확산 완료 여부
def complete(map):
    for y in range(n):
        for x in range(n):
            if map[y][x]==0:
                return False
    return True

# 각 바이러스 조합별 확산 시간
def Time(visited):
    time = -1
    if complete(visited)==False:
        return time
    for y in range(n):
        for x in range(n):
            if type(visited[y][x])==int:
                if visited[y][x]>time:
                    time=visited[y][x]
    return time

# 바이러스 active
def virusActive(virus):
    print('virus: {}'.format(virus))
    for vi in virus:
        print('v:{}'.format(vi))
        y=vi[0]
        x=vi[1]
        for dir in range(4):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if isSafe(new_y,new_x):
                if data[new_y][new_x]==0:
                    print(new_y,new_x)
                    if not visited[new_y][new_x]:
                        visited[new_y][new_x]=visited[y][x]+1
                        que.append((new_y,new_x))
                elif data[new_y][new_x]==1:
                    visited[new_y][new_x] = '-'
                else:
                    visited[new_y][new_x]='*'
        if visited[y][x]==0:
            visited[y][x]='*'
        for v in visited:
            print(v)
        print('----------------------')
    print('que입니다용!')
    print(que)
    print('**********************')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(n)]

    # 바이러스 좌표 찾기
    virus=[]
    for y in range(n):
        for x in range(n):
            if data[y][x]==2:
                virus.append((y,x))

    # m개의 바이러스 조합 리스트
    virus_comb=list(map(list,itertools.combinations(virus,m)))

    # 모든 바이러스 조합에 대해 실행하기!
    que = []
    min_time=987654321
    for v in virus_comb:
        if complete(data):
            min_time=0
            break
        visited = list([0] * n for _ in range(n))
        virusActive(v)
        print('==================')
        if len(que)!=0:
            print('que에 값이 있다.que 시작!')
            virusActive(que)
            que = []
            print('조합별 바이러스 확산 시간: {}'.format(Time(visited)))
        time=Time(visited)
        if time!=-1:
            if time<min_time:
                min_time=time
        print('바이러스1개 조합 끝')
    print('================결과===================')
    if min_time==987654321:
        print(-1)
    else:
        print(min_time)