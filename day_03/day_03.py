sample = "sample_input.txt"
real = "real_input.txt"

from collections import Counter
from string import ascii_lowercase, ascii_uppercase

priorities = {letter: (priority + 1) for priority, letter in enumerate(ascii_lowercase)}
priorities.update(
    {letter: (priority + 27) for priority, letter in enumerate(ascii_uppercase)}
)


def solution_1(filename):
    items = []
    result = 0
    with open(filename, "r") as list_of_rucksacks:
        for rucksack in list_of_rucksacks:
            first_part = Counter(rucksack[: (len(rucksack) // 2)])
            second_part = Counter(rucksack[(len(rucksack) // 2) :])

            common_items = first_part & second_part
            items.extend([item for item in common_items.keys()])

    for item in items:
        result += priorities[item]

    return result



def solution_2(filename):
    f = open(filename, 'r')
    list_of_rucksacks = f.readlines()
    f.close()
    items = []

    for group in range(0, len(list_of_rucksacks), 3):
        current_group = list_of_rucksacks[group:(group+3)]
        common_items = Counter(current_group[0].strip()) & Counter(current_group[1].strip()) & Counter(current_group[2].strip())
        items.extend([item for item in common_items.keys()])

    return sum([priorities[item] for item in items])





print(solution_2(real))
