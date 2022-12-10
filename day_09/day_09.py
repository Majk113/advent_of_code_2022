sample = "sample_input.txt"
real = "real_input.txt"

from math import sqrt
from dataclasses import dataclass


@dataclass
class Move:
    direction: str
    value: int


@dataclass()
class Tile:
    visited: bool = False


class Solution1:
    def __init__(self, filename):
        self.movement = []
        self.grid = [[Tile() for _ in range(1000)] for _ in range(1000)]
        with open(filename, "r") as input_movement:
            for mov in input_movement:
                move = mov.rstrip().split()
                self.movement.append(Move(move[0], int(move[1])))

        self.head_row = 500
        self.head_col = 500
        self.tail_row = 500
        self.tail_col = 500
        self.visited_counter = 0
        self.visit_tile()


    def solve(self):
        for mov in self.movement:
            direction = mov.direction
            value = mov.value
            while value > 0:
                if direction == "R":
                    self.head_col += 1
                    dist = self.check_distance()
                    if dist < 2:
                        pass
                    elif dist >= 2:
                        self.tail_col = self.head_col - 1
                        self.tail_row = self.head_row


                if direction == "L":
                    self.head_col -= 1
                    dist = self.check_distance()
                    if dist < 2:
                        pass
                    elif dist >= 2:
                        self.tail_col = self.head_col + 1
                        self.tail_row = self.head_row

                if direction == "U":
                    self.head_row -= 1
                    dist = self.check_distance()
                    if dist < 2:
                        pass
                    elif dist >= 2:
                        self.tail_row = self.head_row + 1
                        self.tail_col = self.head_col

                if direction == "D":
                    self.head_row += 1
                    dist = self.check_distance()
                    if dist < 2:
                        pass
                    elif dist >= 2:
                        self.tail_row = self.head_row - 1
                        self.tail_col = self.head_col

                self.visit_tile()
                value -= 1

    def check_distance(self):
        return sqrt((self.head_col - self.tail_col) ** 2 + (self.head_row - self.tail_row) ** 2)

    def visit_tile(self):
        if not self.grid[self.tail_row][self.tail_col].visited:
            self.visited_counter += 1
            self.grid[self.tail_row][self.tail_col].visited = True

    def count_visited(self):
        adad = 0
        for i in self.grid:
            for j in i:
                if j.visited:
                    adad += 0

        return adad


def solution_2(filename):
    pass


s1 = Solution1(real)
s1.solve()
print(s1.visited_counter)
