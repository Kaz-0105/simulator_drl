from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

class CommonObject:
    def get(self, property_name):
        try:
            return getattr(self, property_name)
        except AttributeError:
            print('指定されたプロパティは存在しません')
            return None
    
    def set(self, property_name, value):
        setattr(self, property_name, value)