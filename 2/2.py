# A = Rock
# B = Paper
# C = Scissor

# X = Rock
# Y = Paper
# Z = Scissor

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

win = 6
draw = 3
loose = 0
losing_rounds = ['A Z', 'B X', 'C Y']
draw_rounds = ['A X', 'B Y', 'C Z']
winning_rounds = ['A Y', 'B Z', 'C X']

input = open('input.txt')
rounds = input.read().splitlines()
score = 0
for round in rounds:
    print(round)
    match round[-1]:
        case 'X':
            r = next(filter(lambda c: c[0] == round[0], losing_rounds), None)
            s = scores[r[-1]]
            score += s

        case 'Y':
            r = next(filter(lambda c: c[0] == round[0], draw_rounds), None)
            s = scores[r[-1]] + draw
            score += s
        case 'Z':
            r = next(filter(lambda c: c[0] == round[0], winning_rounds), None)
            s = scores[r[-1]] + win
            score += s
print(score)
