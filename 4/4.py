input = open('input.txt')
pairs = input.read().splitlines()
ans = 0
amount = 0
for pair in pairs:
    amount += 1
    group = pair.split(',')
    first_elve = group[0].split('-')
    second_elve = group[1].split('-')

    first = int(first_elve[0])
    second = int(first_elve[1])
    third = int(second_elve[0])
    fourth = int(second_elve[1])
    if ((second >= third and first <= fourth) or (fourth <= first and third >= second)):
        print(group)
        ans += 1
print(ans)
#             -> 5-10 : 4-11 - kleiner höher
#


# a - b: c-d
#
# start1 - end1: start2 - end2
#
#
# end1 >= start2
# start1 = < end2
#
# end2 <= start1
# start2 >= end1
