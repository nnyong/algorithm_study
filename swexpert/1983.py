# 조교의 성적매기기
import copy
T=int(input())
for test_case in range(1,T+1):
    n,k=map(int,input().split())
    score=[]
    for i in range(n):
        l=list(map(int,input().split()))
        score.append(l[0]*0.35+l[1]*0.45+l[2]*0.2)
    sorted_score=copy.deepcopy(score)
    sorted_score.sort(reverse=True)
    for index,value in enumerate(sorted_score):
        if score[k-1]==value:
            i=index
    grade=['A+']*(n//10)+['A0']*(n//10)+['A-']*(n//10)+['B+']*(n//10)+['B0']*(n//10)+['B-']*(n//10)+['C+']*(n//10)+['C0']*(n//10)+['C-']*(n//10)+['D0']*(n//10)
    m=dict(zip(sorted_score,grade))
    for key,value in m.items():
        if score[k-1]==key:
            i=value
    print(f'#{test_case} {i}')
# 10
# 10 2
# 87 59 88
# 99 94 78
# 94 86 86
# 99 100 99
# 69 76 70
# 76 89 96
# 98 95 96
# 74 69 60
# 98 84 67
# 85 84 91
# 20 12
# 76 58 78
# 96 100 99
# 97 99 98
# 96 100 98
# 98 97 100
# 57 67 77
# 75 99 63
# 84 81 79
# 99 99 98
# 85 74 88
# 87 98 85
# 85 80 73
# 92 79 75
# 79 93 93
# 94 83 94
# 99 99 99
# 55 94 71
# 90 89 77
# 98 100 98
# 98 99 98
# 30 12
# 76 88 86
# 100 89 91
# 91 90 83
# 86 82 96
# 78 76 98
# 94 85 96
# 80 91 97
# 63 63 58
# 97 100 99
# 95 76 89
# 97 88 96
# 76 76 96
# 89 82 99
# 62 95 83
# 63 88 60
# 74 77 72
# 98 87 92
# 99 84 58
# 74 76 99
# 81 81 84
# 79 100 72
# 97 88 98
# 97 94 98
# 96 66 74
# 87 89 87
# 69 73 95
# 89 97 91
# 82 94 85
# 85 89 75
# 89 80 91
# 40 18
# 69 71 57
# 92 83 95
# 100 97 100
# 97 96 99
# 98 94 89
# 53 84 83
# 80 96 81
# 100 96 98
# 100 75 100
# 69 62 90
# 99 63 66
# 66 99 94
# 98 78 73
# 97 95 91
# 86 85 89
# 76 85 90
# 98 96 96
# 94 96 100
# 62 60 84
# 70 79 70
# 97 98 90
# 94 98 100
# 75 95 82
# 94 56 65
# 80 90 90
# 97 97 100
# 93 86 79
# 93 96 87
# 100 93 93
# 79 90 79
# 88 77 95
# 73 83 91
# 72 57 84
# 95 99 91
# 86 75 100
# 100 69 56
# 85 99 97
# 100 96 100
# 98 99 98
# 79 96 91
# 50 43
# 83 61 74
# 96 83 84
# 78 81 81
# 100 100 100
# 98 100 98
# 93 93 98
# 89 77 80
# 98 99 99
# 99 100 74
# 91 76 72
# 100 71 70
# 70 84 55
# 71 99 96
# 79 94 77
# 95 85 100
# 99 100 99
# 99 94 99
# 89 68 74
# 89 62 66
# 66 88 78
# 96 98 100
# 93 54 94
# 96 89 94
# 96 76 65
# 99 99 99
# 86 98 95
# 98 97 99
# 98 90 82
# 99 98 97
# 89 74 66
# 63 76 91
# 86 93 78
# 88 83 94
# 97 96 96
# 98 89 90
# 90 62 66
# 83 74 74
# 57 67 77
# 95 93 89
# 66 86 73
# 70 81 68
# 94 97 80
# 75 76 90
# 89 80 98
# 94 99 98
# 97 93 94
# 86 100 92
# 92 69 68
# 100 99 95
# 96 97 89
# 60 6
# 83 93 86
# 72 59 75
# 98 94 99
# 93 91 70
# 78 79 89
# 91 99 95
# 71 83 83
# 71 96 74
# 97 83 69
# 97 94 97
# 99 98 73
# 76 70 92
# 99 100 99
# 98 99 90
# 83 95 84
# 88 85 85
# 90 81 74
# 96 98 99
# 92 94 89
# 76 90 81
# 95 68 69
# 100 99 99
# 83 53 67
# 84 85 94
# 91 79 96
# 99 100 98
# 100 82 84
# 100 99 96
# 83 76 92
# 89 97 78
# 99 95 100
# 99 82 92
# 100 85 85
# 67 100 80
# 85 91 75
# 99 92 86
# 93 86 97
# 100 94 97
# 76 67 63
# 78 89 73
# 68 88 100
# 78 88 94
# 93 79 96
# 93 100 89
# 90 57 70
# 97 98 99
# 79 69 77
# 99 97 94
# 87 98 93
# 84 86 90
# 64 91 64
# 94 84 99
# 100 100 100
# 74 88 94
# 93 73 68
# 82 64 74
# 97 99 98
# 82 99 80
# 86 87 89
# 99 96 97
# 70 37
# 70 81 80
# 83 83 80
# 84 88 93
# 92 96 95
# 98 59 76
# 88 81 74
# 93 91 98
# 99 100 99
# 81 89 82
# 90 89 81
# 67 95 79
# 93 89 91
# 87 79 57
# 96 92 96
# 100 86 88
# 97 100 92
# 77 100 87
# 86 90 73
# 100 100 99
# 97 96 91
# 90 95 97
# 70 84 76
# 90 80 78
# 71 79 86
# 98 98 98
# 94 94 85
# 86 91 85
# 93 96 96
# 90 70 73
# 94 99 98
# 81 86 78
# 94 96 69
# 99 97 99
# 90 96 67
# 61 69 91
# 85 82 93
# 79 95 78
# 87 81 67
# 98 75 68
# 84 60 71
# 93 89 93
# 72 73 81
# 90 89 80
# 100 96 98
# 91 96 99
# 100 99 100
# 81 91 84
# 82 93 97
# 92 78 100
# 97 100 97
# 95 86 89
# 95 100 94
# 97 94 91
# 78 80 82
# 87 100 83
# 96 55 75
# 83 94 99
# 99 97 90
# 100 99 99
# 71 91 65
# 90 69 64
# 99 98 99
# 88 98 87
# 89 90 99
# 100 97 98
# 94 99 100
# 86 98 88
# 84 81 90
# 83 86 94
# 70 68 93
# 80 64
# 88 93 93
# 91 63 71
# 88 93 99
# 93 87 94
# 83 74 97
# 86 88 87
# 91 97 78
# 68 63 82
# 64 72 60
# 72 69 75
# 69 77 76
# 78 81 91
# 95 93 95
# 77 91 80
# 82 92 84
# 73 99 72
# 99 100 100
# 99 98 98
# 95 98 98
# 87 95 100
# 90 95 97
# 73 75 80
# 59 100 65
# 96 93 97
# 66 92 83
# 87 93 88
# 67 91 75
# 83 76 87
# 87 91 86
# 73 71 92
# 85 98 83
# 91 91 85
# 99 94 91
# 81 83 63
# 97 71 79
# 82 93 94
# 92 64 94
# 74 87 81
# 93 97 98
# 82 82 94
# 95 98 93
# 77 76 82
# 72 81 88
# 100 100 99
# 96 99 88
# 94 92 94
# 94 86 85
# 97 96 95
# 99 94 82
# 88 78 94
# 69 81 83
# 81 72 70
# 83 65 78
# 68 70 96
# 100 99 100
# 91 68 89
# 78 91 79
# 99 94 91
# 89 83 86
# 93 87 86
# 94 70 84
# 92 97 90
# 75 95 74
# 76 83 93
# 88 86 100
# 96 95 89
# 69 69 89
# 93 91 98
# 100 77 98
# 69 59 62
# 83 97 100
# 93 100 77
# 79 88 57
# 99 86 85
# 77 93 80
# 96 100 97
# 83 94 88
# 88 93 98
# 94 90 84
# 97 79 72
# 90 83
# 71 95 81
# 93 87 99
# 94 95 95
# 89 84 98
# 99 99 96
# 77 77 91
# 95 76 71
# 74 78 98
# 95 97 96
# 85 71 77
# 74 97 95
# 65 76 94
# 90 92 89
# 92 97 96
# 86 81 84
# 85 100 77
# 95 97 100
# 96 98 97
# 87 62 54
# 87 80 65
# 99 95 76
# 84 79 90
# 83 64 59
# 91 95 92
# 93 90 92
# 99 94 96
# 69 90 72
# 68 99 82
# 85 77 88
# 99 98 98
# 85 99 96
# 93 97 95
# 81 93 97
# 85 98 94
# 100 95 97
# 88 91 87
# 100 95 95
# 76 90 76
# 88 92 99
# 90 84 95
# 95 100 100
# 99 99 99
# 97 98 96
# 52 73 92
# 89 87 82
# 69 67 84
# 84 83 79
# 86 70 93
# 83 86 72
# 98 87 93
# 77 62 82
# 98 100 94
# 92 75 80
# 92 66 100
# 88 93 94
# 88 81 91
# 77 82 76
# 76 94 87
# 92 71 99
# 70 88 73
# 64 67 72
# 77 82 86
# 77 72 98
# 90 90 97
# 100 97 96
# 79 86 81
# 65 63 80
# 94 70 84
# 90 84 96
# 100 85 96
# 95 89 99
# 85 100 67
# 90 69 79
# 89 91 88
# 60 90 83
# 79 70 83
# 87 88 81
# 92 82 100
# 88 79 91
# 92 85 98
# 99 99 100
# 55 96 53
# 96 78 100
# 74 77 80
# 92 56 65
# 90 91 96
# 95 86 96
# 83 80 89
# 100 99 98
# 100 100 100
# 100 14
# 96 81 80
# 80 95 62
# 92 86 78
# 96 94 95
# 88 85 85
# 100 98 94
# 94 96 97
# 86 81 90
# 97 97 89
# 88 94 86
# 87 99 94
# 91 91 94
# 77 84 85
# 97 97 94
# 73 77 90
# 63 90 85
# 97 96 83
# 59 73 89
# 96 89 90
# 64 62 63
# 88 77 79
# 100 99 100
# 92 90 94
# 94 94 90
# 96 83 96
# 99 99 97
# 92 73 71
# 96 81 98
# 80 69 71
# 63 98 79
# 100 100 99
# 99 100 99
# 99 100 97
# 97 68 53
# 80 86 85
# 86 94 82
# 96 88 98
# 73 98 96
# 97 97 95
# 77 93 96
# 70 97 89
# 80 77 78
# 80 92 86
# 96 94 90
# 89 84 92
# 75 69 68
# 90 90 70
# 96 92 92
# 99 100 98
# 98 93 98
# 84 83 82
# 100 99 100
# 80 91 99
# 99 96 93
# 89 100 94
# 93 95 90
# 89 86 95
# 95 98 98
# 58 91 71
# 75 79 99
# 83 89 70
# 96 92 97
# 62 98 97
# 97 91 90
# 96 81 66
# 83 77 91
# 92 86 91
# 99 99 100
# 90 86 95
# 96 76 78
# 92 98 74
# 90 88 90
# 58 81 66
# 96 94 85
# 100 92 93
# 74 65 65
# 79 82 74
# 95 88 70
# 99 99 99
# 98 99 82
# 84 83 88
# 59 87 100
# 95 88 94
# 86 85 94
# 97 70 71
# 82 77 91
# 95 90 94
# 88 67 62
# 74 77 74
# 68 75 85
# 84 73 98
# 71 56 72
# 99 98 99
# 93 96 98
# 59 75 89
# 70 72 59
# 97 59 79
# 90 90 94
# 92 99 86
# 75 95 98

#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0