from lib.object import Object
from lib.container import Container
from object.road import Roads

class Intersections (Container):
    def __init__(self, net):
        super().__init__()

        self.config = net.get('config')
        self.net = net

        self.com_object = None

        self.makeElements()

    
    def makeElements(self):
        vissim_file = self.config.get('vissim_file')
        intersections_data = vissim_file.intersections

        for intersection_data in intersections_data:
            intersection = Intersection(self, intersection_data)
            self.add(intersection)

class Intersection (Object):
    def __init__(self, intersections, data):
        super().__init__()

        self.config = intersections.get('config')
        self.intersections = intersections
        self.com_object = None

        self.id = data.id

        self.input_roads = Roads(self)
        self.output_roads = Roads(self)
        
