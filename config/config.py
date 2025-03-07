from lib.common import CommonObject
import os

class Config(CommonObject):
    def __init__(self):
        super().__init__()
    
        # TODO : vissim_file_idをGUIから作成したい
        self.vissim_file_id = 1
        self.getVissimFile()
        
    def getVissimFile(self):
        self.cursor.execute('SELECT * FROM vissim_files WHERE id = ?', (self.vissim_file_id,))
        data = self.cursor.fetchall()
        self.vissim_file = {
            'id': data[0][0],
            'name': data[0][1],
            'inpx_file_name': data[0][2],
            'layout_file_name': data[0][3],
            'path': data[0][4],
            'description': data[0][5]
        }
    
        
