from flask import Flask, request, Response, jsonify
from database.services.kairos_database_service import initialize_db
from services.station_services import *

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'port': 27017
}

initialize_db(app)

@app.route("/stations", methods=["GET"])
def get_stations():
    return handleGetRequest(stations())

@app.route("/station/<id>", methods=["GET"])
def get_station(id):
    return handleGetRequest(station(id))

@app.route("/station/create", methods=["POST"])
def create_station():
    body = request.get_json()
    id = saveStation(body)
    return {'station_id': str(id) }, 201

@app.route("/station/<id>/measurements", methods=["PUT"])
def add_new_measurement_to_station(id):
    body = request.get_json()
    station = update_measurements(id, body)
    if(station != None):
        return Response(
            {'message': 'Mesasurement created'}, 
            mimetype="application/json", 
            status=201
        )
    else:
        return { 'message': 'Internal server error'}, 500
        
@app.route("/station/<id>", methods=["DELETE"])
def delete_station(id):
    deleteStation(id)
    return "Station has been deleted", 201