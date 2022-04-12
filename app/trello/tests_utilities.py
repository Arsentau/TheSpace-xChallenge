from unicodedata import category
from unittest import result
from django.test import TestCase
from . import utilities
from exceptions import appExceptions
import re

class Test_utilities(TestCase):
    
    def test_invalid_name(self):
        name = "This is a very very long tittle that shall not pass"
        with self.assertRaisesMessage(appExceptions.ValidationError, "This is a very very long tittle that shall not pass"):
            utilities.title_validator(name, 20)
    
    def test_valid_name(self):
        result = None
        name = "This is valid"
        result = utilities.title_validator(name, 20)
        self.assertEqual(result, None)
            
    def test_random_title_generator(self):
        result = utilities.random_title_generator("bug", 5)
        x = bool(re.search("^(bug-)[a-zA-Z]*-[0-9]*", result))
        self.assertTrue(x)

    def test_invalid_categoty(self):
        category = "Invalid"
        categories = [ "Mantainance", "Research", "Test"]
        with self.assertRaisesMessage(appExceptions.ValidationError, 'The category: Invalid is not valid'):
            utilities.categoty_validator(categories, category)

    def test_valid_categoty(self):
        result = None
        category = "Research"
        categories = [ "Mantainance", "Research", "Test"]
        result = utilities.categoty_validator(categories, category)
        self.assertEqual(result, None)