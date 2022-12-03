priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


input = open('input.txt')
rucksacks = input.read().splitlines()
sum = 0
for r in rucksacks:
    first = r[0:int((len(r)/2))]
    second = r[int((len(r)/2)):]
    for c in first:
        if c in second:
            temp = c.lower()
            p = priorities.index(temp) + 1
            sum += p
            if c.isupper():
                sum += 26
            break
sum = 0
for i in range(0, len(rucksacks)-2, 3):
    for c in rucksacks[i]:
        if c in rucksacks[i+1] and c in rucksacks[i+2]:
            temp = c.lower()
            p = priorities.index(temp) + 1
            sum += p
            if c.isupper():
                sum += 26
            break

print(sum)
