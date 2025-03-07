from ..lib.model import Model
import win32com.client

class Vissim(Model):
    def __init__(self, Config):
        super().__init__()

        self.comObject = win32com.client.Dispatch('Vissim.Vissim')

        self.inpx_path = dir + '\\layout\\one_lane\\network.inpx'
        self.layx_path = dir + '\\layout\\one_lane\\network.layx'

        self.comObject.LoadNet(self.inpx_path)
        self.comObject.LoadLayout(self.layx_path)

        
