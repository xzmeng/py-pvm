def add(a, b):
    return a + b


add_one = lambda x: x + 1


class Person:
    max_age = 150

    def __init__(self, name):
        self.name = name

    def info(self):
        print('this is ' + self.name)


p = Person('xzmeng')
p.info()
print(add(1, 1))
print(add_one(2))
