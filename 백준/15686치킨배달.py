from itertools import combinations
import sys
sys.stdin=open("치킨배달.txt",'r')

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]

list2=[]
for y in range(n):
    for x in range(n):
        if data[y][x]==2:
            list2.append((y, x))

# print(list2)
com_list = list(combinations(list2, m))
# print(com_list)

def chicken_dis(list2):
    global min_city_dis
    city_dis=0
    for y in range(n):
        for x in range(n):
            chic_dis=987654321
            if data[y][x] == 1:
                for l2 in list2:
                    temp=abs(y-l2[0])+abs(x-l2[1])
                    if temp<chic_dis:
                        chic_dis=temp
                        ll2=l2
                # print('l1:({},{}), l2:{}, {}'.format(y,x,ll2,chic_dis))
                city_dis+=chic_dis
                # print(city_dis)
                if city_dis>min_city_dis:
                    return city_dis
    # print('조합하나끝:{}'.format(city_dis))
    return city_dis


min_city_dis=987654321
for l2 in com_list:
    temp_city_dis=chicken_dis(l2)
    # print(temp_city_dis)
    if temp_city_dis<min_city_dis:
        min_city_dis=temp_city_dis
print(min_city_dis)

