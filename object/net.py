from lib.container import Container
from object.road import Roads
class Net (Container):
    def __init__(self, vissim):
        super().__init__()

        self.config = vissim.get('config')
        self.vissim = vissim
        self.com_object = vissim.get('com_object').Net

        self.roads = Roads(self)
        
