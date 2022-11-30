# 1. Create a class including 2 subclasses.
# 2. Use a list comprehension syntactic and a chaining decorator.
# 3. Write the complete data to file-1 and the selected data to file-2.

import random

count_tons = [">75 t", "30-75 t", "10-30 t", "<10 t"]  # load capacity
count_engines = ["1", "2", "3", "4", "6", "8"]


def underlining(func):
    """ Decorator for tables """
    def inner(*args, **kwargs):
        print("-" * 80)
        func(*args, **kwargs)
        print("-" * 80)
    return inner


def writingToFile(name, arg_key, *args):
    """Open file: "a" - append, "w" - write, "r"  - read, "x" - create"""
    f = open(name, arg_key)

    if arg_key == "w":
        f.write('| ')
    else:
        f.write('\n| ')

    [f.write(f' {_:^10} |') for _ in args]
    f.close()


@underlining
def readingFromFile(name):
    """Open file: "a" - append, "w" - write, "r"  - read, "x" - create"""
    f = open(name, "r")
    print(f.read())
    f.close()


class Planes(object):
    """ The Plane class """

    def __init__(self, index, tons, engines, passengers):
        """ Constructor """
        self.ability = 'Yes'
        self.index = index
        self.tons = tons
        self.engines = engines
        self.passengers = passengers


class CivilianPlanes(Planes):
    def __init__(self, index, tons, engines, passengers):
        """ Constructor """
        Planes.__init__(self, index, tons, engines, passengers)
        self.kind = 'civilian'

    def filing(self):
        """ Writing data to files """
        writingToFile("table1.txt", "a", self.index, self.kind, self.ability,
                      self.tons, self.engines, self.passengers)
        if self.passengers >= 100:
            writingToFile("table2.txt", "a", self.index, self.kind, self.ability,
                          self.tons, self.engines, self.passengers)


class MilitaryPlanes(Planes):
    def __init__(self, index, tons, engines, passengers):
        """ Constructor """
        Planes.__init__(self, index, tons, engines, passengers)
        self.kind = 'military'

    def filing(self):
        """ Writing data to files """
        writingToFile("table1.txt", "a", self.index, self.kind, self.ability,
                      self.tons, self.engines, self.passengers)
        if self.passengers >= 100:
            writingToFile("table2.txt", "a", self.index, self.kind, self.ability,
                          self.tons, self.engines, self.passengers)


writingToFile("table1.txt", "w", 'Index', 'Type', 'Flying', 'Tonnage', 'Engines', 'Passengers')
writingToFile("table2.txt", "w", 'Index', 'Type', 'Flying', 'Tonnage', 'Engines', 'Passengers')


[CivilianPlanes(i, random.choice(count_tons), random.choice(count_engines), random.randint(10, 300)).filing()
    for i in range(1, 6)]

[MilitaryPlanes(i, random.choice(count_tons), random.choice(count_engines), random.randint(10, 300)).filing()
    for i in range(6, 11)]

print('\nSource table:', end="\n")
readingFromFile("table1.txt")

print('\nSelected table (Passengers > 100):', end="\n")
readingFromFile("table2.txt")
