from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Product API",
    description="REST API for Mobiles, Laptops, Tablets, Smartwatches and Headphones",
    version="1.0.0"
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ======================================================
# HOME
# ======================================================

@app.get("/")
def home():
    return {"message": "Welcome to E-Commerce REST API"}


# ======================================================
# MOBILE ENDPOINTS
# ======================================================

@app.post("/mobiles", response_model=schemas.MobileResponse)
def create_mobile(mobile: schemas.MobileCreate, db: Session = Depends(get_db)):
    return crud.create_mobile(db, mobile)


@app.get("/mobiles", response_model=list[schemas.MobileResponse])
def get_mobiles(db: Session = Depends(get_db)):
    return crud.get_all_mobiles(db)


@app.get("/mobiles/{mobile_id}", response_model=schemas.MobileResponse)
def get_mobile(mobile_id: int, db: Session = Depends(get_db)):
    mobile = crud.get_mobile(db, mobile_id)

    if not mobile:
        raise HTTPException(status_code=404, detail="Mobile not found")

    return mobile


@app.put("/mobiles/{mobile_id}", response_model=schemas.MobileResponse)
def update_mobile(
    mobile_id: int,
    mobile: schemas.MobileCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_mobile(db, mobile_id, mobile)

    if not updated:
        raise HTTPException(status_code=404, detail="Mobile not found")

    return updated


@app.delete("/mobiles/{mobile_id}")
def delete_mobile(mobile_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_mobile(db, mobile_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Mobile not found")

    return {"message": "succesfully deleted mobile"}


# ======================================================
# LAPTOP ENDPOINTS
# ======================================================

@app.post("/laptops", response_model=schemas.LaptopResponse)
def create_laptop(laptop: schemas.LaptopCreate, db: Session = Depends(get_db)):
    return crud.create_laptop(db, laptop)


@app.get("/laptops", response_model=list[schemas.LaptopResponse])
def get_laptops(db: Session = Depends(get_db)):
    return crud.get_all_laptops(db)


@app.get("/laptops/{laptop_id}", response_model=schemas.LaptopResponse)
def get_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = crud.get_laptop(db, laptop_id)

    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")

    return laptop


@app.put("/laptops/{laptop_id}", response_model=schemas.LaptopResponse)
def update_laptop(
    laptop_id: int,
    laptop: schemas.LaptopCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_laptop(db, laptop_id, laptop)

    if not updated:
        raise HTTPException(status_code=404, detail="Laptop not found")

    return updated


@app.delete("/laptops/{laptop_id}")
def delete_laptop(laptop_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_laptop(db, laptop_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Laptop not found")

    return {"message": "Laptop deleted successfully"}


# ======================================================
# TABLET ENDPOINTS
# ======================================================

@app.post("/tablets", response_model=schemas.TabletResponse)
def create_tablet(tablet: schemas.TabletCreate, db: Session = Depends(get_db)):
    return crud.create_tablet(db, tablet)


@app.get("/tablets", response_model=list[schemas.TabletResponse])
def get_tablets(db: Session = Depends(get_db)):
    return crud.get_all_tablets(db)


@app.get("/tablets/{tablet_id}", response_model=schemas.TabletResponse)
def get_tablet(tablet_id: int, db: Session = Depends(get_db)):
    tablet = crud.get_tablet(db, tablet_id)

    if not tablet:
        raise HTTPException(status_code=404, detail="Tablet not found")

    return tablet


@app.put("/tablets/{tablet_id}", response_model=schemas.TabletResponse)
def update_tablet(
    tablet_id: int,
    tablet: schemas.TabletCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_tablet(db, tablet_id, tablet)

    if not updated:
        raise HTTPException(status_code=404, detail="Tablet not found")

    return updated


@app.delete("/tablets/{tablet_id}")
def delete_tablet(tablet_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_tablet(db, tablet_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Tablet not found")

    return {"message": "Tablet deleted successfully"}


# ======================================================
# SMARTWATCH ENDPOINTS
# ======================================================

@app.post("/smartwatches", response_model=schemas.SmartWatchResponse)
def create_watch(watch: schemas.SmartWatchCreate, db: Session = Depends(get_db)):
    return crud.create_smartwatch(db, watch)


@app.get("/smartwatches", response_model=list[schemas.SmartWatchResponse])
def get_watches(db: Session = Depends(get_db)):
    return crud.get_all_smartwatches(db)


@app.get("/smartwatches/{watch_id}", response_model=schemas.SmartWatchResponse)
def get_watch(watch_id: int, db: Session = Depends(get_db)):
    watch = crud.get_smartwatch(db, watch_id)

    if not watch:
        raise HTTPException(status_code=404, detail="SmartWatch not found")

    return watch


@app.put("/smartwatches/{watch_id}", response_model=schemas.SmartWatchResponse)
def update_watch(
    watch_id: int,
    watch: schemas.SmartWatchCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_smartwatch(db, watch_id, watch)

    if not updated:
        raise HTTPException(status_code=404, detail="SmartWatch not found")

    return updated


@app.delete("/smartwatches/{watch_id}")
def delete_watch(watch_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_smartwatch(db, watch_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="SmartWatch not found")

    return {"message": "SmartWatch deleted successfully"}


# ======================================================
# HEADPHONE ENDPOINTS
# ======================================================

@app.post("/headphones", response_model=schemas.HeadphoneResponse)
def create_headphone(headphone: schemas.HeadphoneCreate, db: Session = Depends(get_db)):
    return crud.create_headphone(db, headphone)


@app.get("/headphones", response_model=list[schemas.HeadphoneResponse])
def get_headphones(db: Session = Depends(get_db)):
    return crud.get_all_headphones(db)


@app.get("/headphones/{headphone_id}", response_model=schemas.HeadphoneResponse)
def get_headphone(headphone_id: int, db: Session = Depends(get_db)):
    headphone = crud.get_headphone(db, headphone_id)

    if not headphone:
        raise HTTPException(status_code=404, detail="Headphone not found")

    return headphone


@app.put("/headphones/{headphone_id}", response_model=schemas.HeadphoneResponse)
def update_headphone(
    headphone_id: int,
    headphone: schemas.HeadphoneCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_headphone(db, headphone_id, headphone)

    if not updated:
        raise HTTPException(status_code=404, detail="Headphone not found")

    return updated


@app.delete("/headphones/{headphone_id}")
def delete_headphone(headphone_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_headphone(db, headphone_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Headphone not found")

    return {"message": "Headphone deleted successfully"}
