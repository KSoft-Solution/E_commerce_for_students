from sqlalchemy import create_engine, text

from config.config import DB_URL

engine = create_engine(DB_URL,echo=True)
with engine.connect() as connection:
    connection.execute(text("CREATE TABLE example10 (id INTEGER, name VARCHAR(20))"))


