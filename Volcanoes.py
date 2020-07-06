import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
map = folium.Map(location = [38.58,-99.09],zoom_start = 6, titles = " Stammen Terrain")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <= 3000:
        return  'orange'
    else:
        return 'red'

fg = folium.FeatureGroup(name = "My Map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location = [lt,ln], popup = str(el) + " m", icon = folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Volcanoes.html")
