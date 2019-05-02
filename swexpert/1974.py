# 스도쿠 검증
import copy
T=int(input())
for test_case in range(1,T+1):
    s=[]
    for i in range(9):
        l=list(map(int,input().split()))
        s.append(l)
    s2=copy.deepcopy(s)
    row_check=[]
    for row in s2:
        row.sort()
        if row==[1,2,3,4,5,6,7,8,9]:
            row_check.append(True)
        else:
            row_check.append(False)
    # print(row_check)
    col_list=[]
    for index in range(len(s)):
        l=[]
        for col in range(len(s)):
            l.append(s[col][index])
        col_list.append(l)
    # print(col_list)
    col_check=[]
    for col in col_list:
        col.sort()
        if col==[1,2,3,4,5,6,7,8,9]:
            col_check.append(True)
        else:
            col_check.append(False) 
    # print(col_check)
    square_list=[]
    for i in [0,3,6]:
        for j in [0,3,6]:
            l=[]
            for row in range(i,i+3): 
                for col in range(j,j+3):
                    l.append(s[row][col])
            square_list.append(l)
    square_check=[]
    for sq in square_list:
        sq.sort()
        if sq==[1,2,3,4,5,6,7,8,9]:
            square_check.append(True)
        else:
            square_check.append(False) 
    ck=1
    for ck1 in row_check:
        for ck2 in col_check:
            for ck3 in square_check:
                if ck1==False or ck2==False or ck3==False:
                    ck=0
    print(f'#{test_case} {ck}')

# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9
