from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import joinedload

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

class RouteSet(Base):
    __tablename__ = 'route_sets'

    id = Column(Integer, primary_key=True)
    num_roads = Column(Integer)
    name = Column(String)
    description = Column(String)

    route_set_tags = relationship('RouteSetTag', back_populates='route_set')

class RouteSetTag(Base):
    __tablename__ = 'route_set_tags'

    id = Column(Integer, primary_key=True)
    route_set_id = Column(Integer, ForeignKey('route_sets.id'))
    order = Column(Integer)
    route_id = Column(Integer, ForeignKey('routes.id'))

    route_set = relationship('RouteSet', back_populates='route_set_tags')
    route = relationship('Route', back_populates='route_set_tags')

class Route(Base):
    __tablename__ = 'routes'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    route_set_tags = relationship('RouteSetTag', back_populates='route')
    route_tags = relationship('RouteTag', back_populates='route')

class RouteTag(Base):
    __tablename__ = 'route_tags'

    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'))
    order = Column(Integer)
    relative_volume = Column(Float)

    route = relationship('Route', back_populates='route_tags')

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
        self.RouteSet = RouteSet
        self.RouteSetTag = RouteSetTag
        self.Route = Route
        self.RouteTag = RouteTag

    def getVissimFile(self, vissim_file_id):
        return self.session.query(self.VissimFile).filter_by(id=vissim_file_id).first()
    
    def getInflow(self, vissim_file_id, inflow_id):
        return self.session.query(self.Inflow).filter_by(id=inflow_id, vissim_file_id=vissim_file_id).first()

    def getRouteSets(self, route_set_ids):
        # DBからデータを取得
        route_sets_data = self.session.query(self.RouteSet).filter(self.RouteSet.id.in_(list(route_set_ids.values()))).all()
        
        # キーをID，値をRouteSetオブジェクトとした辞書を作成
        route_sets_dict = {}
        for route_set_data in route_sets_data:
            route_sets_dict[route_set_data.id] = route_set_data
        
        # キーを交差点ID，値をRouteSetオブジェクトとした辞書を作成
        route_sets = {}
        for intersection_id, route_set_id in route_set_ids.items():
            route_sets[intersection_id] = route_sets_dict[route_set_id]
        
        return route_sets

    @staticmethod
    def sortById(model_data):
        sorted_data = {}
        for tmp_data in model_data:
            sorted_data[tmp_data.id] = tmp_data
        return sorted_data