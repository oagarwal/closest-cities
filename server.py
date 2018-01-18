#! /usr/bin/env python
from geodata import GeoData
import pandas as pd
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
	gd = GeoData()
	results = gd.get_k_closest_cities(geonameid,k,same_country)

	if not results:
		return "Invalid geo id"
	
	for row,dist in results:
		if dist == 0:
			outputString = '<html><head><title>'+str(geonameid)+'</title><style>table {font-family:arial,sans-serif;border-collapse:collapse;width:50%;margin-left:auto;margin-right:auto;}td, th { border: 1px solid #dddddd; text-align: left; padding: 8px;}tr:nth-child(even) { background-color: #dddddd;} </style></head><body align=center><br/>Results for '+row['name']+' in '+row['country_code']+' at '+str(row['latitude'])+','+str(row['longitude'])+'<br/><br/><table><tr><th>ID</th><th>Name</th><th>Country Code</th><th>Latitude</th><th>Longitude</th><th>Distance in miles</th></tr>'
		else:
			outputString += '<tr><td>'+str(row['geonameid'])+'</td><td>'+row['name']+'</td><td>'+row['country_code']+'</td><td>'+str(row['latitude'])+'</td><td>'+str(row['longitude'])+'</td><td>'+str(dist)+'</td></tr>'
	outputString += '</table></body></html>'
	return outputString

@app.route('/city')
def city():
        name  = request.args.get('name')
        gd = GeoData()
	results = gd.get_city_by_name(name)
	outputString = '<html><head><title>'+name+'</title><style>table {font-family:arial,sans-serif;border-collapse:collapse;width:50%;margin-left:auto;margin-right:auto;}td, th { border: 1px solid #dddddd; text-align: left; padding: 8px;}tr:nth-child(even) { background-color: #dddddd;} </style></head><body><table><tr><th>ID</th><th>Name</th><th>Country Code</th><th>Latitude</th><th>Longitude</th></tr>'
	for index,row in results.iterrows():
		outputString += '<tr><td>'+str(row['geonameid'])+'</td><td>'+row['name']+'</td><td>'+row['country_code']+'</td><td>'+str(row['latitude'])+'</td><td>'+str(row['longitude'])+'</td></tr>'
	outputString += '</table></body></html>'
        return outputString

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
