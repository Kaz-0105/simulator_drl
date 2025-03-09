from lib.container import Container
from lib.object import Object

class Links (Container):
    def __init__(self, road, road_tags):
        super().__init__()
        self.config = road.get('config')
        self.road = road
        self.com_object = road.get('roads').get('net').get('com_object').Links
        self.makeElements(road_tags)
    
    def makeElements(self, road_tags):
        for road_tag in road_tags:
            link = Link(self, road_tag)
            self.add(link)

class Link (Object):
    def __init__(self, links, road_tag):
        super().__init__()
        self.config = links.get('config')
        self.links = links

        self.id = road_tag.link_id
        self.type = road_tag.link_type

        self.com_object = links.get('com_object').ItemByKey(road_tag.link_id)
        
        