import unittest
from python99 import helloworld

def test_say_hello():
    test_object = helloworld.HelloWorld()
    assert test_object.say_hello('Joe') == 'Hello World!!! Joe'
