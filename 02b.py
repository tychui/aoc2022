ttl = 0
one = ['A', 'B', 'C']
two = ['X', 'Y', 'Z']
for _ in range(2500):
    score = 0
    first, second = input().split()
    # rock A/X, paper B/Y, scissors C/Z
    if second == 'X':
        score += 0
        if first == 'A':
            score += 3
        if first == 'B':
            score += 1
        if first == 'C':
            score += 2
    if second == 'Y':
        score += 3
        score += 1
        score += one.index(first)
    if second == 'Z':
        score += 6
        if first == 'A':
            score += 2
        if first == 'B':
            score += 3
        if first == 'C':
            score += 1
    ttl += score
print(ttl)