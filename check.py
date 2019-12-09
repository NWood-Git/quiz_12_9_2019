from app.shirt import Shirts
import sqlite3
import os

dirname = os.path.dirname(__file__)
DBPATH = os.path.join(dirname, "app", "shirts.db")

new_shirt = Shirts(style = 'formal', size = 'M', color = 'black')
new_shirt.save()

