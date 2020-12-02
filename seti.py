def decimal_to_binary(decimal_number):
    binary_list = []
    while decimal_number > 0:
        element = decimal_number % 2
        binary_list.insert(0, element)
        decimal_number //= 2
    return binary_list

print(decimal_to_binary(20))

def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    pass


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
