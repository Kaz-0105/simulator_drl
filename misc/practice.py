from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///simulator.db')
metadata = MetaData()
metadata.reflect(bind=engine)

print(metadata.tables.keys())

Base = declarative_base()

class VissimFile(Base):
    __table__ = Table('vissim_files', metadata, autoload_with=engine)

print(VissimFile.__table__.columns.keys())

Session = sessionmaker(bind=engine)
session = Session()

vissim_files = session.query(VissimFile).all()

for vissim_file in vissim_files:
    print(vissim_file.inpx_file_name)


