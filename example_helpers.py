import os
import contextlib


def suppress_stdout(func):
    def wrapper(*a, **ka):
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stdout(devnull):
                return func(*a, **ka)
    return wrapper


def check_combo(input_op, input_1, input_2):
    """
    A function to print the various results of different arithmetic operator
    input combinations on two input types.
    Args:
        input_op: A string representation of a input type
        input_1: A numeric type to test
        input_2: A numeric type to test
    """
    # Note we dont raise exceptions as we want to see and print the exception
    # later, normally this would be bad
    # practice.
    import numbers
    if type(input_1) is type(input_2):
        print("Warning: input types are not different\
             this test will be very dull")
    for i in (input_1, input_2):
        if not isinstance(i, numbers.Number):
            print("Warning, datatype is not numeric")

    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
        '//': operator.floordiv,
    }

    input_combos = [
        (input_1, input_1),
        (input_2, input_2),
        (input_1, input_2),
        (input_2, input_1)
        ]
    for i1, i2 in input_combos:
        try:
            my_tmp = ops[input_op](i1, i2)
            my_tmp_type = f"type {type(my_tmp)}"
        except Exception as e:
            exception_cause = f"{ e.__class__ }"
            my_tmp_type = f" { exception_cause[8:-2]}: {e}"
        print(f"type {type(i1)} {input_op} type {type(i2)}, \
        yields {my_tmp_type}")


def check_fizzbuzz(input_fizzbuzz, fizzbuzz_size=20):
    correct = True
    for i in range(0, len(input_fizzbuzz)):
        if input_fizzbuzz[i] != fizzbuzz(i+1):
            print(f"You have an error with fizzbuzz element {i}")
            correct = False
            break
    if len(input_fizzbuzz) == fizzbuzz_size and correct:
        print(f"Success the first {fizzbuzz_size} numbers \
        fizzbuzzed are \n {input_fizzbuzz}")
    elif correct:
        print(f'You dont have all {fizzbuzz_size} \
        elements you only submitted {len(input_fizzbuzz)}')


def fizzbuzz(number_to_fizzbuzz):
    # check if the modulus of the number is 0 if it is its a multiple!
    is_number_fizz = number_to_fizzbuzz % 3 == 0
    is_number_buzz = number_to_fizzbuzz % 5 == 0
    # if both multiples then we need to fizzbuzz
    is_number_fizzbuzz = is_number_fizz and is_number_buzz

    # Check fizzbuzz first
    # Then use two elif conditionals to check fizz then buzz
    # Finally use else to print the number if none of the conditionals pass.

    if (is_number_fizzbuzz):
        ret = 'fizzbuzz'
    elif (is_number_fizz):
        ret = 'fizz'
    elif (is_number_buzz):
        ret = 'buzz'
    else:
        ret = number_to_fizzbuzz

    return ret


def check_fizz(input_fizz, fizz_size):
    fizzed = [i if i % 3 else 'fizz' for i in range(1, 101)]
    correct = True
    for i in range(0, len(input_fizz)):
        if input_fizz[i] != fizzed[i]:
            print(f"You have an error with fizzed element {i}")
            correct = False
            break
    if len(input_fizz) == fizz_size and correct:
        print(f"Success the first {fizz_size} \
            numbers fizzed are \n {input_fizz}")
    elif correct:
        print(f'You dont have all {fizz_size}\
             elements you only submitted {len(input_fizz)}')


def check_buzz(input_buzz, buzz_size):
    buzzed = [i if i % 5 else 'buzz' for i in range(1, 101)]
    correct = True
    for i in range(0, len(input_buzz)):
        if input_buzz[i] != buzzed[i]:
            print(f"You have an error with buzzed element {i}")
            correct = False
            break
    if len(input_buzz) == buzz_size and correct:
        print(f"Success the first {buzz_size}\
             numbers buzzed are \n {input_buzz}")
    elif correct:
        print(f'You dont have all {buzz_size}\
             elements you only submitted {len(input_buzz)}')


def check_1_2_boo(fn_to_check):
    fn_no_stdout = suppress_stdout(fn_to_check)

    out1 = fn_no_stdout(1)
    out2 = fn_no_stdout(2)
    out3 = fn_no_stdout(3)

    message = "Your function:\n"
    if out1 != "1":
        message += "Produces the wrong output for input of 1\n"
    else:
        message += "Is correct for input of 1\n"
    if out2 != "2":
        message += "Produces the wrong output for input of 2\n"
    else:
        message += "Is correct for input of 1\n"
    if out3 != "boo":
        message += "Produces the wrong output for input that isn't 1 or 2\n"
    else:
        message += "Is correct for inputs that are not 1 or 2\n"

    print(message)


def check_functions(fizz_fun, buzz_fun, fizzbuzz_fun):
    numbers_to_check = [1, 100, 3, 9, 5, 10, 15, 45]
    number_failed = 0
    # Test Fizz
    for test_num in numbers_to_check:
        correct_ans = fizzbuzz(test_num) == "fizz"
        if fizz_fun(test_num) != correct_ans:
            print("check_fizz failed with input:", test_num)
            number_failed += 1
    # Test Buzz
    for test_num in numbers_to_check:
        correct_ans = fizzbuzz(test_num) == "buzz"
        if buzz_fun(test_num) != correct_ans:
            print("check_buzz failed with input:", test_num)
            number_failed += 1
    # Test Fizzbuzz
    for test_num in numbers_to_check:
        correct_ans = fizzbuzz(test_num) == "fizzbuzz"
        if fizzbuzz_fun(test_num) != correct_ans:
            print("check_fizzbuzz failed with input:", test_num)
            number_failed += 1

    print(f'Tests Complete: {24-number_failed} Tests Passed,\
         {number_failed} Tests Failed')


def keyword_check_fizz(
        number_to_check: int,
        fizz_num: int = 3,
        buzz_num: int = 5) -> bool:
    """ This function checks if a number is fizz but not buzz,
    i.e. number is a multiple of 3 but not 5, and returns True if it is.
    Parameters
    ----------
    number_to_check : int
        input integer to check for fizz
    fizz_num : int
        input integer to use for fizz check
    buzz_num : int
        input integer to use for buzz check

    Returns
    -------
    bool
        True if number passes fizz check but not buzz check.
    """
    if number_to_check % fizz_num == 0:
        output = True
    else:
        output = False

    if number_to_check % buzz_num == 0:
        output = False

    return output


def keyword_check_buzz(
        number_to_check: int,
        fizz_num: int = 3,
        buzz_num: int = 5) -> bool:
    """ This function checks if a number is fizz but not buzz, i.e. number is
    a multiple of 3 but not 5, and returns True if it is.
    Parameters
    ----------
    number_to_check : int
        input integer to check for fizz
    fizz_num : int
        input integer to use for fizz check
    buzz_num : int
        input integer to use for buzz check

    Returns
    -------
    bool
        True if number passes buzz check but not fizz check.
    """
    if number_to_check % buzz_num == 0:
        output = True
    else:
        output = False

    if number_to_check % fizz_num == 0:
        output = False

    return output


def keyword_check_fizzbuzz(
        number_to_check: int,
        fizz_num: int = 3,
        buzz_num: int = 5) -> bool:
    """ This function checks if a number is fizz but not buzz,
    i.e. number is a multiple of 3 but not 5, and returns True if it is.
    Parameters
    ----------
    number_to_check : int
        input integer to check for fizz
    fizz_num : int
        input integer to use for fizz check
    buzz_num : int
        input integer to use for buzz check

    Returns
    -------
    bool
        True if number passes fizz and buzz check.
    """
    if number_to_check % fizz_num == 0:
        output = True
    else:
        output = False

    if number_to_check % buzz_num == 0:
        output = True
    else:
        output = False

    return output


def keyword_fizzbuzz(
        list_to_mutate: list,
        fizz_num: int = 3,
        buzz_num: int = 5,
        fizz_word: str = 'fizz',
        buzz_word: str = 'buzz') -> None:
    """ This function takes a list of numbers and mutates it to replace
    numbers that are multiples of fizz_num with fizz_word, multiples of
    buzz_num with buzz_word, and multiples of fizz_num*buzz_num with
    fizz_word+buzz_word.
    Parameters
    ----------
    list_to_mutate : list
        input list of numbers to mutate
    fizz_num : int
        input integer to use for fizz check
    buzz_num : int
        input integer to use for buzz check

    Returns
    -------
    None
        This function does not return anything,
        but mutates the list_to_mutate in place.
    """
    for i in range(len(list_to_mutate)):
        if keyword_check_fizzbuzz(
                list_to_mutate[i],
                fizz_num=fizz_num,
                buzz_num=buzz_num):
            list_to_mutate[i] = fizz_word + buzz_word
        elif keyword_check_fizz(
                list_to_mutate[i],
                fizz_num=fizz_num,
                buzz_num=buzz_num):
            list_to_mutate[i] = fizz_word
        elif keyword_check_buzz(
                list_to_mutate[i],
                fizz_num=fizz_num,
                buzz_num=buzz_num):
            list_to_mutate[i] = buzz_word


def check_keyword_fizzbuzz(learner_function):
    """ This function checks if a function is
    correct for the keyword_fizzbuzz function.
    Parameters
    ----------
    learner_function : function
        input function to check for correctness

    Returns
    -------
    None
        This function does not return anything, but prints out a message
        indicating if the function is correct or not.
    """
    test_list = [i for i in range(1, 101)]
    correct_list = [i for i in range(1, 101)]
    print("Testing your function with the default values.")
    keyword_fizzbuzz(correct_list)
    learner_function(test_list)
    if test_list == correct_list:
        print("Your function is correct when using the default values.")
    else:
        print("Your function is not correct when using the default values.\
        Please try again.")

    print("Testing your function with different\
         values for fizz_num and buzz_num.")
    test_list = [i for i in range(1, 101)]
    correct_list = [i for i in range(1, 101)]
    keyword_fizzbuzz(correct_list, fizz_num=4, buzz_num=7)
    learner_function(test_list, fizz_num=4, buzz_num=7)
    if test_list == correct_list:
        print("Your function is correct when using different values\
            for fizz_num and buzz_num.")
    else:
        print("Your function is not correct when using different values\
             for fizz_num and buzz_num. Please try again.")

    print("Testing your function with different values\
         for fizz_word and buzz_word.")
    test_list = [i for i in range(1, 101)]
    correct_list = [i for i in range(1, 101)]
    keyword_fizzbuzz(correct_list, fizz_word='whizz', buzz_word='bang')
    learner_function(test_list, fizz_word='whizz', buzz_word='bang')
    if test_list == correct_list:
        print("Your function is correct when using different values\
             for fizz_word and buzz_word.")
    else:
        print("Your function is not correct when using different values\
             for fizz_word and buzz_word. Please try again.")


def check_formatted_lorem():
    # This function checks if the formatted lorem ipsum file is correct.

    # First get the correct formatted lorem ipsum file.
    with open('lorem_ipsum.txt', 'r') as f:
        formatted_lines = []
        for line in f:
            words_in_line = line.split()
            current_line_length = 0
            for word in words_in_line:
                if current_line_length+len(word) < 90:
                    formatted_lines.append(word)
                    formatted_lines.append(" ")
                    current_line_length += 1
                else:
                    formatted_lines.append("\n")
                    formatted_lines.append(word)
                    formatted_lines.append(" ")
                    current_line_length = 0
                current_line_length += len(word)
            # We will always have a trailing space but instead we want a
            # double newline to indicate the end of a paragraph.
            # Instead of removing the trailing space we will just replace the
            # last list element with a double newline.
            formatted_lines[-1] = "\n\n"

    # Now get the learner's formatted lorem ipsum file.
    with open('formatted_lorem_ipsum.txt', 'r') as f:
        learner_lines = f.readlines()

    # Now check if the two files are the same.
    if formatted_lines == learner_lines:
        print("Your formatted lorem ipsum file is correct.")
    else:
        length_error_line = []
        no_space_line = []
        few_space_line = []
        too_many_paragraphs = []
        lines_with_paragraphs = []
        correct_lines_with_paragraphs = []

        for line_num, line in enumerate(learner_lines):
            line_length = len(line)
            spaces_in_line = line.count(" ")
            paragraph_count = line.count("\n\n")

            if line_length > 90:
                length_error_line.append(line_num)
            if spaces_in_line == 0:
                no_space_line.append(line_num)
            elif spaces_in_line < 10:
                few_space_line.append(line_num)
            if paragraph_count > 1:
                too_many_paragraphs.append(line_num)
            elif paragraph_count == 1:
                lines_with_paragraphs.append(line_num)

        for line_num, line in enumerate(formatted_lines):
            paragraph_count = line.count("\n\n")
            if paragraph_count == 1:
                correct_lines_with_paragraphs.append(line_num)

        # Print the errors.
        if len(length_error_line) > 0:
            print(f"The following lines are too long: {length_error_line}")
        if len(no_space_line) > 0:
            print(f"The following lines have no spaces: {no_space_line}")
        if len(few_space_line) > 0:
            print(f"The following lines have too few spaces: {few_space_line}")
        if len(too_many_paragraphs) > 0:
            print(f"The following lines have\
                too many paragraphs: {too_many_paragraphs}")
        if lines_with_paragraphs == correct_lines_with_paragraphs:
            print(f"The following lines\
                have paragraphs: {lines_with_paragraphs}")
