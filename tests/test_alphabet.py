#importing sys for accessing modules in different directory
import sys

sys.path.insert(0, '../src')

import unittest

from alphabet import Alphabet

class TestAlphabet(unittest.TestCase):

    def test_get_yaml_files(self):
        
        self.assertEqual(Alphabet.get_yaml_files('../src/Alphabet Dictionaries')[0], 'actor')
        self.assertEqual(Alphabet.get_yaml_files('../src/Alphabet Dictionaries')[1], 'alpha')
        self.assertNotEqual(Alphabet.get_yaml_files('../src/Alphabet Dictionaries')[0], 'actor.yaml')

    def test_convert(self):

        import yaml
        with open("../src/Alphabet Dictionaries/" + "actor" + ".yaml", "r") as f:dictionary = yaml.safe_load(f)
        f.close()
        self.assertEqual(Alphabet.convert('John', dictionary['mydict']), 'JACKEY\nOYSTER\nHALLIARD\nNEPTUNE\n')
        self.assertEqual(Alphabet.convert('John\n', dictionary['mydict']), 'JACKEY\nOYSTER\nHALLIARD\nNEPTUNE\n')
        self.assertEqual(Alphabet.convert('JoHN', dictionary['mydict']), 'JACKEY\nOYSTER\nHALLIARD\nNEPTUNE\n')
        self.assertEqual(Alphabet.convert('John Doe\n', dictionary['mydict']), 'JACKEY\nOYSTER\nHALLIARD\nNEPTUNE\nspace\nDIVER\nOYSTER\nEAGLE\n')

                                         
if __name__ == '__main__':
    unittest.main()
