from lib.object import Object
import win32com.client
import os
from model.net import Net

class Vissim(Object):
    def __init__(self, config):
        super().__init__()

        self.config = config
    
        self.comObject = win32com.client.Dispatch('Vissim.Vissim')
        self.loadVissimFile()

        self.Net = Net(self)


    
    def loadVissimFile(self):
        self.inpx_path = os.getcwd() + '\\' + self.config.vissim_file['path'] + '\\' + self.config.vissim_file['inpx_file_name']
        self.layx_path = os.getcwd() + '\\' + self.config.vissim_file['path'] + '\\' + self.config.vissim_file['layout_file_name']
        self.comObject.LoadNet(self.inpx_path)
        self.comObject.LoadLayout(self.layx_path)


        
