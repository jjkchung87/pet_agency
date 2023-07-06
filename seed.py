from models import Pet, db
from app import app 

db.drop_all()
db.create_all()

defaultURL = "https://media.istockphoto.com/id/508410282/photo/yorkshire-sitting-in-front-of-a-white-background.jpg?s=612x612&w=0&k=20&c=SH4uBQh78oGgsN4lAJsr9CqASlh7zBD_44fZbv46u2M="

arlo = Pet(name="Arlo", species="dog", photoUrl = defaultURL, age = 3, notes="Cutest dog in the world. Well behaved.", available=False )
willow = Pet(name="Willow", species="dog", photoUrl = defaultURL, age = 3, notes="Extremely hyper.", available=True )
spike = Pet(name="Spike", species="porcupine", photoUrl = defaultURL, age = 10, available=True )
roy = Pet(name="Roy", species="cat", photoUrl = defaultURL, age = 1, available=False )
goldie = Pet(name="Goldie", species="cat", photoUrl = defaultURL, age = 1, notes="Pretty useless.", available=True )
peter = Pet(name="Peter", species="porcupine", photoUrl = defaultURL, age = 5, notes="I think not venomous...", available=True )

db.session.add_all([arlo, willow, spike, roy, goldie, peter])
db.session.commit()
