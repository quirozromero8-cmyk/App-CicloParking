import pandas as pd
import folium
import geopandas as gpd
import streamlit as st
from streamlit_js_eval import get_geolocation
from streamlit_folium import st_folium
import requests
loc = get_geolocation()

df = pd.read_csv("Cicloparqueadero.csv")

df['CLASECICLOP'] = df['CLASECICLOP'].replace({'F': 1, 'I': 2}).astype(int)
df['SELLOCICLOP'] = df['SELLOCICLOP'].replace(2, 3)

df["Categoria"] = (
    df["CLASECICLOP"] + df["SELLOCICLOP"]
).apply(lambda x: "Oro" if x == 4 else "Plata")

df_parqueaderos = pd.DataFrame({
    "X": df["X"],
    "Y": df["Y"],
    "Nombre": df["NOMBRECICLOP"],
    "Direccion": df["DIRECCIONCICLOP"],
    "Horarios": df["HORARIOCICLOP"],
    "Categoria": df["Categoria"]
})

gdf = gpd.GeoDataFrame(
    df_parqueaderos,
    geometry=gpd.points_from_xy(df_parqueaderos["X"], df_parqueaderos["Y"]),
    crs="EPSG:4326"
)


#Ubication user
if loc:
    user_lat = loc['coords']['latitude']
    user_lon = loc['coords']['longitude']


mapa = folium.Map(location=[user_lat, user_lon], tiles="CartoDB positron", zoom_start=15)

#Distance in m user - parking
gdf["Distancia_m"] = (((gdf["Y"] - user_lat).abs() + (gdf["X"] - user_lon).abs()) * 111000).astype(int)

# Recomendations based on category and distance
oro   = gdf[gdf["Categoria"] == "Oro"].sort_values("Distancia_m")
otros = gdf[gdf["Categoria"] != "Oro"].sort_values("Distancia_m")
recomendados = pd.concat([oro.head(1), otros.head(2)]).reset_index(drop=True) #Olny the 3 best parkings


folium.Marker(
    location=[user_lat, user_lon],
    tooltip="Ubicacion actual",
    icon=folium.Icon(color='red', icon='user', prefix='fa')
).add_to(mapa)

for _, row in recomendados.iterrows():
    color = "lightblue" if row["Categoria"] == "Oro" else "lightgray"
    folium.Marker(
        location=[row["Y"], row["X"]],
        tooltip=f"Nombre: {row['Nombre']}<br>Dirección: {row['Direccion']}<br>Horario: {row['Horarios']}<br>Categoría: {row['Categoria']}",
        icon=folium.Icon(color=color, icon="bicycle", prefix="fa")
    ).add_to(mapa)

# App
st.title("CicloParking")
st.write("Encuentra el cicloparqueadero más cercano a ti.")

tabla = recomendados[["Nombre", "Direccion"]].rename(columns={"Nombre": "Ubicacion", "Direccion": "Dirección"}.hide_index=True)

colum1, colum2 =st.columns(2)

with colum1:
    st.metric(label="Parkeadero Recomendado", value = recomendados.iloc[0]["Nombre"])
    st.metric(label="Direccion", value = recomendados.iloc[0]["Direccion"])

with colum2:
    st.metric(label="Horario de Atencion", value = recomendados.loc[0, "Horarios"])

st.write(tabla)

st_folium(mapa, width=700)