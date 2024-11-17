import json
from pathlib import Path
import plotly.express as px

path=Path("C:/Users/rahul/OneDrive/Desktop/Files/python_works/Data_Visualization/eq_data_1_day_m1.geojson")
lines=path.read_text("utf-8")
all_eq_data=json.loads(lines)
  
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, eq_titles=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)


print(mags[:10])
print(lons[:5])
print(lats[:5])

title="Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
color=mags,color_continuous_scale='Viridis',labels={'color':'Magnitude'},projection='natural earth',hover_name=eq_titles,)
fig.show()

