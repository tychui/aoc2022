score = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
scr = 0
for _ in range(100):
    lst = []
    for i in range(3):
        s = input()
        lst.append(s)
    one = [c for c in lst[0]]
    two = [c for c in lst[1]]
    three = [c for c in lst[2]]
    oneset = set(one)
    twoset = set(two)
    threeset = set(three)
    onetwo = oneset.intersection(twoset)
    c = onetwo.intersection(threeset)
    for cha in c:
        scr += (score.index(cha))
print(scr)