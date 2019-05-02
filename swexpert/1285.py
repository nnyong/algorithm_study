l=list(map(int, input().split()))

p=0
new_l=[]
for i in l:
    new_l.append(abs(i-p))
count=0
min_value=0
for i in new_l:
    if min_value ==False:
        min_value=i
    else:
        if i<=min_value:
            min_value=i
            if i==min_value:
                count+=1
if min_value==new_l[0]:
    count+=1
print(f'#1 {min_value} {count}')