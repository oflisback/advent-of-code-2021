with open('input.txt') as file:
    rows = [row.split('|') for row in file.readlines()]
    input = [row[0].strip() for row in rows]
    output = [row[1].strip() for row in rows]

def contains(candidate, content):
    for c in content:
        if candidate.find(c) == -1:
            return False
    return True

sum = 0
for index in range(len(rows)):
    segments_to_numbers = {}
    numbers_to_segments = {}

    segments = sorted(input[index].strip().split(), key=len)

    def save(segment, number):
        sorted_segment = ''.join(sorted(segment))
        segments_to_numbers[sorted_segment] = number
        numbers_to_segments[number] = sorted_segment
        segments.remove(segment)

    save(segments[0], "1")
    save(segments[0], "7")
    save(segments[0], "4")
    save(segments[len(segments) - 1], "8")

    # 0, 3 and 9 are the ones remaining that contains 1, the shortest
    # segment is 3
    zero_three_nine = sorted([segment for segment in segments if contains(segment, numbers_to_segments["1"])], key=len)
    three = zero_three_nine[0]
    save(three, "3")
    zero_nine = zero_three_nine[1:]
    # Nine contains three
    nine = [value for value in zero_nine if contains(value, three)][0]
    # Zero doesn't
    zero = [value for value in zero_nine if not contains(value, three)][0]
    save(nine, "9")
    save(zero, "0")

    # 6 is the longest remaining
    save(segments[2], "6")

    def get_overlap(a, b):
        overlap = ''
        for c in a:
            if b.find(c) != -1:
                overlap +=c
        return overlap

    # Which part of the 1 is present in 6?
    overlap = get_overlap(numbers_to_segments["1"], numbers_to_segments["6"])
    # That part is in 5 but not in 2
    five = [segment for segment in segments if len(get_overlap(overlap, segment)) == 1][0]
    save(five, "5")
    save(segments[0], "2")

    output_segments = output[index].strip().split()

    number = ""
    for segment in output_segments:
        number += segments_to_numbers[''.join(sorted(segment))]
    sum += int(number)

print(sum)
