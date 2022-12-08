cnt = 0
for _ in range(1000):
    a, b = input().split(',')
    one = list(map(int, a.split('-')))
    two = list(map(int, b.split('-')))
    if (one[0] >= two[0] and one[1] <= two[1]) or (one[0] <= two[0] and one[1] >= two[1]): cnt += 1
print(cnt)