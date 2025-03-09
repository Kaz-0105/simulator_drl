from lib.container import Container
from lib.object import Object

class VehicleInputs (Container):
    def __init__(self, net):
        super().__init__()
        self.config = net.config
        self.net = net
        self.com_object = net.com_object.VehicleInputs

        self.makeElements()
    
    def makeElements(self):
        vehicle_input_objects = self.com_object.GetAll()
        for vehicle_input_object in vehicle_input_objects:
            vehicle_input = VehicleInput(self, vehicle_input_object)
            self.add(vehicle_input)
        
        inflow_data = self.config.get('inflow')
        for inflow_tag in inflow_data.inflow_tags:
            vehicle_input = self.objectByKey(inflow_tag.vehicle_input_id)
            vehicle_input.set('volume', inflow_tag.volume)
            vehicle_input.com_object.SetAttValue('Volume(1)', inflow_tag.volume)

class VehicleInput (Object):
    def __init__(self, vehicle_inputs, com_object):
        super().__init__()
        self.config = vehicle_inputs.config
        self.vehicle_inputs = vehicle_inputs
        self.com_object = com_object

        self.id = self.com_object.AttValue('No')