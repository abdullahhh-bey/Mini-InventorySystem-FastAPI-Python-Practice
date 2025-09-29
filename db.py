from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib

# Using Windows Authentication, no password needed
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=DESKTOP-JOGOILA\SQLEXPRESS01;"   
    "DATABASE=InventoryDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()