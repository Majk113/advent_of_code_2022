import os

py_file_template = ""

for i in range(1,26):
    filename = "G:\\advent_of_code_2022\\advent_of_code_2022\\" + f"day_{i:02d}"
    os.mkdir(filename)
    open(filename + "\\sample_input.txt", 'a').close()
    open(filename + "\\real_input.txt", 'a').close()
    with open(filename + "\\" + f"day_{i:02d}.py", 'a') as script:
        script.write(open("solution_template.py", "r").read())
