import sys
from itertools import permutations #순열

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(permutations(n, 3))	

t = int(sys.stdin.readline())
for _ in range(t):
    test, s, b = map(int, sys.stdin.readline().split())
    test = list(str(test))
    removed_cnt = 0    


    leng = len(num)
    for i in range(leng):
        s_cnt = b_cnt = 0   
        i -= removed_cnt

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            num.remove(num[i])     
            removed_cnt += 1

print(len(num))