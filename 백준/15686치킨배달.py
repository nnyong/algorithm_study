from itertools import combinations
import sys
sys.stdin=open("치킨배달.txt",'r')

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]

list1=[]
list2=[]
for y in range(n):
    for x in range(n):
        if data[y][x]==2:
            list2.append((y,x))
        elif data[y][x]==1:
            list1.append((y,x))

com_list = list(combinations(list2,m))

result=987654321
temp_result=0
for i in range(len(com_list)):
    for l1 in list1:
        min_temp=987654321
        for l2 in com_list[i]:
            temp=abs(l1[0]-l2[0])+abs(l1[1]-l2[1])
            if temp<min_temp:
                min_temp=temp
            print("l1: {}".format(l1))
            print(min_temp)
        temp_result+=min_temp
    if temp_result<result:
        result=temp_result

print(result)

