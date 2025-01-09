import re
from itertools import chain

def read_file(file_name):
    with open(file_name, "r") as file:
        # Read the entire content of the file
        content = file.readlines()
    return content


def do_mul(commands):
    sum_of_num = 0
    for command in commands:
        # finds the 2 numbers in the command then multiplies them
        numbers = list(re.findall(r"(\d+)", command))
        sum_of_num += int(numbers[0]) * int(numbers[1])
    return sum_of_num


def day_3_part_1():
    content = read_file("day3input.txt")

    # content is a list of each line
    #print(content)
    # findall will make a list of lists from each line, you need chain from iterable to flatten the list
    mul_commands = list(chain.from_iterable(re.findall(r"(mul\(\d+,\d+\))", line) for line in content))

    final_sum = do_mul(mul_commands)
    print(final_sum)


def day_3_part_2():
    content = read_file("day3input.txt")

    # finds all the parts we care about and puts them into a list
    do_commands = list(chain.from_iterable([re.findall(r"(do\(\))|(don't\(\))|(mul\(\d+,\d+\))", line) for line in content]))
    # filters all the empty strings in the list
    do_commands = list(filter(None, chain.from_iterable(do_commands)))

    can_mul = True
    sum_of_mul = 0
    for command in do_commands:
        # acts as an on/off switch for commands
        if command == "do()":
            can_mul = True
        elif command == "don't()":
            can_mul = False
        # if true and is a mul() then do_mul
        if can_mul and re.match(r"(mul\()", command):
            sum_of_mul += do_mul([command])

    print("sum_of_mul: ", sum_of_mul)

