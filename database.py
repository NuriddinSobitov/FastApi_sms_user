from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

Session = sessionmaker(engine, autoflush=True)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()