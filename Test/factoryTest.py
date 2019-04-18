class Factory(object):
    def createFruit(self,fruit):
        if fruit=='apple':
            return Apple()
        elif fruit=='banana':
            return Banana()
class Fruit(object):
    def __init__(self):
        print('f')

class Apple(Fruit):
    def __init__(self):
        print('a')

class Banana(Fruit):
    def __init__(self):
        print('b')


if __name__ == '__main__':
    factory = Factory()
    aa = factory.createFruit('apple')


