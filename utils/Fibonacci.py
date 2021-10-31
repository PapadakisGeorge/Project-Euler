def generate_fibonacci_number(first_seed, second_seed, term):
    if term == 1:
        fibonacci_number = first_seed
    elif term == 2:
        fibonacci_number = second_seed
    else:
        fibonacci_number = generate_fibonacci_number(first_seed, second_seed, term - 2) + \
                           generate_fibonacci_number(first_seed, second_seed, term - 1)
    return fibonacci_number

