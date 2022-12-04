sample = "sample_input.txt"
real = "real_input.txt"


class Pair:
    def __init__(self, pair):
        first, second = pair.split(",")
        self.first_start = int(first.split("-")[0])
        self.first_stop = int(first.split("-")[1])
        self.second_start = int(second.split("-")[0])
        self.second_stop = int(second.split("-")[1])


def solution_1(filename):
    overlaps_counter = 0
    with open(filename, "r") as pairs:
        for pair in pairs:
            current_pair = Pair(pair)

            if (
                (current_pair.first_start >= current_pair.second_start)
                and (current_pair.first_stop <= current_pair.second_stop)
            ) or (
                (current_pair.second_start >= current_pair.first_start)
                and (current_pair.second_stop <= current_pair.first_stop)
            ):
                overlaps_counter += 1

    return overlaps_counter


def solution_2(filename):
    overlaps_counter = 0
    with open(filename, "r") as pairs:
        for pair in pairs:
            current_pair = Pair(pair)

            if (
                (
                    (current_pair.first_start >= current_pair.second_start)
                    and (current_pair.first_stop <= current_pair.second_stop)
                )
                or (
                    (current_pair.second_start >= current_pair.first_start)
                    and (current_pair.second_stop <= current_pair.first_stop)
                )
                or (
                    (current_pair.first_start <= current_pair.second_stop)
                    and (current_pair.first_start >= current_pair.second_start)
                )
                or (current_pair.first_stop >= current_pair.second_start)
                and (current_pair.first_stop <= current_pair.second_stop)
            ):
                overlaps_counter += 1

    return overlaps_counter


print(solution_2(real))
