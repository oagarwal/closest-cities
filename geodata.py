import pandas as pd
from re import sub
from haversine import haversine

class GeoData:

	def __init__(self):
		self.df = pd.read_csv('data/cities1000_new.txt',sep='\t',encoding='utf-8')
		self.df.set_index(['latitude','longitude'])
		self.df['name'] = self.df['name'].astype(unicode)
		self.df['name_lower'] = self.df['name_lower'].astype(unicode)

	def get_city_by_id(self,geonameid):
		return self.df.loc[self.df['geonameid'] == geonameid]

	def get_city_by_coordinates(self,latitude,longitude,offset):
        	return self.df.loc[(self.df['latitude'] < latitude+offset) & (self.df['latitude'] > latitude-offset) & (self.df['longitude'] < longitude+offset) & (self.df['longitude'] > longitude-offset)]

	def get_city_by_coordinates_and_country(self,latitude,longitude,offset,country_code):
		return self.df.loc[(self.df['latitude'] < latitude+offset) & (self.df['latitude'] > latitude-offset) & (self.df['longitude'] < longitude+offset) & (self.df['longitude'] > longitude-offset) & (self.df['country_code'] == country_code)]
	
	def get_city_by_name(self,name):
		name = sub(r"\s+", '|', name.lower())
		return self.df.loc[self.df['name_lower'].str.contains(name)]#[['geonameid','name','country_code','latitude','longitude']]

	def get_k_closest_cities(self,geonameid,k,same_country):
		given_city = self.get_city_by_id(geonameid)
		if len(given_city) == 0:
			return None
		else:
			latitude = given_city.iloc[0]['latitude']
			longitude = given_city.iloc[0]['longitude']
			country_code = given_city.iloc[0]['country_code']

			closest_cities = []
			for offset in xrange(1,6):
				if same_country:
					temp_df = self.get_city_by_coordinates_and_country(latitude,longitude,offset,country_code)
				else:
					temp_df = self.get_city_by_coordinates(latitude,longitude,offset)
				if len(temp_df)>k:
					break
				
			for index,row in temp_df.iterrows():
				closest_cities.append((row[['geonameid','name','country_code','latitude','longitude']],haversine((latitude,longitude),(row['latitude'],row['longitude']),miles=True)))

			return sorted(closest_cities,key=lambda x:x[1])[:min(k+1,len(closest_cities))]

