

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL ulanish ma'lumotlari
DATABASE_URL = "postgresql://postgres:123@localhost:5432/autosalonlar"

# Engine va session yaratish
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM bazasi
Base = declarative_base()

# Model klass
class AutoSalonlar(Base):
    __tablename__ = 'autosalonlar'  # Jadval nomi shu bo‘lishi kerak

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    city = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)


session = SessionLocal()

a1 = AutoSalonlar(brand="BMW", phone="+998938000747", city="Toshkent")

session.add(a1)
session.commit()
session.close()




