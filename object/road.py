from lib.container import Container
from lib.object import Object
from object.link import Links

class Roads (Container):
    def __init__(self, upper_object):
        upper_object_name = upper_object.__class__.__name__

        if upper_object_name == 'Net':
            super().__init__()
            self.config = upper_object.get('config')
            self.net = upper_object
            self.com_object = None
            self.makeElements()
        
        elif upper_object_name == 'Intersection':
            super().__init__()
            self.config = upper_object.get('config')
            self.intersection = upper_object
            self.com_object = None
    
    def makeElements(self):
        vissim_file = self.config.get('vissim_file')
        roads_data = vissim_file.roads
        for road_data in roads_data:
            road = Road(self, road_data)
            self.add(road)         

class Road (Object):    
    def __init__(self, roads, data):
        super().__init__()

        self.config = roads.get('config')
        self.roads = roads
        self.com_object = None

        self.id = data.id

        self.Links = Links(self, data.road_tags)



