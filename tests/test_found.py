import unittest
from app.models import Found  
Found = Found

class LostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Found class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_found = Found()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_found,Found))