import os
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import scoped_session, sessionmaker

from dotenv                     import load_dotenv


load_dotenv(".env")

engine = create_engine(
    os.environ["DATABASE_URL"],
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = session.query_property()