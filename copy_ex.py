# -*- coding = utf-8 -*-


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating!" % self.name)

class Person(Animal):
    def __init__(self, name, age, sex):
        super(Person, self).__init__(name, age)
        self.sex = sex

    def eat(self):
        super(Person, self).eat()
        print("person is eating!")

person = Person("ghy", 35, "nan")
person.eat()