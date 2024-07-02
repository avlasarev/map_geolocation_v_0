from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='../web', static_url_path='')


@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/reverse-geocode', methods=['GET'])
def reverse_geocode():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}"

    response = requests.get(url)
    data = response.json()

    neighborhood = data.get('address', {}).get('neighbourhood') or data.get('address', {}).get('suburb') or data.get(
        'address', {}).get('city_district')

    if neighborhood:
        return jsonify({'neighborhood': neighborhood})
    else:
        return jsonify({'error': 'Neighborhood not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
