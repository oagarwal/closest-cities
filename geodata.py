import pandas as pd

class GeoData:

	def __init__(self):
		self.df = pd.read_csv('data/cities1000.txt',header=None,names=['geonameid','name','asciiname','alternatenames','latitude','longitude','feature_class','feature_code','country_code','cc2','admin1_code','admin2_code','admin3_code','admin4_code','population','elevation','dem','timezone','modification_date'],sep='\t',encoding='utf-8')
		self.df.set_index(['latitude','longitide'])

	def get_city_by_id(geonameid):
		return self.df.loc[self.df['geonameid'] == geonameid]

	def get_city_by_coordinates(latitude,longitude,offset):
        	return self.df.loc[(self.df['latitude'] < latitude+offset) & (self.df['latitude'] > latitude-offset) & (self.df['longitude'] < longitude+offset) & (self.df['longitude'] > longitude-offset)]

