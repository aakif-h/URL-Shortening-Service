# external libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

parent_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))

if not os.path.exists(os.path.abspath(parent_dir + '/db')):
    os.makedirs(parent_dir + '/db')

engine = create_engine('sqlite:///db/URL_DATABASE.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all necessary modules that define models so they get
    # registered properly on the metadata

    Base.metadata.create_all(bind=engine)