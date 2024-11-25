import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEquals("foo".upper(), "FOO")

    def test_lower(self):
        self.assertEquals("foo".upper(), "FOO")



if __name__ == '__main__':
    unittest.main()