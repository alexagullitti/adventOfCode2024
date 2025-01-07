# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#def read_file()

def find_sum(name):
    # Open the file in read mode
    file = open("inputList.txt", "r")
    # Read the entire content of the file
    content = file.read()
    temp_list = content.split('\n')

    column1_list = []
    column2_list = []

    for row in temp_list:
        # Split the row into individual numbers
        numbers = row.split()
        # Append the first number to column1_numbers list
        column1_list.append(int(numbers[0]))
        # Append the second number to column2_numbers list
        column2_list.append(int(numbers[1]))

    #sort lists
    column1_list.sort()
    column2_list.sort()

    # Print the two lists
    print("Column 1 numbers:", column1_list)
    print("Column 2 numbers:", column2_list)

    sum_of_differences = 0

    for i in range(len(column1_list)):
        sum_of_differences += abs(column1_list[i] - column2_list[i])

    # Print the content
    print(sum_of_differences)
    # Close the file
    file.close()


def getOrderedLists():
    # Open the file in read mode
    file = open("inputList.txt", "r")
    # Read the entire content of the file
    content = file.read()
    temp_list = content.split('\n')

    column1_list = []
    column2_list = []

    for row in temp_list:
        # Split the row into individual numbers
        numbers = row.split()
        # Append the first number to column1_numbers list
        column1_list.append(int(numbers[0]))
        # Append the second number to column2_numbers list
        column2_list.append(int(numbers[1]))

    # sort lists
    column1_list.sort()
    column2_list.sort()

    # Print the two lists
    print("Column 1 numbers:", column1_list)
    print("Column 2 numbers:", column2_list)
    return column1_list, column2_list

#day 1 part 2
def find_similarity_count():
    list1, list2 = getOrderedLists()
    similarity_score = 0

    for number in list1:
        occurrences = list2.count(number)
        similarity_score += number * occurrences

    print("similarity_score: ", similarity_score)


#day 2 part 1
def find_safe_reports():
    # Open the file in read mode
    file = open("day2Input.txt", "r")
    # Read the entire content of the file
    content = file.readlines()
    list_of_lists = []

    for line in content:
        numbers = line.split()
        numbers = list(map(int, numbers))
        list_of_lists.append(numbers)

    #print(list_of_lists)

    test_list = [[7, 10, 12, 16, 17, 18, 21],[1,2,3,4,5]]
    line_count = 0
    safe_count = 0

    for line in list_of_lists:
        print(line)
        trend = line[0] - line[1]
        print(trend)
        for i in range(len(line)-1):
            #print(i)
            difference = line[i] - line[i+1]
            print(difference)
            if trend == 0:
                break
            #if trending negative
            if trend > 0:
                if difference > 3 or difference <= 0:
                    break

            #if trending positive
            if trend < 0:
                if difference < -3 or difference >= 0:
                    break
        else:
            print("safe")
            safe_count += 1
        line_count += 1

    print(safe_count)
    print(line_count)

def find_safe_reports2():
    # Open the file in read mode
    file = open("test.txt", "r")
    # Read the entire content of the file
    content = file.readlines()
    list_of_lists = []

    for line in content:
        numbers = line.split()
        numbers = list(map(int, numbers))
        list_of_lists.append(numbers)

    #print(list_of_lists)
    line_count = 0
    safe_count = 0

    for line in list_of_lists:
        print(line)
        trend = line[0] - line[1]
        print(trend)
        for i in range(len(line)-1):
            #make a copy
            line_copy = line.copy()

            #find the difference
            difference = line_copy[i] - line_copy[i+1]
            print(difference)


            level_removed = False

            if trend == 0:
                if level_removed:
                    break
                line_copy.pop(i)
                level_removed = True

            #if trending negative
            if trend > 0:
                if difference > 3 or difference <= 0:
                    if level_removed:
                        break
                    line_copy.pop(i)
                    level_removed = True

            #if trending positive
            if trend < 0:
                if difference < -3 or difference >= 0:
                    if level_removed:
                        break
                    line_copy.pop(i)
                    level_removed = True
            print(line_copy)
        else:
            print("safe")
            safe_count += 1
        line_count += 1

    print(safe_count)
    print(line_count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_safe_reports2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
