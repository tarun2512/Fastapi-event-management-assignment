import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from scripts.config import DBConf
from scripts.logger.logging import logger

Base = declarative_base()

def init_db():
    try:
        engine = create_engine(DBConf.POSTGRES_URI)
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(bind=engine)
        engine.dispose()
    except Exception as e:
        logger.error(str(e))


# Dependency
def get_db():
    # Commenting multi-tenant postgres connections for maintenance DB tables considering other module deps
    engine = create_engine(
        DBConf.POSTGRES_URI,
        pool_size=int(os.getenv("PG_POOL_SIZE", 20)),
        max_overflow=int(os.getenv("PG_MAX_OVERFLOW", 10)),
    )

    session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        engine.dispose()
