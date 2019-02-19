import folium
import pandas

# Reading *.xlsx file with data
data = pandas.read_excel('datafile/population_2.xlsx')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
city = list(data['region_units'])
population = list(data['population_01.12.18'])
'''
from folium import plugins -- icon upgrade 
The color of the marker. You can use:

            ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']
'''


# Create func for color Markers Icons
def color_icon(population):
    if population < 1000000:
        return 'red'
    elif population <= population < 1500000:
        return 'orange'
    elif 1500000 <= population < 2000000:
        return 'green'
    else:
        return 'blue'


# Create Map
Starobilsk = [49.25, 38.91]

map = folium.Map(location=Starobilsk, zoom_start=8, tiles='Mapbox Bright')
for lat, lon, city, popul in zip(lat, lon, city, population):
    folium.Marker(location=[lat, lon], popup=city,
                  tooltip=city + ' ' + str(popul),
                  icon=folium.Icon(color=color_icon(popul))).add_to(map)

# Create LayerControl
map.add_child(folium.LayerControl())

# Save Map like ***.html file
map.save('Map.html')
