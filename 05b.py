stack = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'], ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'], ['G', 'F', 'Q', 'T', 'S', 'L', 'B'], ['L', 'G', 'C', 'Z', 'V'], ['N', 'L', 'G'], ['J', 'F', 'H', 'C']]
for _ in range(501):
    move, moveno, fr, initial, to, final = input().split()
    moveno = int(moveno)
    initial = int(initial)-1
    final = int(final)-1
    n = len(stack[initial])
    for element in stack[initial][(n-moveno):]:
        stack[final].append(element)
    for i in range(moveno):
        stack[initial].pop()
for i in range(9):
    print(stack[i][-1])