from lib.common import CommonObject
from sqlalchemy import Table
from model.model import ConfigController
class Config(CommonObject):
    def __init__(self):
        super().__init__()
        self.config_controller = ConfigController()

        # 定数の設定
        self.road_type = {
            '1' : '流入道路',
            '2' : '流出道路',
        }
        self.link_types = {
            '1' : 'メインリンク',
            '2' : '右折用サブリンク',
            '3' : '右折用コネクタ',
            '4' : '左折用サブリンク',
            '5' : '左折用コネクタ',
        }

        # TODO : vissim_file_id, inflow_idをGUIから取得したい
        self.vissim_file_id = 1
        self.inflow_id = 1

        # vissim_fileの取得
        self.vissim_file = self.config_controller.getVissimFile(self.vissim_file_id)
        self.inflow = self.config_controller.getInflow(self.vissim_file_id, self.inflow_id)

    
        
