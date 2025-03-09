from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///simulator.db')
metadata = MetaData()
metadata.reflect(bind=engine)

Base = declarative_base()

# モデルクラスの定義
class VissimFile(Base):
    __tablename__ = 'vissim_files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    inpx_file_name = Column(String)
    layx_file_name = Column(String)
    path = Column(String)
    description = Column(String)

    inflows = relationship('Inflow', back_populates = 'vissim_file')
    roads = relationship('Road', back_populates = 'vissim_file')
    intersections = relationship('Intersection', back_populates = 'vissim_file')
    inflows = relationship('Inflow', back_populates='vissim_file')

class Inflow(Base):
    __tablename__ = 'inflows'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    vissim_file_id = Column(Integer, ForeignKey('vissim_files.id'))
    description = Column(String)

    vissim_file = relationship('VissimFile', back_populates='inflows')
    inflow_tags = relationship('InflowTag', back_populates='inflow')

class InflowTag(Base):
    __tablename__ = 'inflow_tags'

    id = Column(Integer, primary_key=True)
    inflow_id = Column(Integer, ForeignKey('inflows.id'))
    vehicle_input_id = Column(Integer)
    volume = Column(Float)

    inflow = relationship('Inflow', back_populates='inflow_tags')

class Road(Base):
    __tablename__ = 'roads'

    id = Column(Integer, primary_key=True)
    vissim_file_id = Column(Integer, ForeignKey('vissim_files.id'))

    vissim_file = relationship('VissimFile', back_populates='roads')
    road_link_tags = relationship('RoadLinkTag', back_populates='road')

class RoadLinkTag(Base):
    __tablename__ = 'road_link_tags'

    id = Column(Integer, primary_key=True)
    road_id = Column(Integer, ForeignKey('roads.id'))
    link_id = Column(Integer)
    link_type = Column(Integer)

    road = relationship('Road', back_populates='road_link_tags')

class Intersection(Base):
    __tablename__ = 'intersections'

    id = Column(Integer, primary_key=True)
    vissim_file_id = Column(Integer, ForeignKey('vissim_files.id'))

    vissim_file = relationship('VissimFile', back_populates='intersections')
    intersection_road_tags = relationship('IntersectionRoadTag', back_populates='intersection')

class IntersectionRoadTag(Base):
    __tablename__ = 'intersection_road_tags'

    id = Column(Integer, primary_key=True)
    intersection_id = Column(Integer, ForeignKey('intersections.id'))
    road_id = Column(Integer)
    order = Column(Integer)
    type = Column(Integer)

    intersection = relationship('Intersection', back_populates='intersection_road_tags')

Session = sessionmaker(bind=engine)

class ConfigController:
    def __init__(self):
        self.engine = engine
        self.metadata = metadata
        self.session = Session()
        self.VissimFile = VissimFile
        self.Road = Road
        self.RoadLinkTag = RoadLinkTag
        self.Intersection = Intersection
        self.IntersectionRoadTag = IntersectionRoadTag
        self.Inflow = Inflow
        self.InflowTag = InflowTag

    def getVissimFile(self, vissim_file_id):
        return self.session.query(self.VissimFile).filter_by(id=vissim_file_id).first()
    
    def getInflow(self, vissim_file_id, inflow_id):
        return self.session.query(self.Inflow).filter_by(id=inflow_id, vissim_file_id=vissim_file_id).first()
    
    @staticmethod
    def sortById(model_data):
        sorted_data = {}
        for tmp_data in model_data:
            sorted_data[tmp_data.id] = tmp_data
        return sorted_data