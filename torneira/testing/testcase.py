import unittest2
from torneira.testing.client import TestingClient

class TestCase(unittest2.TestCase):
    
    def __init__(self):
        self.client = TestingClient()