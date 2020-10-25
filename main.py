import folium

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[
    38.5, -99.1], popup="I will work at Google", icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("map_prac.html")
