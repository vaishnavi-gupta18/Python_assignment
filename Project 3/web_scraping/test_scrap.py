import unittest
import web_scraping as ws
from web_scraping import *

class Test(unittest.TestCase):
    
    def test__init(self):
        w1 = ws.Person('Radhika Garg', city='Roorkee')
        with self.assertRaises(AttributeError):
            w1.work


    def test_user_check(self):
        with self.assertRaises(ValueError):
            ws.scrap("vaishnavigupta")  

    def  test_user(self):
        self.assertEqual(ws.scrap('ritvik.jain.52206').city,'Roorkee')
        self.assertEqual(ws.scrap('ritvik.jain.52206').name,'Ritvik Jain')
        

if __name__ == '__main__':
    unittest.main()