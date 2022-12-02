sample = "sample_input.txt"
real = "real_input.txt"

ROCK = "AX"
PAPER = "BY"
SCISSORS = "CZ"

SHAPES = {
    "A": ROCK,
    "X": ROCK,
    "B": PAPER,
    "Y": PAPER,
    "C": SCISSORS,
    "Z": SCISSORS
}

BEATS = {
    PAPER: ROCK,
    ROCK: SCISSORS,
    SCISSORS: PAPER,
}

POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


def solution_1(filename):
    score = 0
    with open(filename, 'r') as game:
        for line in game:
            current_shapes = line.split()
            oponent_shape = SHAPES[current_shapes[0]]
            my_shape = SHAPES[current_shapes[1]]

            if oponent_shape in BEATS[my_shape]:
                score += (6 + POINTS[my_shape])

            elif my_shape in BEATS[oponent_shape]:
                score += (0 + POINTS[my_shape])

            else:
                score += (3 + POINTS[my_shape])

    return score




def solution_2(filename):
    score = 0
    with open(filename, 'r') as game:
        for line in game:
            current_shapes = line.split()
            oponent_shape = SHAPES[current_shapes[0]]
            my_intentions = current_shapes[1]

            if my_intentions == "X":
                my_shape = BEATS[oponent_shape]
            elif my_intentions == "Z":
                my_shape = BEATS[BEATS[oponent_shape]]
            else:
                my_shape = oponent_shape


            if oponent_shape in BEATS[my_shape]:
                score += (6 + POINTS[my_shape])

            elif my_shape in BEATS[oponent_shape]:
                score += (0 + POINTS[my_shape])

            else:
                score += (3 + POINTS[my_shape])

    return score


print(solution_2(real))
