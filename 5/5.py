stack1 = ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q']
stack2 = ['W', 'D', 'B', 'G']
stack3 = ['F', 'W', 'R', 'T', 'S', 'Q', 'B']
stack4 = ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N']
stack5 = ['M', 'P', 'D', 'V', 'F']
stack6 = ['F', 'W', 'J']
stack7 = ['L', 'N', 'Q', 'B', 'J', 'V']
stack8 = ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N']
stack9 = ['J', 'S', 'Q', 'C', 'W', 'D', 'M']


stacks = [stack1, stack2, stack3, stack4,
          stack5, stack6, stack7, stack8, stack9]

# stack1 = ['Z', 'N']
# stack2 = ['M', 'C', 'D']
# stack3 = ['P']
# stacks = [stack1, stack2, stack3]

input = open('input.txt')
commands = input.read().splitlines()

step = -1


def move(amount, f, t):
    print(stack1, stack2, stack3)
    popped = []
    for i in range(amount):
        popped.append(f.pop())
    popped.reverse()
    for p in popped:
        t.append(p)
    print(stack1, stack2, stack3)


for command in commands:
    c = command.split(' ')
    am = int(c[1])
    fr = stacks[int(c[3])-1]
    to = stacks[int(c[5])-1]
    print(command)
    move(am, fr, to)

for stack in stacks:
    print(stack[-1])
