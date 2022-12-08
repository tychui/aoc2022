class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.sub = []

    def addfile(self, filesize, filename):
        self.sub.append(File(filename, filesize))
        self.size += filesize

    def adddirectory(self, direct):
        self.sub.append(direct)
        self.size += direct.size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

currentdir = []
directs = []
for _ in range(1006):
    s = input()
    slst = list(s.split())
    match slst:
        case '$', 'cd', '..':
            currentdir[-2].adddirectory(currentdir[-1])
            currentdir.pop()
        case '$', 'cd', direct:
            currentdir.append(Directory(direct))
            directs.append(currentdir[-1])
        case '$', 'ls':
            continue
        case 'dir', direct:
            continue
        case filesize, filename:
            currentdir[-1].addfile(int(filesize), filename)
while len(currentdir) != 1:
    currentdir[-2].adddirectory(currentdir[-1])
    currentdir.pop()
ttl = 0
for d in directs:
    if d.size <= 100000: 
        ttl += d.size
print(ttl)