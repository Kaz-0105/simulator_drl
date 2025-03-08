from lib.object import Object
import win32com.client
import os
from object.net import Net

class Vissim(Object):
    def __init__(self, config):
        super().__init__()

        # configオブジェクトの取得
        self.config = config
    
        # VissimのCOMオブジェクトを取得し、Vissimファイルを読み込む
        self.com_object = win32com.client.Dispatch('Vissim.Vissim')
        self.loadVissimFile()

        # Netオブジェクトの作成
        self.Net = Net(self)
    
    def loadVissimFile(self):
        vissim_file = self.config.get('vissim_file')
        self.inpx_path = os.getcwd() + '\\' + vissim_file.path + '\\' + vissim_file.inpx_file_name
        self.layx_path = os.getcwd() + '\\' + vissim_file.path + '\\' + vissim_file.layx_file_name
        self.com_object.LoadNet(self.inpx_path)
        self.com_object.LoadLayout(self.layx_path)


        
