from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base
from typing import List

app = FastAPI()

DATABASE_URL = 'sqlite:///mood_journal.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()   

class Journal(Base):
    __tablename__ = 'journals'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    mood = Column(String, nullable=False)
    entry = Column(String, nullable=False)
    date = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class JournalCreate(BaseModel):
    mood: str
    entry: str
    date: str

class JournalSchema(BaseModel):
    id: int
    mood: str
    entry: str
    date: str

    class Config:
        orm_mode = True

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/journals/")
def create_journal(journal: JournalCreate, db: Session = Depends(get_db)):
    db_journal = Journal(**journal.dict())
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    return {"message": "Journal entry created successfully", "id": db_journal.id}

@app.get("/journals/", response_model=List[JournalSchema])
def get_journals(db: Session = Depends(get_db)):
    # Fetch all journal entries from the database
    journals = db.query(Journal).all()
    return journals

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="0.0.0.0", port=8081)
    except SystemExit:
        pass  # Prevent traceback on normal exit