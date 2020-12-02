def decimal_to_binary(decimal_number):
    destination_base_list = []
    while decimal_number > 0:
        element = decimal_number % 2
        destination_base_list.insert(0, element)
        decimal_number //= 2
    return destination_base_list


def binary_to_decimal(binary_digits):
    decimal_number = 0
    for i in range(len(binary_digits)):
        decimal_number += binary_digits[i] * 2**(len(binary_digits)-i-1)
    return decimal_number


def decimal_to_base(decimal_number, destination_base):
    destination_base_list = []
    while decimal_number > 0:
        element = decimal_number % destination_base
        destination_base_list.insert(0, element)
        decimal_number //= destination_base
    return destination_base_list


def base_to_decimal(digits, original_base):
    decimal_number = 0
    for i in range(len(digits)):
        decimal_number += digits[i] * original_base**(len(digits)-i-1)
    return decimal_number


print(decimal_to_binary(20))
print(binary_to_decimal([1, 0, 1, 0, 0]))
print(decimal_to_base(20, 8))
print(base_to_decimal([2, 4], 8))


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
