import sys
sys.stdin=open('큐빙','r')

T=int(input())
for tc in range(1,T+1):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    n=int(input())
    data=list(input().split())
    for i in range(n):
        if data[i][0]=='U':
            if data[i][1]=='-':
                for y in range(3):
                    temp=B[0][y]
                    B[0][y]=R[0][y]
                    R[0][y]=F[0][y]
                    F[0][y]=L[0][y]
                    L[0][y]=temp
                U = list(map(list, zip(*[U[i][::-1] for i in range(3)])))
            else:
                for y in range(3):
                    temp = B[0][y]
                    B[0][y] = L[0][y]
                    L[0][y] = F[0][y]
                    F[0][y] = R[0][y]
                    R[0][y] = temp
                U=list(map(list,zip(*U[::-1])))
        if data[i][0]=='D':
            if data[i][1]=='-':
                for y in range(3):
                    temp=B[2][y]
                    B[2][y]=R[2][y]
                    R[2][y]=F[2][y]
                    F[2][y]=L[2][y]
                    L[2][y]=temp
                D = list(map(list, zip(*[D[i][::-1] for i in range(3)])))
            else:
                for y in range(3):
                    temp = B[2][y]
                    B[2][y] = L[2][y]
                    L[2][y] = F[2][y]
                    F[2][y] = R[2][y]
                    R[2][y] = temp
                D=list(map(list,zip(*D[::-1])))
        if data[i][0]=='F':
            if data[i][1]=='-':
                for y in range(3):
                    temp=U[2][y]
                    U[2][y]=R[y][0]
                    R[y][0]=D[2][y]
                    D[2][y]=L[y][2]
                    L[y][2]=temp
                F = list(map(list, zip(*[F[i][::-1] for i in range(3)])))
            else:
                for y in range(3):
                    temp=U[2][y]
                    U[2][y]=L[y][2]
                    L[y][2]=D[2][y]
                    D[2][y]=R[y][0]
                    R[y][0]=temp
                F=list(map(list,zip(*F[::-1])))
        if data[i][0]=='B':
            if data[i][1]=='-':
                for y in range(3):
                    temp=U[0][y]
                    U[0][y]=L[y][0]
                    L[y][0]=D[0][y]
                    D[0][y]=R[y][2]
                    R[y][2]=temp
                B = list(map(list, zip(*B[::-1])))
            else:
                for y in range(3):
                    temp = U[0][y]
                    U[0][y] = R[y][2]
                    R[y][2] = D[0][y]
                    D[0][y] = L[y][0]
                    L[y][0] = temp
                B = list(map(list, zip(*[B[i][::-1] for i in range(3)])))
        if data[i][0]=='L':
            if data[i][1]=='-':
                for y in range(3):
                    temp=U[y][0]
                    U[y][0]=F[y][0]
                    F[y][0]=D[y][0]
                    D[y][0]=B[y][0]
                    B[y][0]=temp
                L = list(map(list, zip(*[L[i][::-1] for i in range(3)])))
            else:
                for y in range(3):
                    temp=F[y][0]
                    F[y][0]=U[y][0]
                    U[y][0]=B[y][0]
                    B[y][0]=D[y][0]
                    D[y][0]=temp
                L=list(map(list,zip(*L[::-1])))
        if data[i][0]=='R':
            if data[i][1]=='-':
                for y in range(3):
                    temp=U[y][2]
                    U[y][2]=B[y][2]
                    B[y][2]=D[y][2]
                    D[y][2]=F[y][2]
                    F[y][2]=temp
                R = list(map(list, zip(*[R[i][::-1] for i in range(3)])))
            else:
                for y in range(3):
                    temp = U[y][2]
                    U[y][2] = F[y][2]
                    F[y][2] = D[y][2]
                    D[y][2] = B[y][2]
                    B[y][2] = temp
                R=list(map(list,zip(*R[::-1])))
        for u in U:
            print(*u,sep='')
        print('============')
        print('')

