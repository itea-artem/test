from tree import Tree
from fruit_tree import FruitTree

tree_1 = Tree('pear', 1.2)
tree_2 = FruitTree("apple", 0.7)
# у нас есть доступ к методам родителя
tree_2.info()
tree_2.grow()
# Мы можем использовать свой метод
tree_2.give_fruits()
# А для родительского экземпляра метод give_fruits() недоступен
tree_1.give_fruits() # Вызовет ошибку
