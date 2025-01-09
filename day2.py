
#day 2 part 1

# #attempt 1 did not work
# def find_safe_reports2():
#     # Open the file in read mode
#     file = open("test.txt", "r")
#     # Read the entire content of the file
#     content = file.readlines()
#     list_of_lists = []
#
#     for line in content:
#         numbers = line.split()
#         numbers = list(map(int, numbers))
#         list_of_lists.append(numbers)
#
#     #print(list_of_lists)
#     line_count = 0
#     safe_count = 0
#
#     for line in list_of_lists:
#         print(line)
#         trend = line[0] - line[1]
#         print(trend)
#         for i in range(len(line)-1):
#             #make a copy
#             line_copy = line.copy()
#
#             #find the difference
#             difference = line_copy[i] - line_copy[i+1]
#             print(difference)
#
#             level_removed = False
#
#             if trend == 0:
#                 if level_removed:
#                     safe_count += 1
#                     break
#                 line_copy.pop(i)
#                 level_removed = True
#
#             #if trending negative
#             if trend > 0:
#                 if difference > 3 or difference <= 0:
#                     if level_removed:
#                         break
#                     line_copy.pop(i)
#                     level_removed = True
#
#             #if trending positive
#             if trend < 0:
#                 if difference < -3 or difference >= 0:
#                     if level_removed:
#                         break
#                     line_copy.pop(i)
#                     level_removed = True
#             print(line_copy)
#         else:
#             print("safe")
#             safe_count += 1
#         line_count += 1
#
#     print(safe_count)
#     print(line_count)

def format_file_lines(file_name):
    # Open the file in read mode
    file = open(file_name, "r")
    # Read the entire content of the file
    content = file.readlines()
    list_of_lists = []

    for line in content:
        numbers = line.split()
        numbers = list(map(int, numbers))
        list_of_lists.append(numbers)

    return list_of_lists

def find_safe_reports():
    # Open the file in read mode
    with open("day2Input.txt", "r") as file:
        # Read the entire content of the file
        content = file.readlines()

    # for each line in the content convert the value to a string and then put in a list
    list_of_lists = [list(map(int, line.split())) for line in content]
    # print(list_of_lists)

    test_list = [[7, 10, 12, 16, 17, 18, 21], [1, 2, 3, 4, 5]]
    line_count = 0
    safe_count = 0

    for line in list_of_lists:
        # see if the line is increasing, then do for each index in line, returns true or false to is_increaseing
        is_increasing = all(line[i] < line[i + 1] and line[i + 1] - line[i] <= 3 for i in range(len(line) - 1))
        is_decreasing = all(line[i] > line[i + 1] and line[i] - line[i + 1] <= 3 for i in range(len(line) - 1))

        if is_increasing or is_decreasing:
            safe_count += 1
        line_count += 1

    print(safe_count)
    print(line_count)


def day_2_part_2():
    # Open the file in read mode
    with open("day2Input.txt", "r") as file:
        # Read the entire content of the file
        content = file.readlines()

    # for each line in the content convert the value to a string and then put in a list
    list_of_lists = [list(map(int, line.split())) for line in content]
    # print(list_of_lists)

    test_list = [[7, 10, 12, 16, 17, 18, 21], [1, 2, 3, 4, 5]]
    line_count = 0
    safe_count = 0

    for line in list_of_lists:
        # for each index in the line it will remove it and see if that passes, if it passes it will break out of the
        # loop and add 1 to safe count
        for i in range(len(line)):
            modified_line = line[:i] + line[i + 1:]  # Remove the i-th index from the line
            is_increasing = all(
                modified_line[j] < modified_line[j + 1] and modified_line[j + 1] - modified_line[j] <= 3 for j in
                range(len(modified_line) - 1))
            is_decreasing = all(
                modified_line[j] > modified_line[j + 1] and modified_line[j] - modified_line[j + 1] <= 3 for j in
                range(len(modified_line) - 1))

            if is_increasing or is_decreasing:
                safe_count += 1
                break
        line_count += 1

    print(safe_count)
    print(line_count)
