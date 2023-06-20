import seaborn as sns
import pandas as pd
import matplotlib as plt
df = pd.read_csv('data/housing_features_v1.csv')

#insight in data distribution 
df.head()
df.describe()

#plot dependent variable 
plot = sns.countplot(x = 'SELECTIE', data = df)
df = pd.read_csv('Scriptie/data/housing_features_v1.csv')

#insight in data distribution 
df.head()
df.describe()

#plot dependent variable 
plot = sns.countplot(x = 'SELECTIE', data = df)
plt.show()
plot
matplotlib.use('TkAgg')
plt.use('TkAgg')
df = pd.read_csv('Scriptie/data/housing_features_v1.csv')

#insight in data distribution 
df.head()
df.describe()

#plot dependent variable 
plot = sns.countplot(x = 'SELECTIE', data = df)
plot

from matplotlib import pyplot as plt
df = pd.read_csv('Scriptie/data/housing_features_v1.csv')

#insight in data distribution 
df.head()
df.describe()

#plot dependent variable 
plot = sns.countplot(x = 'SELECTIE', data = df)
plt.show()
df.columns

df2 = df['identifica', 'rdf_seeals', 'oppervlakt', 'status', 'gebruiksdo',
       'openbare_r', 'huisnummer', 'huisletter', 'toevoeging', 'postcode',
       'woonplaats','pandidenti', 'pandstatus', 'fuuid','Fixed ge_1'].drop()
df2 = df.drop(['identifica', 'rdf_seeals', 'oppervlakt', 'status', 'gebruiksdo',
       'openbare_r', 'huisnummer', 'huisletter', 'toevoeging', 'postcode',
       'woonplaats','pandidenti', 'pandstatus', 'fuuid','Fixed ge_1'])
df2 = df.drop(['identifica', 'rdf_seeals', 'oppervlakt', 'status', 'gebruiksdo',
       'openbare_r', 'huisnummer', 'huisletter', 'toevoeging', 'postcode',
       'woonplaats','pandidenti', 'pandstatus', 'fuuid','Fixed ge_1'],axis = 1)
df2.head()
df2.max('Fixed geom')
df2['Fixed geom'].max()
df2['Fixed geom'].min()
df
df2.columns
x = df2['Huizenprij', 'UHI1', 'detailhand', 'Onderwijs',
       'horeca', 'zorg', 'kantoren', 'Fixed geom', 'OV','bouwjaar')
y = df2['SELECTIE']
x = df2['Huizenprij', 'UHI1', 'detailhand', 'Onderwijs',
       'horeca', 'zorg', 'kantoren', 'Fixed geom', 'OV','bouwjaar']
y = df2['SELECTIE']
x = df2.remove['SELECTIE]
x = df2.remove['SELECTIE']
x = df2.remove('SELECTIE')
x = df2.drop('SELECTIE')
x = df2.drop('SELECTIE')
x = df2.drop(['SELECTIE'])
