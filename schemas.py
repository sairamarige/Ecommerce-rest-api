from pydantic import BaseModel, Field


# ---------------- MOBILE ----------------

class MobileBase(BaseModel):
    name: str
    brand: str
    price: float = Field(gt=0)
    ram: int
    storage: int


class MobileCreate(MobileBase):
    pass

class MobileResponse(MobileBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- LAPTOP ----------------

class LaptopBase(BaseModel):
    name: str
    brand: str
    price: float = Field(gt=0)
    ram: int
    storage: int


class LaptopCreate(LaptopBase):
    pass


class LaptopResponse(LaptopBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- TABLET ----------------

class TabletBase(BaseModel):
    name: str
    brand: str
    price: float = Field(gt=0)
    storage: int


class TabletCreate(TabletBase):
    pass


class TabletResponse(TabletBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- SMARTWATCH ----------------

class SmartWatchBase(BaseModel):
    name: str
    brand: str
    price: float = Field(gt=0)
    battery: str


class SmartWatchCreate(SmartWatchBase):
    pass


class SmartWatchResponse(SmartWatchBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- HEADPHONE ----------------

class HeadphoneBase(BaseModel):
    name: str
    brand: str
    price: float = Field(gt=0)
    wireless: str


class HeadphoneCreate(HeadphoneBase):
    pass


class HeadphoneResponse(HeadphoneBase):
    id: int

    class Config:
        from_attributes = True