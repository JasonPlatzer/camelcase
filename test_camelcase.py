import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('HelloWorld', camelcase.camel_case('hello world'))

    def test_camelcase_caps(self):
        self.assertEqual('HelloWorld', camelcase.camel_case('Hello World'))

    def test_camelcase_empty(self):
        self.assertEqual('', camelcase.camel_case(''))
    #from https://stackoverflow.com/questions/32359402/comparison-of-multi-line-strings-in-python-unit-test
    def test_camelcase_newline(self):
        self.assertMultiLineEqual('HelloWorld', camelcase.camel_case('hello \\n world'))