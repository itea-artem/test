"""
source: http://pythonicway.com/education/python-oop-themes/21-python-inheritance
"""

class Tree:
    def __init__(self, kind, height):
         self.kind = kind
         self.age = 0
         self.height = height

    def info(self):
         """ Метод вывода информации о дереве """
         print ("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))

    def grow(self):
        """ Метод роста """
        self.age += 1
        self.height += 0.5
