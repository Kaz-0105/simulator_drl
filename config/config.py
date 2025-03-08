from lib.common import CommonObject
from sqlalchemy import Table
from model.model import ConfigController
class Config(CommonObject):
    def __init__(self):
        super().__init__()
        self.config_controller = ConfigController()

        # 定数の設定
        self.orders = {
            # 三差路
            '3' : {
                '0' : '系外への流出道路',
                '1' : '流入道路（１）',
                '2' : '流入道路（２）',
                '3' : '流入道路（３）',
            },
            # 十字路
            '4' : {
                '0' : '系外への流出道路',
                '1' : '流入道路（北）',
                '2' : '流入道路（東）',
                '3' : '流入道路（南）',
                '4' : '流入道路（西）',
            },
            # 五差路
            '5' : {
                '0' : '系外への流出道路',
                '1' : '流入道路（１）',
                '2' : '流入道路（２）',
                '3' : '流入道路（３）',
                '4' : '流入道路（４）',
                '5' : '流入道路（５）',
            }
        }
        self.link_types = {
            '1' : 'メインリンク',
            '2' : '右折用サブリンク',
            '3' : '右折用コネクタ',
            '4' : '左折用サブリンク',
            '5' : '左折用コネクタ',
        }

        # TODO : vissim_file_idをGUIから作成したい
        self.vissim_file_id = 1

        # vissim_fileの取得
        self.vissim_file = self.config_controller.getVissimFile(self.vissim_file_id)
    
        
