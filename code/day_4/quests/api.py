from http.client import HTTPException
from fastapi import FastAPI, Depends, HTTPException
from schemas import SchemaItem
from typing import ItemsView, List
from models import Base
from sqlalchemy.orm import Session
from database import get_db, engine
from crud import get_item, get_items, create_item

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/status")
def status():
    return{"message": "ok"}

@app.get("/items", response_model = List[SchemaItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_item(db, skip=skip, limit=limit)
    return Items

@app.post("/items", responde_model=SchemaItem)
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=SchemaItem)
def read_item(item_ide: int, db: Session = Depends(get_db)):
    db_item = get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item