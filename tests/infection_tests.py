from nose.tools import * 
import infection 

def setup():
	print("SETUP!")

def teardown():
	print("TEARDOWN!")

def test_basic():
	print("I RAN!")