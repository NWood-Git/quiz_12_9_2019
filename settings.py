import os

dirname = os.path.dirname(__file__)
DBPATH = os.path.join(dirname, "app", "shirts.db")
TESTDBPATH = os.path.join(dirname, "test", "_test.db")