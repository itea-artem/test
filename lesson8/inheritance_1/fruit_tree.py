from tree import Tree


class FruitTree(Tree):
    def __init__(self, kind, height):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(kind, height)
 
    def give_fruits(self):
        print ("Collected 20kg of {}s".format(self.kind))
