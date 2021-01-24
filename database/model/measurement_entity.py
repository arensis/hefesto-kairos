from database.services.kairos_database_service import db

class Measurement(db.EmbeddedDocument):
    date = db.StringField()
    temperature = db.FloatField(required=True)
    humidity = db.FloatField()
    airPressure = db.FloatField()