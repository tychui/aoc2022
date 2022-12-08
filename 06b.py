s = input()
for i in range(13, len(s)):
    ss = s[i-13:i+1]
    status = False
    for j in range(14):
        for k in range(j+1, 14):
            if ss[j] == ss[k]:
                status = True
    if not status:
        print(i+1)
        exit()