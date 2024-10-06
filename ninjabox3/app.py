from flask import Flask, render_template, jsonify
from services.courier_service import get_simulation_data

app = Flask(__name__)

# random cimek
addresses = [
    {'address': 'Station A', 'lat': 47.0931, 'lon': 17.9070},
    {'address': 'Station B', 'lat': 47.0970, 'lon': 17.9070},
    {'address': 'Station C', 'lat': 47.0935, 'lon': 17.9025},
    {'address': 'Station D', 'lat': 47.0910, 'lon': 17.9000},
]

@app.route('/')
def index():
    simulation_data = get_simulation_data(addresses)
    return render_template('optimize_route.html', simulation_data=simulation_data)

if __name__ == '__main__':
    app.run(debug=True)
