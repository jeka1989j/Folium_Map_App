import folium


# Create Map
Starobilsk = [49.25,38.91]

map = folium.Map(location=Starobilsk, zoom_start=8, tiles='Mapbox Bright')
folium.Marker(location=Starobilsk, popup='Starobilsk', tooltip='Starobilsk',
              icon=folium.Icon(color='red')).add_to(map)


# Create LayerControl
map.add_child(folium.LayerControl())


# Save Map like ***.html file
map.save('Map.html')