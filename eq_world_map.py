from fileinput import filename
import plotly.express as ex
import json

lons, lats = [], []
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dict = all_eq_data['features']
for eq_dice in all_eq_dict:
    lon = eq_dice['geometry']['coordinates'][0]
    lat = eq_dice['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)

fig = ex.scatter(
    x = lons,
    y = lats,
    labels={'x': '经度', 'y': '纬度'},
    range_x = [-200, 200],
    range_y = [-90, 90],
    width = 800,
    height = 800,
    title = '全球地震散点图'
)
fig.write_html('global_earthquakes.html')
fig.show()