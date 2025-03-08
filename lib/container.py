from lib.common import CommonObject

class Container (CommonObject):
    def __init__(self):
        super().__init__()
        self.elements = {}
    
    def add(self, element):
        self.elements[element.get('id')] = element
    
    def count(self):
        return len(self.elements)