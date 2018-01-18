import pandas as pd

df = pd.read_csv('data/cities1000.txt',header=None,names=['geonameid','name','asciiname','alternatenames','latitude','longitude','feature_class','feature_code','country_code','cc2','admin1_code','admin2_code','admin3_code','admin4_code','population','elevation','dem','timezone','modification_date'],sep='\t',encoding='utf-8')
df['name_lower'] = df.apply(lambda row: row['name'].lower(),axis=1)
df.to_csv('data/cities1000_new.txt',header=['geonameid','name','asciiname','alternatenames','latitude','longitude','feature_class','feature_code','country_code','cc2','admin1_code','admin2_code','admin3_code','admin4_code','population','elevation','dem','timezone','modification_date','name_lower'],sep='\t',encoding='utf-8')
