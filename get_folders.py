import os

for i in range(1,26):
    filename = "G:\\advent_of_code_2022\\advent_of_code_2022\\" + f"day_{i:02d}"
    os.mkdir(filename)
    open(filename + "\\" + f"day_{i:02d}.py", 'a').close()
    