from sqlalchemy import Column, Integer, String
from database import Base, db_session
from random import randint

class URL(Base):
    __tablename__ = 'URL'

    url = Column(String, primary_key=False, nullable=False, unique=True)
    short_url = Column(String, primary_key=False, nullable=False, unique=True)
    ID = Column(Integer, primary_key=True, nullable=False, unique=True)


    def __init__(self, url, short_url):
        self.url = url
        self.short_url = short_url

        # set the id of the object to a random value
        # using a range unlikely to collide with other ids
        self.ID = randint(0,1000000)


def add_URL(url, short_url):
    if URL.query.filter(URL.url == url).one_or_none() is not None:
        print("This URL cannot be added. It already exists in the DB")
        return 
    if URL.query.filter(URL.short_url == short_url).one_or_none() is not None:
        print("This short_url URL cannot be added. It already exists in the DB")
        return 
    new_URL = URL(url, short_url)
    db_session.add(new_URL)
    db_session.commit()


def get_URL(short_url):
    try:
        return URL.query.filter(URL.short_url == short_url).one_or_none()
    except Exception as e:
        print("An exception occurred with the following details:\n{}".format(str(e)))
        return None


def get_all():
    try:
        return URL.query.filter().all()
    except Exception as e:
        print("An exception occurred with the following details:\n{}".format(str(e)))
        return None