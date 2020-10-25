import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="my map")


def color_picker(el):
    if el < 1000:
        return 'green'
    elif el < 3000:
        return 'orange'
    else:
        return 'red'


for i, j, k in zip(lat, lon, elev):

    fg.add_child(folium.Marker(
        location=[i, j], popup=str(k) + 'm', icon=folium.Icon(color=color_picker(k))))

fg.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.save("map_prac.html")
