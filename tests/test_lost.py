import unittest
from app.models import Lost  
Lost = Lost

class LostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Lost class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_lost = Lost()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_lost,Lost))