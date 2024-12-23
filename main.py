# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
