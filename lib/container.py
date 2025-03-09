from lib.common import CommonObject

class Container (CommonObject):
    def __init__(self):
        super().__init__()
        self.elements = {}
    
    def add(self, element, id=None):
        if id is not None:
            self.elements[id] = element
        else:
            self.elements[element.get('id')] = element
    
    def count(self):
        return len(self.elements)
    
    def objectByKey(self, id):
        return self.elements[id]