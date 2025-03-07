from lib.common import CommonObject

class Container (CommonObject):
    def __init__(self):
        super().__init__()
        self.elements = {}
        self.last_index = -1