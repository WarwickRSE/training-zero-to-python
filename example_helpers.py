def check_combo(input_op, input_1, input_2):
    """
    A function to print the various results of different arithmetic operator input combonations on two input types.
    Args:
        input_op: A string representation of a input type
        input_1: A numeric type to test
        input_2: A numeric type to test
    """
    
    # Note we dont raise exceptions as we want to see and print the exception later, normally this would be bad
    # practice.
    import numbers
    if type(input_1) == type(input_2):
        print("Warning: input types are not diffrent this test will be very dull")
    for i in (input_1, input_2):
        if not isinstance(i, numbers.Number):
            print("Warning, datatype is not numeric")

    import operator
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '**': operator.pow,
    '//' : operator.floordiv,
    }


    input_combos = [(input_1, input_1),(input_2, input_2),(input_1, input_2),(input_2, input_1)]
    for i1, i2 in input_combos:
        try:
            my_tmp = ops[input_op](i1, i2)
            my_tmp_type = f"type {type(my_tmp)}"
        except Exception as e:
            exception_cause = f"{ e.__class__ }"
            my_tmp_type = f" { exception_cause[8:-2]}: {e}"
        print(f"type {type(i1)} {input_op} type {type(i2)}, yeilds {my_tmp_type}")