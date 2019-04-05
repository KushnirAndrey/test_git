import math
######### 123 4
#######
#####3
###
n = int(input())
s = [int(i) for i in input().split()]
c = int(input())
razn = 1000
razn2 = 1000
index = None
for i in range(len(s)):
    if s[i] == c:
        print(s[i])
        index = None
        break
    else:
        razn2 = c - math.fabs(s[i])
        if razn2 <= 0:
            continue
        elif razn2 < razn:
            razn = razn2
            index = i
if index is not None:
    print(s[index])
