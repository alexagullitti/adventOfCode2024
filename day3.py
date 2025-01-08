import re

def do_mul(commands):
    sum_of_num = 0
    for command in commands:
        print(command)
        numbers = list(re.findall(r"(\d+)", command))
        #testing = int(command[1])
        print(numbers)
        sum_of_num += int(numbers[0]) * int(numbers[1])

    print(sum_of_num)
#28546082

def day_3_part_1():
    test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    with open("day3input.txt", "r") as file:
        # Read the entire content of the file
        content = file.readlines()

    #content = test_string
    print(content)
    mul_commands = list(re.findall(r"(mul\(\d+,\d+\))", line) for line in content)
    print(mul_commands)

    do_mul(mul_commands[0])


