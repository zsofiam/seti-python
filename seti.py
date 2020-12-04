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


def digits_as_string(digits, base):
    if base > 16:
        raise ValueError("Base cannot be greater than 16")
    string_representation_of_digits = ""
    for i in range(len(digits)):
        if digits[i] > (base-1):
            raise ValueError("Digit cannot be greater than base")
        else:
            if digits[i] > 9:
                character = change_digit_to_letter(digits[i])
            else:
                character = str(digits[i])
        string_representation_of_digits += character
    return string_representation_of_digits


def change_digit_to_letter(digit):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    letter = letters[digit-10]
    return letter


def convert_base(original_digits, original_base, destination_base):
    decimal_number = base_to_decimal(original_digits, original_base)
    destination_base_number = decimal_to_base(decimal_number, destination_base)
    return destination_base_number


def convert_base_advanced(original_digits, original_base, destination_base):
    destination_base_number = 0
    
    return destination_base_number


print(decimal_to_binary(20))
print(binary_to_decimal([1, 0, 1, 0, 0]))
print(decimal_to_base(20, 8))
print(base_to_decimal([2, 4], 8))
print(digits_as_string([1, 2, 3, 4], 8))
print(digits_as_string([2, 15, 9, 11], 16))
print(convert_base([1, 1, 2, 0], 3, 2))