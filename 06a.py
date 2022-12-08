s = input()
for i in range(3, len(s)):
    ss = s[i-3:i+1]
    status = False
    for j in range(4):
        for k in range(j+1, 4):
            if ss[j] == ss[k]:
                status = True
    if not status:
        print(i+1)
        exit()