import pandas as pd

df = None

def read_data():
	df = pd.read_csv('data/cities1000.txt',header=None,names=['geonameid','name','asciiname','alternatenames','latitude','longitude','feature_class','feature_code','country_code','cc2','admin1_code','admin2_code','admin3_code','admin4_code','population','elevation','dem','timezone','modification_date'],sep='\t',encoding='utf-8')

def get_city_by_id(geonameid):
	return df.loc[df['geonameid'] == geonameid]

def get_city_by_coordinates(latitude,longitude,offset):
        return df.loc[(df['latitude'] < latitude+offset) & (df['latitude'] > latitude-offset) & (df['longitude'] < longitude+offset) & (df['longitude'] > longitude-offset)]

