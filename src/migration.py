from sqlalchemy import MetaData, Table, Column
from models import engine, Base


def create_tables():
    Base.metadata.create_all(engine)

create_tables()
