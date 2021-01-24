from database.services.kairos_database_service import db

class Location(db.EmbeddedDocument):
    name = db.StringField(required=True)
    indoor = db.BooleanField(required=True)
    city = db.StringField(required=True)
    latitude = db.DecimalField(precision=6)
    longitude = db.DecimalField(precision=6)