import folium
import pandas

# Reading *.xlsx file with data 
data = pandas.read_excel('datafile/population_2.xlsx')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
city = list(data['region_units'])

'''
from folium import plugins -- icon upgrade 
The color of the marker. You can use:

            ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']
'''

# Create Map
Starobilsk = [49.25, 38.91]

map = folium.Map(location=Starobilsk, zoom_start=8, tiles='Mapbox Bright')
for lat, lon, city in zip(lat, lon, city):
    folium.Marker(location=[lat, lon], popup=city, tooltip=city,
                  icon=folium.Icon(color='red')).add_to(map)

# Create LayerControl
map.add_child(folium.LayerControl())

# Save Map like ***.html file
map.save('Map.html')
