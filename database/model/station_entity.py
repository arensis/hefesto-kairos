from database.services.kairos_database_service import db
from database.model.location_entity import Location
from database.model.measurement_entity import Measurement

class Station(db.Document):
    createdDate = db.StringField()
    location = db.EmbeddedDocumentField(Location)
    measurements = db.EmbeddedDocumentListField(Measurement)
