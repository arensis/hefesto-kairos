from flask import Flask, request, Response
from database.db import initialize_db
from services.station_services import *

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'port': 37017
}

initialize_db(app)

@app.route("/stations", methods=["GET"])
def get_stations():
    return Response(stations().to_json(), mimetype="application/json", status=200)

@app.route("/station/<id>", methods=["GET"])
def get_station():
    return Response(station(id).to_json(), mimetype="application/json", status=200)

@app.route("/station/create", methods=["POST"])
def create_station():
    body = request.get_jsong()
    id = saveStation(body)
    return Response({ 'station_id': str(id) }, mimetype="application/json", status=200)

@app.route("/station/<id>/measurements", methods=["POST"])
def create_station_measurement(id):
    body = request.get_jsong()
    measurement_id = update_measurements(id, body)
    return Response(
            { 'measurement_id': str(measurement_id), 'message': 'Mesasurement created'}, 
            mimetype="application/json", 
            status=200
        )
