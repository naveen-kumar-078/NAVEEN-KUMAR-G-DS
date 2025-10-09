import pandas as nkg
import matplotlib.pyplot as pp
city=nkg.read_csv("Bangalore_1990_2022_BangaloreCity.csv")
print(city.isnull().sum())
city['tavg']=city['tavg'].fillna(city['tavg'].mean())
city['tmax']=city['tmax'].fillna(city['tmax'].mean())
city['tmin']=city['tmin'].fillna(city['tmin'].mean())
city['prcp']=city['prcp'].fillna(city['prcp'].mean())
print(city.isnull().sum())
city['time']=nkg.to_datetime(city['time'], format="%d-%m-%Y")
city['year']=city['time'].dt.year
city['month']=city['time'].dt.month
city['day']=city['time'].dt.day
yearly=city.groupby('year')['tavg'].mean().reset_index()
print(yearly)
pp.figure(figsize=(10, 5))
pp.plot(yearly['year'], yearly['tavg'], marker='p')
pp.plot(yearly['year'], yearly['tavg'], marker='p', color='orange')
pp.title('Year of  Average Temperature in Bangalore (1990-2022)')
pp.xlabel('Year')
pp.ylabel('Average Temperature (°C)')
pp.show()