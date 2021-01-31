from database.model.station_entity import Station
from database.model.measurement_entity import Measurement
from database.model.location_entity import Location
from flask import Response
import datetime


def stations():
    return Station.objects()


def station(id):
    return Station.objects().get(id=id)


def getDateTimeToString():
    return datetime.datetime.utcnow().strftime("%d/%m/%y %H:%Mh")


def saveStation(body):
    location = saveLocation(body)
    station = Station(measurements=[])
    station.location = location
    station.createdDate = getDateTimeToString()
    station.save()
    print(station.id)
    return station.id


def saveLocation(location_json):
    location = Location(**location_json)
    return location


def update_measurements(station_id, measurement_json):
    station = Station.objects().get(id=station_id)
    print(station)
    measurement = Measurement(**measurement_json)
    measurement.date = getDateTimeToString()
    print(measurement)
    station.measurements.append(measurement)
    print(station)
    return station.save()


def deleteStation(id):
    Station.objects().get(id=id).delete()


def handleGetRequest(object):
    if object != None:
        return Response(object.to_json(), mimetype="application/json", status=200)
    else:
        return "Source not found", 404
