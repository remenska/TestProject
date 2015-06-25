__author__ = 'daniela'
import os
print("Hello World")
#test_data = ["one", "two", "three", "four"]


def simple_function(test_data):
    for data in test_data:
        print(data)

simple_function(os.listdir("."))

print("Bye bye")


