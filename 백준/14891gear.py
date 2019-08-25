import sys
sys.stdin=open('input.txt','r')

def rotate(gear, direction):
    if direction==1: #시계방향
        temp = gearwheel[gear][7]
        for i in range(7,0,-1):
            gearwheel[gear][i]=gearwheel[gear][i-1]
        gearwheel[gear][0]=temp
    else:
        temp = gearwheel[gear][0]
        for i in range(7):
            gearwheel[gear][i]=gearwheel[gear][i+1]
        gearwheel[gear][7]=temp

gearwheel = [list(map(int, input()) )for _ in range(4)]
k = int(input())
method = [list(map(int, input().split())) for _ in range(k)]

for m in method:
    rotation_list = [[m[0]-1,m[1]]]
    front=-1
    rear=0
    while front!=rear:
        front+=1
        gear=rotation_list[front][0]
        direction=rotation_list[front][1]
        if gear==0:
            if gearwheel[gear][2]!=gearwheel[gear+1][6]: #다르면 gear1도 회전
                if direction == 1:
                    if [gear+1,-1] not in rotation_list:
                        rotation_list.append([gear+1,-1])
                        rear+=1
                else:
                    if [gear+1,1] not in rotation_list:
                        rotation_list.append([gear+1,1])
                        rear+=1
        elif gear==1:
            if gearwheel[gear][2]!=gearwheel[gear+1][6]:
                if direction == 1:
                    if [gear+1,-1] not in rotation_list:
                        rotation_list.append([gear+1,-1])
                        rear += 1
                else:
                    if [gear+1,1] not in rotation_list:
                        rotation_list.append([gear+1,1])
                        rear += 1
            if gearwheel[gear][6] != gearwheel[gear - 1][2]:
                if direction == 1:
                    if [gear-1,-1] not in rotation_list:
                        rotation_list.append([gear-1,-1])
                        rear += 1
                else:
                    if [gear-1,1] not in rotation_list:
                        rotation_list.append([gear-1,1])
                        rear += 1
        elif gear==2:
            if gearwheel[gear][2]!=gearwheel[gear+1][6]:
                if direction == 1:
                    if [gear+1,-1] not in rotation_list:
                        rotation_list.append([gear+1,-1])
                        rear += 1
                else:
                    if [gear+1,1] not in rotation_list:
                        rotation_list.append([gear+1,1])
                        rear += 1
            if gearwheel[gear][6] != gearwheel[gear - 1][2]:
                if direction == 1:
                    if [gear-1,-1] not in rotation_list:
                        rotation_list.append([gear-1,-1])
                        rear += 1
                else:
                    if [gear-1,1] not in rotation_list:
                        rotation_list.append([gear-1,1])
                        rear += 1
        else:
            if gearwheel[gear][6]!=gearwheel[gear-1][2]:
                if direction == 1:
                    if [gear-1,-1] not in rotation_list:
                        rotation_list.append([gear-1,-1])
                        rear += 1
                else:
                    if [gear-1,1] not in rotation_list:
                        rotation_list.append([gear-1,1])
                        rear += 1
    for r in rotation_list:
        gear=r[0]
        direction=r[1]
        rotate(gear,direction)

result=0
if gearwheel[0][0]==1:
    result+=1
if gearwheel[1][0]==1:
    result+=2
if gearwheel[2][0]==1:
    result+=4
if gearwheel[3][0]==1:
    result+=8
print(result)