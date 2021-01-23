from database.models import Station, Location, Measurement

def stations():
    return Station.objects()

def station(id):
    return Station.objects().get(id=id)

def saveStation(body):
    location = saveLocation(body.location)
    station = Station(measurements=[])
    station.location = location
    station.save()
    return station.id

def saveLocation(location_json):
    location = Location(**location_json).save()
    return location

def update_measurements(station_id, measurement_json):
    station = Station.objects().get(id=id)
    measurement = Measurement(**measurement_json).save()
    station.update_one(push__measurements=measurement)
    return measurment.id

