from sqlalchemy import Column, DateTime, String, Integer, func, ARRAY, create_engine

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    login = Column(String, unique=True)
    password = Column(String)
    api_token = Column(String, unique=True)
    telegram_id = Column(String, unique=True)
    articles_read = Column(ARRAY(String))
    articles_written = Column(ARRAY(String))
    user_id = Column(Integer, primary_key=True)
    subs = Column(ARRAY(String))
    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)


class Articles(Base):
    __tablename__ = 'articles'
    author = Column(String)
    title = Column(String)
    text = Column(String)
    image = Column(String)
    time_stamp = Column(DateTime, default=func.now())
    tags = Column(ARRAY(String))
    article_id = Column(Integer, primary_key=True)
    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)

class Comments(Base):
    __tablename__ = 'posts'
    comment_id = Column(Integer, primary_key=True)
    article_id = Column(Integer)
    author = Column(String)
    text = Column(String)
    time_stamp = Column(DateTime, default=func.now())
    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@db/postgres",
    isolation_level="SERIALIZABLE",
)
Base.metadata.create_all(engine)