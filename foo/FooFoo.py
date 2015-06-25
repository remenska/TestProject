__author__ = 'daniela'

class FooFoo(object):
    name = "John Doe"
    age = 44

    def __init__(self, name = "John Doe", age = 45):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


