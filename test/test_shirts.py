import unittest
from app.shirt import Shirts
import schema
from settings import TESTDBPATH
import sqlite3

schema.schema(TESTDBPATH)
Shirts.dbpath = TESTDBPATH
test_shirt = None
#python3 -m unittest discover test 

class TestAccount(unittest.TestCase):

    def setUp(self):
        # runs before every test case
        global test_shirt
        with sqlite3.connect(Shirts.dbpath) as conn:
            cur = conn.cursor()
            SQL = f"DELETE FROM {Shirts.tablename}"
            cur.execute(SQL)
            SQL = f"""INSERT INTO {Shirts.tablename}(style, size, color)  VALUES ("casual", "L", "green")"""
            cur.execute(SQL)
            test_shirt = cur.lastrowid

    def test_dummy(self):
        '''if everything is working correctly this will pass'''
        self.assertTrue(True)

    def test_all(self):
        result = Shirts.all()
        self.assertEqual(len(result), 1, "all func returns list with correct number of elements")
        self.assertIsInstance(result[0], Shirts, "all func returns account object")
        self.assertEqual(result[0].color, "green", "all func populates attributes")
    
    
    def test_from_id(self):
        result = Shirts.from_id(test_shirt)
        self.assertIsInstance(result, Shirts, "from_id returns an instance of an account")
        self.assertEqual(result.size,"L")
        self.assertIsNone(Shirts.from_id(0), "from_id returns None for bad pk")
    
    
    def test_insert(self):
        tester = Shirts(style='athlesiure', size='M', color='red')
        tester.save()
        result = Shirts.all()#using the all fucntion to count rows in DB
        self.assertEqual(len(result), 2, "The first row was the set up the new row was inserted")
        self.assertEqual(result[0].color,"green","all func populates attributes, checking first for row[0] / pk1" )
        self.assertEqual(result[1].color,"red","all func populates attributes, checking email for row[1] / pk2" )


    ##Note: Ran out of time to create a test for del & update##
    does not work
    # def test_delete(self): 
    #     tester = Shirts(style='athlesiure', size='M', color='red')
    #     tester.save()
    #     tester.delete()
    #     result = Shirts.all()
    #     self.assertEqual(len(result),1,"should be none added and deleted new row")

