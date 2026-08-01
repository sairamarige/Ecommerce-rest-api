from sqlalchemy.orm import Session
import models


# ==========================
# MOBILE CRUD
# ==========================

def create_mobile(db: Session, mobile):
    db_mobile = models.Mobile(**mobile.model_dump())
    db.add(db_mobile)
    db.commit()
    db.refresh(db_mobile)
    return db_mobile


def get_all_mobiles(db: Session):
    return db.query(models.Mobile).all()


def get_mobile(db: Session, mobile_id: int):
    return db.query(models.Mobile).filter(
        models.Mobile.id == mobile_id
    ).first()


def update_mobile(db: Session, mobile_id: int, mobile):

    db_mobile = get_mobile(db, mobile_id)

    if db_mobile is None:
        return None

    for key, value in mobile.model_dump().items():
        setattr(db_mobile, key, value)

    db.commit()
    db.refresh(db_mobile)

    return db_mobile


def delete_mobile(db: Session, mobile_id: int):

    db_mobile = get_mobile(db, mobile_id)

    if db_mobile is None:
        return None

    db.delete(db_mobile)
    db.commit()

    return db_mobile


# ==========================
# LAPTOP CRUD
# ==========================

def create_laptop(db: Session, laptop):
    db_laptop = models.Laptop(**laptop.model_dump())
    db.add(db_laptop)
    db.commit()
    db.refresh(db_laptop)
    return db_laptop


def get_all_laptops(db: Session):
    return db.query(models.Laptop).all()


def get_laptop(db: Session, laptop_id: int):
    return db.query(models.Laptop).filter(
        models.Laptop.id == laptop_id
    ).first()


def update_laptop(db: Session, laptop_id: int, laptop):

    db_laptop = get_laptop(db, laptop_id)

    if db_laptop is None:
        return None

    for key, value in laptop.model_dump().items():
        setattr(db_laptop, key, value)

    db.commit()
    db.refresh(db_laptop)

    return db_laptop


def delete_laptop(db: Session, laptop_id: int):

    db_laptop = get_laptop(db, laptop_id)

    if db_laptop is None:
        return None

    db.delete(db_laptop)
    db.commit()

    return db_laptop


# ==========================
# TABLET CRUD
# ==========================

def create_tablet(db: Session, tablet):
    db_tablet = models.Tablet(**tablet.model_dump())
    db.add(db_tablet)
    db.commit()
    db.refresh(db_tablet)
    return db_tablet


def get_all_tablets(db: Session):
    return db.query(models.Tablet).all()


def get_tablet(db: Session, tablet_id: int):
    return db.query(models.Tablet).filter(
        models.Tablet.id == tablet_id
    ).first()


def update_tablet(db: Session, tablet_id: int, tablet):

    db_tablet = get_tablet(db, tablet_id)

    if db_tablet is None:
        return None

    for key, value in tablet.model_dump().items():
        setattr(db_tablet, key, value)

    db.commit()
    db.refresh(db_tablet)

    return db_tablet


def delete_tablet(db: Session, tablet_id: int):

    db_tablet = get_tablet(db, tablet_id)

    if db_tablet is None:
        return None

    db.delete(db_tablet)
    db.commit()

    return db_tablet


# ==========================
# SMARTWATCH CRUD
# ==========================

def create_smartwatch(db: Session, smartwatch):
    db_watch = models.SmartWatch(**smartwatch.model_dump())
    db.add(db_watch)
    db.commit()
    db.refresh(db_watch)
    return db_watch


def get_all_smartwatches(db: Session):
    return db.query(models.SmartWatch).all()


def get_smartwatch(db: Session, watch_id: int):
    return db.query(models.SmartWatch).filter(
        models.SmartWatch.id == watch_id
    ).first()


def update_smartwatch(db: Session, watch_id: int, smartwatch):

    db_watch = get_smartwatch(db, watch_id)

    if db_watch is None:
        return None

    for key, value in smartwatch.model_dump().items():
        setattr(db_watch, key, value)

    db.commit()
    db.refresh(db_watch)

    return db_watch


def delete_smartwatch(db: Session, watch_id: int):

    db_watch = get_smartwatch(db, watch_id)

    if db_watch is None:
        return None

    db.delete(db_watch)
    db.commit()

    return db_watch


# ==========================
# HEADPHONE CRUD
# ==========================

def create_headphone(db: Session, headphone):
    db_headphone = models.Headphone(**headphone.model_dump())
    db.add(db_headphone)
    db.commit()
    db.refresh(db_headphone)
    return db_headphone


def get_all_headphones(db: Session):
    return db.query(models.Headphone).all()


def get_headphone(db: Session, headphone_id: int):
    return db.query(models.Headphone).filter(
        models.Headphone.id == headphone_id
    ).first()


def update_headphone(db: Session, headphone_id: int, headphone):

    db_headphone = get_headphone(db, headphone_id)

    if db_headphone is None:
        return None

    for key, value in headphone.model_dump().items():
        setattr(db_headphone, key, value)

    db.commit()
    db.refresh(db_headphone)

    return db_headphone


def delete_headphone(db: Session, headphone_id: int):

    db_headphone = get_headphone(db, headphone_id)

    if db_headphone is None:
        return None

    db.delete(db_headphone)
    db.commit()

    return db_headphone