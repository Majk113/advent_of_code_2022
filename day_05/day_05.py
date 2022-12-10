sample = "sample_input.txt"
real = "real_input.txt"

from collections import defaultdict
from string import ascii_uppercase


def solution_1(filename):
    crane_input = ""
    stacks = defaultdict(list)
    with open(filename, 'r') as ff:
        crane_input = ff.readlines()

    line_of_stacks = 0
    number_of_stacks = 0
    for index, line in enumerate(crane_input):
        try:
            int(line.replace(' ', ''))
            number_of_stacks = len(line.split("   "))
            line_of_stacks = index
        except:
            pass


    for i in range(line_of_stacks-1, -1, -1):
        base = 0
        for j in range(number_of_stacks):
            element = crane_input[i][base + 1:base + 2]
            if element and element in ascii_uppercase:
                stacks[j+1].append(element)
            base += 4

    for i in range(line_of_stacks+2, len(crane_input)):
        line = crane_input[i].split()
        number = int(line[1])
        source = int(line[3])
        destination = int(line[5])

        while(number):
            crate = stacks[source].pop()
            stacks[destination].append(crate)
            number -= 1

    result = ""
    for stack in stacks:
        result += stacks[stack][-1]

    return result







def solution_2(filename):
    crane_input = ""
    stacks = defaultdict(list)
    with open(filename, 'r') as ff:
        crane_input = ff.readlines()

    line_of_stacks = 0
    number_of_stacks = 0
    for index, line in enumerate(crane_input):
        try:
            int(line.replace(' ', ''))
            number_of_stacks = len(line.split("   "))
            line_of_stacks = index
        except:
            pass

    for i in range(line_of_stacks - 1, -1, -1):
        base = 0
        for j in range(number_of_stacks):
            element = crane_input[i][base + 1:base + 2]
            if element and element in ascii_uppercase:
                stacks[j + 1].append(element)
            base += 4

    for i in range(line_of_stacks + 2, len(crane_input)):
        line = crane_input[i].split()
        number = int(line[1])
        source = int(line[3])
        destination = int(line[5])

        crates_to_move = []
        while (number):
            crate = stacks[source].pop()
            crates_to_move.append(crate)
            number -= 1

        if len(crates_to_move) > 1:
            crates_to_move.reverse()
        stacks[destination].extend(crates_to_move)

    result = ""
    for stack in stacks:
        result += stacks[stack][-1]

    return result

print(solution_2(real))