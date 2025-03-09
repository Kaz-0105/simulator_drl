from lib.container import Container
from object.road import Roads
from object.intersection import Intersections

class Net (Container):
    def __init__(self, vissim):
        super().__init__()

        self.config = vissim.get('config')
        self.vissim = vissim
        self.com_object = vissim.get('com_object').Net

        # RoadsクラスとIntersectionsクラスを作成
        self.roads = Roads(self)
        self.intersections = Intersections(self)

        self.connectRoadIntersection()

    def connectRoadIntersection(self):
        vissim_file = self.config.get('vissim_file')
        intersections_data = vissim_file.intersections

        for intersection_data in intersections_data:
            intersection_tags = intersection_data.intersection_tags
            for intersection_tag in intersection_tags:
                intersection = self.intersections.objectByKey(intersection_tag.intersection_id)
                road = self.roads.objectByKey(intersection_tag.road_id)

                if intersection_tag.type == 1:
                    intersection.input_roads.add(road, intersection_tag.order)
                elif intersection_tag.type == 2:
                    intersection.output_roads.add(road, intersection_tag.order)
        
        print('test')
        
