def part1():

    input = open('input.txt')

    lines = input.read().split()

    trees = []
    for line in lines:
        trees.append(list(line))
    ans = 0
    ans += ((len(trees)-1) * 2)
    ans += ((len(trees[0]) - 1) * 2)
    print(ans)
    for i in range(1, len(trees)-1):
        edges = []
        for j in range(1, len(trees[i]) - 1):
            left = []
            right = []
            up = []
            down = []
            for l in range(0, j):
                left.append(int(trees[i][l]))
            for r in range(j+1, len(trees[i])):
                right.append(int(trees[i][r]))
            for u in range(0, i):
                up.append(int(trees[u][j]))
            for d in range(i+1, len(trees[j])):
                down.append(int(trees[d][j]))
            print(left, right, up, down)
            upmax = max(up)
            downmax = max(down)
            leftmax = max(left)
            rightmax = max(right)
            if (int(trees[i][j]) > upmax or int(trees[i][j]) > downmax or int(trees[i][j]) > leftmax or int(trees[i][j]) > rightmax):
                ans += 1

        print(edges)

        print('next line')
        print(ans)


def part2():

    input = open('input.txt')

    lines = input.read().split()

    trees = []
    for line in lines:
        trees.append(list(line))
    ans = 0
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            visleft = 0
            visright = 0
            visup = 0
            visdown = 0
            left = []
            right = []
            up = []
            down = []
            for l in range(0, j):
                left.append(int(trees[i][l]))
            for r in range(j+1, len(trees[i])):
                right.append(int(trees[i][r]))
            for u in range(0, i):
                up.append(int(trees[u][j]))
            for d in range(i+1, len(trees[j])):
                down.append(int(trees[d][j]))
            print(f'next number is {trees[i][j]}')

            left.reverse()
            up.reverse()
            print(left, right, up, down)
            for o in range(0, len(left)):
                print(left[o], trees[i][j], o)
                if left[o] >= int(trees[i][j]):
                    visleft = o+1
                    break
                visleft = len(left)
            print(f'left: {visleft}')
            for o in range(0, len(right)):
                print(right[0], trees[i][j], o)
                if right[o] >= int(trees[i][j]):
                    visright = o+1
                    break
                visright = len(right)
            print(f'right {visright}')
            for o in range(0, len(up)):
                if up[o] >= int(trees[i][j]):
                    visup = o+1
                    break
                visup = len(up)
            print(f'visup: {visup}')
            for o in range(0, len(down)):
                if down[o] >= int(trees[i][j]):
                    visdown = o+1
                    break
                visdown = len(down)
            print(f'visdown: {visdown}')
            temp = visup * visdown * visleft * visright
            if temp > ans:
                ans = temp
            print(ans)


part2()
