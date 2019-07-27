import os

from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
from dotenv import load_dotenv
from amadeus import Client, Location

app = Flask(__name__)
load_dotenv()


client = Client(
    client_id=os.environ['AMADEUS_API_KEY'],
    client_secret=os.environ['AMADEUS_API_SECRET']
)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search_flight():
    data = request.json
    flights = []
    try:
        locations = client.reference_data.locations.get(keyword=data['city'], subType=Location.ANY).data
    except Exception:
        locations = []
    if locations:
        try:
            flights = client.shopping.flight_destinations.get(origin=locations[0]["address"]["cityCode"]).data
        except Exception:
            flights = []
    return render_template('card.html', **{"flights": flights})


if __name__ == '__main__':
    app.debug = True
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
