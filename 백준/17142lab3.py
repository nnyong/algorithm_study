import sys,itertools
sys.stdin=open("연구소3.txt",'r')

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
# print(n,m,data)

# 바이러스 리스트 만들기
virus=[]
def findvirus():
    for y in range(n):
        for x in range(n):
            if data[y][x]==2:
                virus.append((y,x))
findvirus()
# print(virus)

# 초기화
visited=[[0]*n for _ in range(n)]
virus_map = [['f'] * n for _ in range(n)]
def reset():
    for y in range(n):
        for x in range(n):
            if data[y][x]==1:
                virus_map[y][x]='-'
            elif data[y][x]==2:
                virus_map[y][x]='*'
reset()
# print(virus_map)

# 조합
def comb():
    return list(itertools.combinations(virus,m))
virus_comb=comb()
# print(virus_comb)

dy=[0,1,0,-1]
dx=[1,0,-1,0]
def isSafe(y,x):
    if y<n and y>=0 and x<n and x>=0 and virus_map[y][x]!='-' and virus_map[y][x]!=0:
        return True
    else:
        return False

# 완료확인
def end():
    for y in range(n):
        for x in range(n):
            if virus_map[y][x]=='f':
                return False
    return True
# 확산
def active_virus():
    while que!=[]:
        q=que.pop(0)
        y=q[0]
        x=q[1]
        for dir in range(4):
            newy=y+dy[dir]
            newx=x+dx[dir]
            if isSafe(newy,newx) and not visited[newy][newx]:
                if virus_map[newy][newx]=='*':
                    if end():
                        return
                visited[newy][newx]=1
                virus_map[newy][newx]=virus_map[y][x]+1
                que.append((newy,newx))

def max_time():
    max_value=0
    for y in range(n):
        for x in range(n):
            if virus_map[y][x]=='f':
                return -1
            if virus_map[y][x]!='-' and virus_map[y][x]!='*':
                if virus_map[y][x]>max_value:
                    max_value=virus_map[y][x]
    return max_value

result=987654321
for virus in virus_comb:
    que=[]
    for active in virus:
        virus_map[active[0]][active[1]]=0
        que.append((active[0],active[1]))
        visited[active[0]][active[1]]=1
    active_virus()
    # for vi in virus_map:
        # print(vi)
    max_time()
    max_value=max_time()
    if max_value!=-1 and max_value<result:
        result=max_value
    # print(max_value)
    # print('--------------------------------------')
    virus_map = [['f'] * n for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    reset()

if result==987654321:
    print(-1)
else:
    print(result)


