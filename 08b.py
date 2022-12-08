maxi = 0
n = 99
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
        upc = 0
        downc = 0
        leftc = 0
        rightc = 0
        for k in range(len(up)-1, -1, -1):
            upc += 1
            if up[k] >= current:
                break
        for k in range(len(down)):
            downc += 1
            if down[k] >= current:
                break
        for k in range(len(left)-1, -1, -1):
            leftc += 1
            if left[k] >= current:
                break
        for k in range(len(right)):
            rightc += 1
            if right[k] >= current:
                break
        scenic = upc*downc*leftc*rightc
        maxi = max(scenic, maxi)
print(maxi)