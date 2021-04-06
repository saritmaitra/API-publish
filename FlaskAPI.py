from flask import request, jsonify
import flask, json, sys, traceback
from flask import make_response
from flask_restful import Api, Resource, reqparse
import requests

# Init
app = flask.Flask(__name__)
API = Api(app)

testdata = [
    {
        "date_of_news": "February 23, 2018",
        "title": "nGen_LUX is here",
        "hyperlink": "https://learn.colorfabb.com/ngen_lux-is-here/",
        "organizations_entity": [
            [2, "Kristaps Politis"],
        ],
        "person_entity": [[1, "David Payne"]],
    }
]


class prediction(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument("date_of_news")
        parser.add_argument("title")
        parser.add_argument("hyperlink")

        args = parser.parse_args()  # creates dict

        out = {"organizations_entity", "person_entity"}

        return out, 200


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p> Data is not available.</p>", 404


# Create a handler for our read (GET) people
def read():
    return [testdata[key] for key in sorted(testdata.keys())]


# @app.route("/", methods=["GET", "POST"])
# def home():
#     return """<h1>News_Content_Named_Entity_Recognition</h1>
# <p>A prototype API testing for LEONARD.</p>"""


@app.route("/", methods=["GET", "POST"])
def predict():
    return jsonify({"inference": testdata})


def add_resource(self, resource, *urls, **kwargs):
    API.add_resource(prediction, "/prediction", endpoint="prediction")

    if self.app is not None:
        self._register_view(self.app, resource, *urls, **kwargs)
    else:
        self.resources.append((resource, urls, kwargs))


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])  # This is for a command-line argument
    except:
        port = 8000  # If no port provided then the port will be set to 12345
    app.run(port=port, debug=True)


# This app can be run in a new  terminal of this directory (API can also be accessed from within the Python application)
# python run FastAPI.py

# For debugging and testing purposes, I used Postman


# Here employed requests module to define the URL to access and the body to send along with our HTTP request:
url = "http://127.0.0.1:8000/prediction"  # localhost and the defined port + endpoint
body = {
    "date_of_news": "February 23, 2018",
    "title": "nGen_LUX is here",
    "hyperlink": "https://learn.colorfabb.com/ngen_lux-is-here/",
}
response = requests.post(url, data=body)
response.json()
