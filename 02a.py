ttl = 0
one = ['A', 'B', 'C']
two = ['X', 'Y', 'Z']
for _ in range(2500):
    score = 0
    first, second = input().split()
    # rock A/X, paper B/Y, scissors C/Z
    if second == 'X':
        score += 1
    if second == 'Y':
        score += 2
    if second == 'Z':
        score += 3
    if one.index(first) == two.index(second):
        score += 3
    elif first == 'A' and second == 'Y':
        score += 6
    elif first == 'B' and second == 'Z':
        score += 6
    elif first == 'C' and second == 'X':
        score += 6
    ttl += score
print(ttl)