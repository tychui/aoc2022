last = 0
maxi = 0
while True:
    n = input()
    if n != '':
        n = int(n)
        last += n
    else:
        maxi = max(maxi, last)
        last = 0
        print(maxi)