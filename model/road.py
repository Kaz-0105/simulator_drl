from lib.container import Container
from lib.object import Object

class Roads (Container):
    def __init__(self, net):
        super().__init__()
        self.config = net.get('config')
        self.net = net
        self.makeElements()
    
    def makeElements(self):
        pass

class Road (Object):    
    pass