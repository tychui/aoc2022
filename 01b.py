last = 0
maxi = 0
lst = []
while True:
    n = input()
    if n != '':
        n = int(n)
        last += n
    else:
        lst.append(last)
        lst.sort()
        lst.reverse()
        print(lst)
        last = 0
        if len(lst) >= 3:
            print(lst[0]+lst[1]+lst[2])
        print(len(lst))