input = open('input.txt')

datastream = input.read()

print(datastream)


for i in range(3, len(datastream)):
    current = datastream[i]
    a, b, c = datastream[i-1], datastream[i-2], datastream[i-3]
    lastfour = [a, b, c, current]
    print(lastfour)
    print(set(lastfour))
    if (len(set(lastfour)) == len(lastfour)):
        print(i+1)
        break

for i in range(14, len(datastream)):
    currList = []
    for j in range(i, i-14, -1):
        if datastream[j] not in currList:
            currList.append(datastream[j])
            if len(currList) == 14:
                print(i+1)
                break
        else:
            currlist = []
            break
