import sys,itertools
sys.stdin=open('연구소3.txt','r')

def isSafe(y, x):
    if y < n and y >= 0 and x < n and x >= 0:
        return True
    else:
        return False

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(n)]

    virus=[]
    for y in range(n):
        for x in range(n):
            if data[y][x]==2:
                virus.append((y,x))

    virus_comb=list(map(list,itertools.combinations(virus,3)))

    dy=[0,1,0,-1]
    dx=[1,0,-1,0]

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
                    if data[new_y][new_x]==1:
                        visited[new_y][new_x]='-'
                    elif data[new_y][new_x]==0:
                        visited[new_y][new_x]=visited[y][x]+1
                        que.append((new_y,new_x))
            print('que:{}'.format(que))
            for i in visited:
                print(i)
            print('---------------------')
            print(virus)
            return
        print('끝')

    print('========================')
    que=[]
    for v in virus_comb:
        visited = list([0] * n for _ in range(n))
        virusActive(v)
        if len(que)!=0:
            virusActive(que)