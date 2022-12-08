score = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
scr = 0
for _ in range(300):
    s = input()
    n = len(s)
    one = [c for c in s[0:(n//2)]]
    two = [c for c in s[(n//2):]]
    oneset = set(one)
    twoset = set(two)
    c = oneset.intersection(twoset)
    for cha in c:
        scr += (score.index(cha))
print(scr)