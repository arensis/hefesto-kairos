from flask import Flask

app = Flask(__name__)


@app.route("/")
def stations():
    return app.response_class(
        response=open("mocks/stations.json", "r").read(),
        status=200,
        mimetype="application/json",
    )


@app.route("/hefesto/", methods=["POST"])
def save_register():
    return app.response_class(status=201)
