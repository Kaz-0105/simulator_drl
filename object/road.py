from lib.container import Container
from lib.object import Object
from object.link import Links

class Roads (Container):
    def __init__(self, net):
        super().__init__()
        self.config = net.get('config')
        self.net = net
        self.makeElements()
    
    def makeElements(self):
        vissim_file = self.config.get('vissim_file')
        roads_data = vissim_file.roads
        for road_data in roads_data:
            road = Road(self, road_data)
            self.add(road)
        print('test')
            

class Road (Object):    
    def __init__(self, roads, data):
        super().__init__()

        self.config = roads.get('config')
        self.roads = roads

        self.id = data.id

        self.Links = Links(self, data.road_tags)



