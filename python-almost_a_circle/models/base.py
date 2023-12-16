'''my base class'''
class base:
   
    '''we define a class named Base with a private class attribute __nb_objects'''
    __nb_objects = 0
    '''creating instances of our class'''
    def __init__(self, id=None):
        '''the first parameter'''
        if id is not None:
            self.id = id
        else:
            '''the base class is the increament setting'''
            base. __nb_objects += 1
            self.id = base.__nb_objects

