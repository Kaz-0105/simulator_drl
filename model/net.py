from lib.container import Container
from model.road import Roads
class Net (Container):
    def __init__(self, vissim):
        super().__init__()

        self.config = vissim.get('config')
        self.vissim = vissim
        self.comObject = vissim.comObject.Net

        self.roads = Roads(self)
        
