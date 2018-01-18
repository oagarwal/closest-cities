#! /usr/bin/env python
from geodata import GeoData
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/closestcities')
def closestcities():
	geonameid  = int(request.args.get('geonameid'))
	k = int(request.args.get('k'))
	same_country = True if request.args.get('country')=='yes' else False
	print(same_country)
	gd = GeoData()	
	return str(gd.get_k_closest_cities(geonameid,k,False))

@app.route('/city')
def city():
        name  = request.args.get('name')
        gd = GeoData()
        return str(gd.get_city_by_name(name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
