import sqlite3
import os
from settings import DBPATH


class Shirts:
    tablename = 'shirts'
    dbpath = DBPATH

    def __init__(self, **kwargs):
        '''initializes the the class shrits'''
        self.id = kwargs.get('id')
        self.style = kwargs.get('style')
        self.size = kwargs.get('size')
        self.color = kwargs.get('color')

    def save(self):
        '''if the class instance is already in the db
        it calls update to update the instance,
        if it is not in the db it creates the instance via the insert funct'''
        if self.id is None:
            self.insert()
        else:
            self.update()
    
    def insert(self):
        '''this inserts the class instance into the database'''
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            SQL = f"""INSERT INTO {self.tablename}(style, size, color)
                    VALUES(:style, :size, :color)"""
            cur.execute(SQL, {'style':self.style, 'size':self.size, 'color':self.color})

    def update(self):#no test yet
        '''this updates an existing class instance in the database'''
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
        SQL = f"""UPDATE {self.tablename} SET style=:style, size=:size, color=:color WHERE id=:id"""
        cur.execute(SQL, {'id':self.id, 'style':self.style, 'color':self.color})

    def delete(self):#no test yet
        '''deletes an instance from the shirts table in the database'''
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            SQL = f"DELETE FROM {self.tablename} WHERE id=:id;"
            cur.execute(SQL, {'id':self.id})
            self.id = None
    
    @classmethod
    def all(cls):
        SQL = f"SELECT * FROM {cls.tablename};"
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(SQL)
            rows = cur.fetchall()
            result = [cls(**row) for row in rows]
            return result

    @classmethod
    def from_id(cls,id):
        SQL = f"SELECT * FROM {cls.tablename} WHERE id=:id;"
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(SQL, {'id':id})
            row = cur.fetchone()
            if row is None:
                return None
            result = cls(**row)
            return result #result is a class instance


