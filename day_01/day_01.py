sample = "sample_input.txt"
real = "real_input.txt"


def solution_1(filename):
    sample_input = open(filename, 'r').read().split('\n\n')
    max_calories = 0
    for elf in sample_input:
        current_calories = 0
        for calories in elf.split():
            current_calories += int(calories)

        max_calories = current_calories if current_calories > max_calories else max_calories

    return max_calories

def solution_2(filename):
    sample_input = open(filename, 'r').read().split('\n\n')
    max_calories = []
    for elf in sample_input:
        current_calories = 0
        for calories in elf.split():
            current_calories += int(calories)

        max_calories.append(current_calories)

    max_calories.sort()
    return sum(max_calories[-3:])

print(solution_2(real))