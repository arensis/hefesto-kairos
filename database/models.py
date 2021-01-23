from .db import db

class Station(db.Document):
    date = db.DateTimeField(default=datetime.utcnow)
    location = db.ReferenceField(Location)
    measurements = db.ListField(ReferenceField(Measurement))

class Location(db.Document):
    name = db.StringField(required=True)
    indoor = db.BooleanField(required=True)
    city = db.StringField(required=True)
    latitude = db.DecimalField(precision=6)
    longitude = db.db.DecimalField(precision=6)

class Measurement(db.Document):
    date = db.DateTimeField(default=datetime.utcnow)
    temperature = db.FloatField(required=True)
    humidity = db.FloatField()
    airPressure = db.FloatField()
