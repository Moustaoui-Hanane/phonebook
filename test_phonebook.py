import unittest
from phoneBook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_phone(self):
        phonebook = PhoneBook()
        #add name = Bob + number = 12345
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    #define new test case looking for missing names
    def test_missing_names(self):
        phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

