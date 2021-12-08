with open('input.txt') as file:
    input, output = zip(*[row.strip().split('|') for row in file.readlines()])

uniqueLengths = [2,4,3,7]

instances = 0
for outputIndex in range(len(output)):
    segments = output[outputIndex].strip().split()

    for word in segments:
        if len(word) in uniqueLengths:
            instances +=1

print(instances)
