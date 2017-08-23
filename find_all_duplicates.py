
def find_all_duplicates(given_array):
    """
    Given an array of integers the method returns all the duplicate values of the array as a set.
    The values of the array must be between 1 and n where n is the length of the array.
    :param given_array: An array of values from 1 to n (n is the length of the array).
    :return: A set of all the duplicate values.
    """

    # create an empty set
    result = set()

    # For every element get the value. Make that value positive, subtract one and use it as index.
    # If the value of the element at position index is negative, add the value of the current element to result set,
    # else make the value of the element at the position 'index' negative.
    for i in range(len(given_array)):
        index = abs(given_array[i]) - 1
        if given_array[index] < 0:
            result.add(abs(given_array[i]))
        else:
            given_array[index] = -given_array[index]

    return result



if __name__ == '__main__':
    given_array = [1, 2, 11, 3, 2, 5, 5, 4, 3, 7, 3, 9, 1, 9, 11]

    print('The array\n', given_array)
    print('has the following duplicates :\n', find_all_duplicates(given_array))
