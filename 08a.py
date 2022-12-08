cnt = 0
n = 99
exterior = 4*(n-1)
representation = []
for _ in range(n):
    s = input()
    lst = [c for c in s]
    map(int, lst)
    representation.append(lst)
for i in range(1, n-1):
    for j in range(1, n-1):
        current = representation[i][j]
        up = []
        down = []
        left = []
        right = []
        for k in range(n):
            if k < i:
                up.append(representation[k][j])
            if k > i:
                down.append(representation[k][j])
            if k < j:
                left.append(representation[i][k])
            if k > j: 
                right.append(representation[i][k])
        if current > max(up) or current > max(down) or current > max(left) or current > max(right): cnt += 1
print(cnt+exterior)