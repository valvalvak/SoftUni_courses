def palindrome(name, index):
    if name[index] == name[-index - 1]:
        if index >= (len(name) - 1):
            return f"{name} is a palindrome"
        else:
            return palindrome(name, index + 1)
    else:
        return f"{name} is not a palindrome"

# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
# print(palindrome("azobi4amma4iboza", 0))

# import unittest
#
# class Tests(unittest.TestCase):
#    def test(self):
#       func = palindrome
#       res = func("peter", 0)
#       self.assertEqual(res, 'peter is not a palindrome')
#
# if __name__ == "__main__":
#    unittest.main()
