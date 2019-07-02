

if __name__ == '__main__':
    x = 4
    print(x.__add__(5))  # 4 + 5
    print(dir(x))  # all magic methods for int

    x = [1, 2]
    print(x.__add__([3]))  # x + [3]
    print(dir(x))

    x = 'Hello world'
    print(x.__getitem__(1))  # x[1]
    print(dir(x))

    x = {'a': 1}
    print(x.__contains__('b'))  # 'b' in x
    print(dir(x))
