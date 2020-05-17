# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:35:26 2020


farid_map.py

@author: Farid Khafizov
"""

import folium
import os
# import json
import numpy as np
import pandas as pd

wd = 'C:\\Users\\Farid Khafizov\\conda\\pyviz\\'
os.chdir(wd)
# Create map object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=14)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icons
CellTowerIcon = folium.features.CustomIcon(wd+'icons/cell_tower.png', 
                                           icon_size=(30, 30))
UEIcon = folium.features.CustomIcon(wd+'icons/mobile-alt-solid.svg', 
                                           icon_size=(50, 50))
TIcon = folium.features.CustomIcon(wd+'icons/logo.png', 
                                           icon_size=(50, 50))


x0 =  42.375140
y0 = -71.0589
longs = [x0, x0+0.01, x0-0.01,  x0+.013]
lats = [y0, y0+0.02, y0+0.015, y0-.003]

df_coordinates = pd.DataFrame(  {'x':longs, 'y':lats}  )
eNB_coords = np.array(df_coordinates.iloc[0])
UElocs = df_coordinates.iloc[1:]

folium.Marker( eNB_coords,
              popup='<strong>Location Five</strong>',
              tooltip=str(eNB_coords),
              icon=CellTowerIcon).add_to(m)

for k in range(UElocs.shape[0]):
    # print(k)      
    prompt = 'UE_'+str(k)+' '+str(np.array(UElocs.iloc[0]))
    folium.Marker( location = np.array(UElocs.iloc[k]), 
                   tooltip = prompt,
              icon=folium.Icon(color='green', 
                               icon = 'mobile' ,prefix='fa',
                              )).add_to(m)
    
    # ROUNDS=5
    # coordinates = str(  np.round( UElocs['x'][k] , ROUNDS)  ) + \
    #                ', ' + \
    #              str(  np.round( UElocs['y'][k] , ROUNDS)  )   
    # folium.Marker(location=[  UElocs['x'][k],   UElocs['y'][k]  ], 
    #               tooltip=coordinates,
    #           icon=folium.Icon(color='green', 
    #                            icon = 'mobile' ,prefix='fa',
    #                           )).add_to(m)


# Circle marker
folium.CircleMarker(
    location = eNB_coords,
    radius = 50,
    popup= str(eNB_coords),
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

folium.Circle(
    location = eNB_coords,
    radius = 2500,
    popup= str(eNB_coords),
    color='red',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Generate map
m.save(wd+'farid_map.html')
#%%
help(folium.Icon)