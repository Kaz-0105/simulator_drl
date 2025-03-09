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

    def getAll(self, sequence_flg=False):
        if sequence_flg:
            new_elements = {}
            count = 0
            for _, value in self.elements.items():
                new_elements[count] = value
                count += 1
            return new_elements
        else:
            return self.elements