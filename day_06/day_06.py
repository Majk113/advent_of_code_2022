sample = "sample_input.txt"
real = "real_input.txt"


def solution_1(datastream):
    for i in range(len(datastream) - 4):
        if len(set(datastream[i:i+4])) == 4:
            return (i+4)



def solution_2(datastream):
    for i in range(len(datastream) - 14):
        if len(set(datastream[i:i + 14])) == 14:
            return (i + 14)


with open(real, 'r') as datastream:
    print(solution_2(datastream.read()))
