import unittest
from item import Item


class Food(unittest.TestCase):
    def test_size(self):
        self.sizing=size('large')

    def test_item(self):
        self.foodItemName=FoodItem('burger')

class Order(unittest.TestCase):
    def test_size(self):
        self.detail=OrderDetail('quanity3')

class ItemTest(unittest.TestCase): 
    def setUp(self):
        self.item=item(1, 'item1', 30.00)
    
    def test_string(self):
        self.assertEqual(str(self.item), self.itme.itemname)
    
    def test_item(self):
        self.foodItemName=FoodItem('large')

class Food(unittest.TestCase):
    def setUp(self):
        self.food=Food('burger')
    
    
