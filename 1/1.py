
def main():
    part1()
    part2()


def part1():
    file = open('input.txt')
    temp = 0
    max = 0
    for line in file:
        if (line != "\n"):
            temp += int(line.strip())
        else:
            if (temp > max):
                max = temp
            temp = 0
    print(max)


def part2():
    file = open('input.txt')
    temp = 0
    elves = []
    for line in file:
        if (line != "\n"):
            temp += int(line.strip())
        else:
            elves.append(temp)
            temp = 0
    elves.append(temp)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


if __name__ == '__main__':
    main()
