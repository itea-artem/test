"""
source: https://metanit.com/python/tutorial/7.2.php
"""


class Person:
    def __init__(self, name):
        self.__name = name      # устанавливаем имя
        self.__age = 1          # устанавливаем возраст
 
    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    def get_age(self):
        return self.__age
         
    def get_name(self):
        return self.__name
 
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
         
tom = Person("Tom")
 
tom.__age = 43              # Атрибут age не изменится
tom.display_info()          # Имя: Tom  Возраст: 1
tom.set_age(-3486)          # Недопустимый возраст
tom.set_age(25)
tom.display_info()          # Имя: Tom  Возраст: 25