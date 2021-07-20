class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        """ Convert a Roman numeral to an integer. """
        if not isinstance(value, str):
            return "wrong type"
            # raise TypeError("expected string, got type(value))
        value = value.upper()
        nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        num = 0
        for i in range(len(value)):
            current_value = nums[value[i]]
            # If the next place holds a larger number, this value is negative
            if i + 1 < len(value) and nums[value[i + 1]] > current_value:
                num -= current_value
            else:
                num += current_value
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except:
            return "wrong type"

# first_num = Integer(10)
# second_num = Integer.from_roman("IV")
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))


# def int_to_roman(input):
#     """ Convert an integer to a Roman numeral. """
#
#     if not isinstance(input, type(1)):
#         raise TypeError, "expected integer, got %s" % type(input)
#     if not 0 < input < 4000:
#         raise ValueError, "Argument must be between 1 and 3999"
#     ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
#     nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
#     result = []
#     for i in range(len(ints)):
#         count = int(input / ints[i])
#         result.append(nums[i] * count)
#         input -= ints[i] * count
#     return ''.join(result)
#
# def roman_to_int(input):
#     """ Convert a Roman numeral to an integer. """
#
#     """
#     if not isinstance(input, type("")):
#         raise TypeError, "expected string, got %s" % type(input)
#     input = input.upper(  )
#     nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#     sum = 0
#     for i in range(len(input)):
#         try:
#             value = nums[input[i]]
#             # If the next place holds a larger number, this value is negative
#             if i+1 < len(input) and nums[input[i+1]] > value:
#                 sum -= value
#             else: sum += value
#         except KeyError:
#             raise ValueError, 'input is not a valid Roman numeral: %s' % input
#     # easiest test for validity...
#     if int_to_roman(sum) == input:
#         return sum
#     else:
#         raise ValueError, 'input is not a valid Roman numeral: %s' % input
# def roman_to_int(input):
#     try: input = input.upper(  )
#     except AttributeError:
#         raise TypeError, 'expected string, got %s' % type(input)
#     # map of (numeral, value, maxcount) tuples
#     roman_numeral_map = (('M', 1000, 3), ('CM', 900, 1),
#         ('D', 500, 1), ('CD', 400, 1),
#         ('C', 100, 3), ('XC', 90, 1),
#         ('L', 50, 1), ('XL', 40, 1),
#         ('X', 10, 3), ('IX', 9, 1),
#         ('V', 5, 1), ('IV', 4, 1), ('I', 1, 3))
#     result, index = 0, 0
#     for numeral, value, maxcount in roman_numeral_map:
#         count = 0
#         while input[index: index+len(numeral)] == numeral:
#             count += 1 # how many of this numeral we have
#             if count > maxcount:
#                 raise ValueError, \
#                     'input is not a valid roman numeral: %s' % input
#             result += value
#             index += len(numeral)
#     if index < len(input): # There are characters unaccounted for
#         raise ValueError, 'input is not a valid roman numeral: %s'%input
#     return result
# roman = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
#             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
#         }
#         i = 0
#         num = 0
#         while i < len(value):
#             if i + 1 < len(value) and value[i:i + 2] in roman:
#                 num += roman[value[i:i + 2]]
#                 i += 2
#             else:
#                 # print(i)
#                 num += roman[value[i]]
#                 i += 1
#         return cls(num)


####
# # unittests
# import unittest
#
#
# class IntegerTests(unittest.TestCase):
#     def test_basic_init(self):
#         integer = Integer(1)
#         self.assertEqual(integer.value, 1)
#
#     def test_from_float_success(self):
#         integer = Integer.from_float(2.5)
#         self.assertEqual(integer.value, 2)
#
#     def test_from_float_wrong_type(self):
#         result = Integer.from_float("2.5")
#         self.assertEqual(result, "value is not a float")
#
#     def test_from_roman(self):
#         integer = Integer.from_roman("XIX")
#         self.assertEqual(integer.value, 19)
#
#     def test_from_string_success(self):
#         integer = Integer.from_string("10")
#         self.assertEqual(integer.value, 10)
#
#     def test_from_string_wrong_type(self):
#         result = Integer.from_string(1.5)
#         self.assertEqual(result, "wrong type")
#
#
# if __name__ == "__main__":
#     unittest.main()
