# entities.py

class Entity:
    '''
    Base class for entity in adventure game
    '''
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon