
def find_all_duplicates(given_array):

    result = set()

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
