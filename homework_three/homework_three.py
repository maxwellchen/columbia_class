def question_1(name: str) -> str:
    """
    Returns "Hello my name is" plus the name
    :param name: a string that indicates the name
    :return: A string of "Hello my name is" plus name
    """
    return "Hello my name is " + name


def question_2(name: str) -> str:
    """
    Capitalize name and add it to "Hello my name is "
    :param name: a string that indicates the name
    :return: A string of "Hello my name is" plus the capitalization of name
    """
    name = name.capitalize()
    return "Hello my name is " + name


def question_3(name: str) -> str:
    """
    Returns "Hello my name is" plus the first name
    :param name: a string that indicates the name
    :return: A string of "Hello my name is" plus the first name
    """
    return "MY first name is " + name


def question_4(name: str) -> str:
    """
    Capitalize first name and add it to "Hello my name is "
    :param name: a string that indicates the name
    :return: A string of "Hello my name is" plus the capitalization of first name
    """
    name = name.capitalize()
    return "My first name is " + name


def question_5(first_name: str, last_name: str) -> str:
    """
    takes in first and last name and return them
    :param first_name: a string that indicates first name
    :param last_name: a string that indicates last name
    :return: a string of first and last name
    """
    return "My full name is " + first_name + " " + last_name


def question_6(first_name: str, last_name: str) -> str:
    """
    takes in first and last name and return the capitalized first and last name
    :param first_name: a string that indicates first name
    :param last_name: a string that indicates last name
    :return: a string of first and last name that are both capitalized
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return "My full name is " + first_name + " " + last_name


def question_7(string: str) -> list:
    """
    find indicies that are lowercase in a string
    :param string: a string that may have upper and lower cases
    :return: indices of lowercases in the string
    """
    result = []
    for i, s in enumerate(string):
        if s.islower():
            result.append(i)
    return result


def question_8(string: str) -> list:
    """
    find indicies that are uppercase in a string
    :param string: a string that may have upper and lower cases
    :return: indices of uppercases in the string
    """
    result = []
    for i, s in enumerate(string):
        if s.isupper():
            result.append(i)
    return result


def question_9(string: str) -> list:
    """
    find indicies that are whitespace in a string
    :param string: a string that may have whitespaces
    :return: indices of whitespaces in the string
    """
    result = []
    for i, s in enumerate(string):
        if s.isspace():
            result.append(i)
    return result


def question_10(string: str) -> int:
    """
    find the number of distinct words in the string
    :param string: a string
    :return: number of distinct words
    """
    word_list = list(string.split())
    result = []
    for i in word_list:
        if i not in result:
            result.append(i)
    return len(result)


def question_11(string: str) -> int:
    """
    finds the number of integers in the string
    :param string: a string that may contain integers
    :return: an int that represents the number of integers in the string
    """
    listing = list(string)
    counter = 0
    for i in listing:
        if i.isdigit():
            counter += 1
    return counter


def question_12(s1: str, s2: str) -> str:
    """
    concatenates the two strings
    :param s1: a string
    :param s2: a string
    :return: concatenation of two strings
    """
    return s1 + " " + s2


def question_13(s1: str, s2: str) -> str:
    """
    concatenates the two capitalized strings
    :param s1: a string
    :param s2: a string
    :return: concatenation of two capitalized strings
    """
    s1 = s1.capitalize()
    s2 = s2.capitalize()
    return s1 + " " + s2


def question_14(string: str) -> str:
    """
    replaces spaces with _ in a string
    :param string: a string that may have spaces
    :return: a string with spaces replaced with _
    """
    string = string.replace(" ", "_")
    return string


def question_15(string: list) -> str:
    """
    find the longest word in a list of strings
    :param string: a list of strings
    :return: a string that is the longest word in the list
    """
    max_len = 0
    max_word = ""
    for word in string:
        if len(word) > len(max_word):
            max_word = word
    return max_word


def question_16(string: list) -> str:
    """
    find the shortest word in a list of strings
    :param string: a list of strings
    :return: a string that is the shortest word in the list
    """
    min_word = string[0]
    min_len = len(min_word)
    for word in string:
        if min_len > len(word):
            min_len = len(word)
            min_word = word
    return min_word


def question_17(string: list) -> float:
    """
    find the average length of words in the list of strings
    :param string: a list of strings
    :return: a float, the average length of words in the string
    """
    lengths = [len(i) for i in string]
    avg = float(sum(lengths))/len(lengths)
    return avg


def question_18(string: list) -> float:
    """
    find the median word length in a list of strings
    :param string: a list of strings
    :return: a float, the median word length from the list of strings
    """
    sorted_list = sorted(string, key=len)

    if len(sorted_list) %2 != 0:
        median = len(sorted_list[int(len(sorted_list) / 2)])
    else:
        median = (len(sorted_list[int(len(sorted_list)/2)]) + len(sorted_list[int(len(sorted_list)/2-1)]))/2
    return median


def question_19(numbers: list) -> list:
    """
    find the even numbers in a list of nunmbers
    :param numbers: a list of numbers
    :return: even numbers in the list
    """
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def question_20(numbers: list) -> list:
    """
    find the odd numbers in a list of nunmbers
    :param numbers: a list of numbers
    :return: odd numbers in the list
    """
    odd_list = []
    for i in numbers:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


def question_21(numbers: list) -> list:
    """
    find the three largest numbers in a list of numbers
    :param numbers: a list of numbers
    :return: a list of three largest numbers
    """
    large_list = []
    numbers.sort()
    if len(numbers) >= 3:
        large_list.append(numbers[-1])
        large_list.append(numbers[-2])
        large_list.append(numbers[-3])
    return large_list


def question_22(numbers: list) -> list:
    """
    find the three smallest numbers in a list of numbers
    :param numbers: a list of numbers
    :return: a list of three smallest numbers
    """
    small_list = []
    numbers.sort()
    if len(numbers) >= 3:
        small_list.append(numbers[0])
        small_list.append(numbers[1])
        small_list.append(numbers[2])
    return small_list


def question_23(numbers: list) -> float:
    """
    find the mean of a list of numbers
    :param numbers: a list of numbers
    :return: the mean of a list of numbers
    """
    return sum(numbers)/len(numbers)


def question_24(numbers: list):
    """
    find the mode of a list of numbers
    :param numbers: a list of numbers
    :return: the mode of a list of numbers
    """
    return max(numbers, key=numbers.count)


def question_25(numbers: list) -> list:
    """
    reverse the list
    :param numbers: a list of numbers
    :return: returns the list of number in reverse
    """
    numbers.reverse()
    return numbers


def question_26(numbers: list) -> list:
    """
    calculates the cumulative sum of a list of numbers
    :param numbers: a list of numbers
    :return: cumulative sum of the list
    """
    sums = [sum(numbers[:i]) for i in range(1, len(numbers)+1)]
    return sums


def question_27(numbers: list) -> list:
    """
    find the differences between each number
    and returns a list
    :param numbers: a list of numbers
    :return: a list with differences of the number
    """
    new_list = []
    i = 0
    while i + 1 < len(numbers):
        new_list.append(numbers[i+1] - numbers[i])
        i += 1
    return new_list


def question_28(n: int) -> int:
    """
    a recursive function with bases of the following:
    F[0] = 0
    F[1] = 1
    F[2] = 1
    and the F[n] = F[n-1] + F[n-3]
    :param n: an integer that indicates the index
    :return: an integer, F[n]
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return question_28(n-1) + question_28(n-3)


def question_29(n: int) -> int:
    """
    a recursive function with base case of F[0] = 1
    F[n] = F[n-1] * F[n-2] * F[n-3] *... * 2 * 1
    :param n: an integer that indicates the index
    :return: an integer, F[n]
    """
    if n == 0 or n == 1:
        return 1
    else:
        return (n-1) * question_29(n-1)


def question_30(n: int) -> int:
    """
    a recursive function with base case of F[0] = 1
    F[n] = 2^F[n-1] * 2^F[n-2] * 2^F[n-3] ... * 2^2 * 2^1 * 2^0
    :param n: an integer
    :return: an integer, F[n]
    """
    if n == 0:
        return 1
    else:
        return 2**(n-1) * question_30(n-1)

