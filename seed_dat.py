from database import SessionLocal, engine
from models import Base, Mobile, Laptop, Tablet, SmartWatch, Headphone

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# -----------------------------
# Mobiles
# -----------------------------
mobiles = [
    Mobile(name="iPhone 16", brand="Apple", price=89999, ram=8, storage=128),
    Mobile(name="Galaxy S25", brand="Samsung", price=84999, ram=12, storage=256),
    Mobile(name="OnePlus 13", brand="OnePlus", price=64999, ram=12, storage=256),
    Mobile(name="Pixel 10", brand="Google", price=79999, ram=12, storage=256),
    Mobile(name="Nothing Phone 3", brand="Nothing", price=45999, ram=8, storage=128),
    Mobile(name="Redmi Note 15", brand="Xiaomi", price=24999, ram=8, storage=128),
    Mobile(name="Realme GT 7", brand="Realme", price=39999, ram=12, storage=256),
    Mobile(name="Moto Edge 70", brand="Motorola", price=35999, ram=8, storage=128),
    Mobile(name="Vivo X300", brand="Vivo", price=52999, ram=12, storage=256),
    Mobile(name="Oppo Reno 15", brand="Oppo", price=37999, ram=8, storage=256),
]

# -----------------------------
# Laptops
# -----------------------------
laptops = [
    Laptop(name="MacBook Air M4", brand="Apple", price=119999, ram=16, storage=512),
    Laptop(name="Dell XPS 15", brand="Dell", price=149999, ram=16, storage=1024),
    Laptop(name="HP Pavilion", brand="HP", price=69999, ram=16, storage=512),
    Laptop(name="Lenovo ThinkPad", brand="Lenovo", price=89999, ram=16, storage=512),
    Laptop(name="Asus Zenbook", brand="Asus", price=79999, ram=16, storage=512),
    Laptop(name="Acer Aspire 7", brand="Acer", price=64999, ram=16, storage=512),
    Laptop(name="MSI Katana", brand="MSI", price=99999, ram=16, storage=1024),
    Laptop(name="Samsung Galaxy Book", brand="Samsung", price=84999, ram=16, storage=512),
    Laptop(name="LG Gram", brand="LG", price=109999, ram=16, storage=512),
    Laptop(name="Razer Blade 16", brand="Razer", price=199999, ram=32, storage=1024),
]

# -----------------------------
# Tablets
# -----------------------------
tablets = [
    Tablet(name="iPad Air", brand="Apple", price=59999, storage=128),
    Tablet(name="Galaxy Tab S10", brand="Samsung", price=69999, storage=256),
    Tablet(name="Lenovo Tab P12", brand="Lenovo", price=34999, storage=128),
    Tablet(name="Xiaomi Pad 7", brand="Xiaomi", price=32999, storage=128),
    Tablet(name="OnePlus Pad", brand="OnePlus", price=37999, storage=128),
    Tablet(name="Realme Pad X", brand="Realme", price=22999, storage=64),
    Tablet(name="Nokia T21", brand="Nokia", price=19999, storage=64),
    Tablet(name="Honor Pad", brand="Honor", price=24999, storage=128),
    Tablet(name="Redmi Pad Pro", brand="Xiaomi", price=28999, storage=128),
    Tablet(name="Amazon Fire HD 10", brand="Amazon", price=15999, storage=64),
]

# -----------------------------
# SmartWatches
# -----------------------------
smartwatches = [
    SmartWatch(name="Apple Watch Series 10", brand="Apple", price=49999, battery="36 Hours"),
    SmartWatch(name="Galaxy Watch 8", brand="Samsung", price=32999, battery="40 Hours"),
    SmartWatch(name="OnePlus Watch 3", brand="OnePlus", price=24999, battery="100 Hours"),
    SmartWatch(name="Nothing Watch Pro", brand="Nothing", price=15999, battery="120 Hours"),
    SmartWatch(name="Noise ColorFit Ultra", brand="Noise", price=4999, battery="7 Days"),
    SmartWatch(name="boAt Xtend", brand="boAt", price=2999, battery="7 Days"),
    SmartWatch(name="Fire-Boltt Ninja", brand="Fire-Boltt", price=2499, battery="6 Days"),
    SmartWatch(name="Titan Smart 3", brand="Titan", price=8999, battery="5 Days"),
    SmartWatch(name="Fastrack Revoltt", brand="Fastrack", price=6999, battery="5 Days"),
    SmartWatch(name="Amazfit GTR 4", brand="Amazfit", price=16999, battery="14 Days"),
]

# -----------------------------
# Headphones
# -----------------------------
headphones = [
    Headphone(name="Sony WH-1000XM6", brand="Sony", price=34999, wireless="Yes"),
    Headphone(name="AirPods Max", brand="Apple", price=59999, wireless="Yes"),
    Headphone(name="JBL Tune 770NC", brand="JBL", price=8999, wireless="Yes"),
    Headphone(name="boAt Rockerz 550", brand="boAt", price=2499, wireless="Yes"),
    Headphone(name="Realme Buds Air 7", brand="Realme", price=3999, wireless="Yes"),
    Headphone(name="Nothing Ear", brand="Nothing", price=8999, wireless="Yes"),
    Headphone(name="OnePlus Buds Pro 3", brand="OnePlus", price=11999, wireless="Yes"),
    Headphone(name="Samsung Galaxy Buds 3", brand="Samsung", price=13999, wireless="Yes"),
    Headphone(name="Skullcandy Crusher Evo", brand="Skullcandy", price=14999, wireless="Yes"),
    Headphone(name="Sennheiser HD 450BT", brand="Sennheiser", price=12999, wireless="Yes"),
]

# Insert only if tables are empty
if db.query(Mobile).count() == 0:
    db.add_all(mobiles)

if db.query(Laptop).count() == 0:
    db.add_all(laptops)

if db.query(Tablet).count() == 0:
    db.add_all(tablets)

if db.query(SmartWatch).count() == 0:
    db.add_all(smartwatches)

if db.query(Headphone).count() == 0:
    db.add_all(headphones)

db.commit()
db.close()

print("✅ Database seeded successfully!")