from lib.container import Container
from lib.object import Object

class Links (Container):
    def __init__(self, upper_object):
        super().__init__()

        if upper_object.__class__.__name__ == 'Net':
            self.config = upper_object.get('config')
            self.net = upper_object
            self.com_object = upper_object.get('com_object').Links
            self.makeElements()

        elif upper_object.__class__.__name__ == 'Road':
            self.config = upper_object.get('config')
            self.road = upper_object
            self.com_object = None
    
    def makeElements(self):
        for link_object in self.com_object.GetAll():
            link = Link(self, link_object)
            self.add(link)

class Link (Object):
    def __init__(self, links, com_object):
        super().__init__()
        self.config = links.get('config')
        self.links = links
        self.com_object = com_object

        self.id = self.com_object.AttValue('No')

        
        
        