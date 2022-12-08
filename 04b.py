cnt = 1000
for _ in range(1000):
    a, b = input().split(',')
    one = list(map(int, a.split('-')))
    two = list(map(int, b.split('-')))
    if one[1] < two[0] or two[1] < one[0]: cnt -= 1
print(cnt)