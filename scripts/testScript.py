from foo import FooFoo

try:
    foo = FooFoo()
    assert isinstance(foo, object)
    foo.get_name()
    foo.get_age()
except TypeError:
    print("Exception")

print(foo.get_name(),":",foo.get_age())