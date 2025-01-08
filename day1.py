
#day 1 part 1
def find_sum():
    # open the file in read mode
    file = open("inputList.txt", "r")
    # read the entire content of the file
    content = file.read()
    temp_list = content.split('\n')

    column1_list = []
    column2_list = []

    for row in temp_list:
        # split the row into individual numbers
        numbers = row.split()
        # append the first number to column1_numbers list
        column1_list.append(int(numbers[0]))
        # append the second number to column2_numbers list
        column2_list.append(int(numbers[1]))

    #sort lists
    column1_list.sort()
    column2_list.sort()

    # print the two lists
    print("Column 1 numbers:", column1_list)
    print("Column 2 numbers:", column2_list)

    sum_of_differences = 0

    for i in range(len(column1_list)):
        sum_of_differences += abs(column1_list[i] - column2_list[i])

    # Print the content
    print(sum_of_differences)
    # Close the file
    file.close()


def get_ordered_lists():
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
    list1, list2 = get_ordered_lists()
    similarity_score = 0

    for number in list1:
        occurrences = list2.count(number)
        similarity_score += number * occurrences

    print("similarity_score: ", similarity_score)

