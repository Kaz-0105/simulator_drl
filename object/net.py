from lib.container import Container
from object.road import Roads
from object.link import Links
from object.intersection import Intersections
from object.vehicle_input import VehicleInputs

class Net (Container):
    def __init__(self, vissim):
        super().__init__()

        self.config = vissim.get('config')
        self.vissim = vissim
        self.com_object = vissim.get('com_object').Net

        # Roadsクラスを作成
        self.roads = Roads(self)

        # Linkクラスを作成
        self.links = Links(self)
        self.connectRoadLink()

        # Intersectionクラスを作成
        self.intersections = Intersections(self)
        self.connectRoadIntersection()

        # VehicleInputクラスを作成
        self.vehicle_inputs = VehicleInputs(self)
        self.connectRoadVehicleInput()
    
    def connectRoadLink(self):
        vissim_file = self.config.get('vissim_file')
        roads_data = vissim_file.roads

        for road_data in roads_data:
            road_tags = road_data.road_tags
            for road_tag in road_tags:
                road = self.roads.objectByKey(road_tag.road_id)
                link = self.links.objectByKey(road_tag.link_id)

                link.set('type', road_tag.link_type)
                link.set('road', road)

                road.links.add(link)
                
    def connectRoadIntersection(self):
        vissim_file = self.config.get('vissim_file')
        intersections_data = vissim_file.intersections

        for intersection_data in intersections_data:
            intersection_tags = intersection_data.intersection_tags
            for intersection_tag in intersection_tags:
                intersection = self.intersections.objectByKey(intersection_tag.intersection_id)
                road = self.roads.objectByKey(intersection_tag.road_id)

                if intersection_tag.type == 1:
                    road.set('output_intersection', intersection)
                    intersection.input_roads.add(road, intersection_tag.order)
                elif intersection_tag.type == 2:
                    road.set('input_intersection', intersection)
                    intersection.output_roads.add(road, intersection_tag.order) 

    def connectRoadVehicleInput(self):
        for _, vehicle_input in self.vehicle_inputs.getAll().items():
            link_object = vehicle_input.com_object.Link
            link = self.links.objectByKey(link_object.AttValue('No'))
            road = link.road

            link.set('vehicle_input', vehicle_input)    
            road.set('vehicle_input', vehicle_input)
            vehicle_input.set('link', link)
            vehicle_input.set('road', road)