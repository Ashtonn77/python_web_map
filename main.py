import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="my map")

# [[38.5, -99.1], [37.1, -98.35]]:
for i, j, k in zip(lat, lon, elev):

    fg.add_child(folium.Marker(
        location=[i, j], popup=str(k) + 'm', icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("map_prac.html")
