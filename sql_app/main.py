from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import Sessionlocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependencies

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users/", response_model=schemas.User,status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_user(skip_int: int = 0, limit_int: int = 100, db: Session = Depends(get_db)):
    users = crud.get_user(db, skip=skip_int, limit=limit_int)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user 

@app.post("/users/{user_id}/items/", response_model=schemas.Item, status_code=201)
def create_item(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip_int: int = 0, limit_int: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip_int, limit=limit_int)
    return items