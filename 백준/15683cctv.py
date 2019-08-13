# cctv
import sys
sys.stdin=open('cctv.txt','r')

n,m=list(map(int,input().split()))
data=[list(map(int,input().split())) for _ in range(n)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]

# 5인경우, 0~3다 보기! 한번에
# 4인경우, (0,1,2),(0,1,3),(0,2,3),(1,2,3) 해보고 가장 0이 많은 것! 선택!
# 3인경우, (0,1),(1,2),(2,3),(3,1) 해보고 가장 0 많은 것!
# 2인경우, (0,2),(1,3) 해보고 가장 0 많은 것!
# 1인경우, 0,1,2,3 해보고 가장 0 많은 것!

# 6나오면 continue, 다른 숫자 나오면 cnt 올리지 말기!
# 0나오면 cnt올리기.
# 큰수부터 먼저 # 채우기

# def findMaxZero(n):

def isSafe(y,x):
    if y<n and y>=0 and x<m and x>=0:
        return True
    else:
        return False

li=[]
for i in range(5,0,-1):
    for y in range(n):
        for x  in range(m):
            if data[y][x]==i:
                li.append((y,x,i))

for l in li:
    y=l[0]
    x=l[1]
    num = l[2]
    if num==1:
        max_cnt=0
        max_dir=0
        for dir in range(4):
            cnt=0
            newy=y
            newx=x
            while isSafe(newy,newx):
                newy=newy+dy[dir]
                newx=newx+dx[dir]
                if isSafe(newy,newx):
                    if data[newy][newx]==6:
                        break
                    elif data[newy][newx]==0:
                        cnt+=1
            if cnt>max_cnt:
                max_cnt=cnt
                max_dir=dir
        newy=y
        newx=x
        while isSafe(newy,newx):
            newy = newy + dy[max_dir]
            newx = newx + dx[max_dir]
            if isSafe(newy,newx):
                if data[newy][newx] == 6:
                    break
                elif data[newy][newx]==0:
                    data[newy][newx]='#'
    elif num==2:
        max_cnt = 0
        max_dir = 0
        for dir in [(0,2),(1,3)]:
            cnt = 0
            for d in dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_dir = dir
        if max_cnt!=0:
            for d in max_dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            data[newy][newx] = '#'
    elif num==3:
        max_cnt = 0
        max_dir = 0
        for dir in [(0,1),(1,2),(2,3),(3,1)]:
            cnt = 0
            for d in dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_dir = dir
        if max_cnt!=0:
            for d in max_dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            data[newy][newx] = '#'
    elif num==4:
        max_cnt = 0
        max_dir = 0
        for dir in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]:
            cnt = 0
            for d in dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_dir = dir
        if max_cnt!=0:
            for d in max_dir:
                newy = y
                newx = x
                while isSafe(newy, newx):
                    newy = newy + dy[d]
                    newx = newx + dx[d]
                    if isSafe(newy,newx):
                        if data[newy][newx] == 6:
                            break
                        elif data[newy][newx] == 0:
                            data[newy][newx] = '#'
    elif num==5:
        for d in range(4):
            newy = y
            newx = x
            while isSafe(newy, newx):
                newy = newy + dy[d]
                newx = newx + dx[d]
                if isSafe(newy,newx):
                    if data[newy][newx] == 6:
                        break
                    elif data[newy][newx] == 0:
                        data[newy][newx] = '#'

result=0
for y in range(n):
    for x in range(m):
        if data[y][x]==0:
            result+=1
print(result)
