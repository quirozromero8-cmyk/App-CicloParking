# CicloParking

Web application developed with Streamlit to find the bike parking locations closest to the user's position in Bogotá. Bike parking spots are ranked into two categories: Silver and Gold. These categories take into account the quality of the bike racks and the parking infrastructure.

## Features

- Detects user location in real time
- Calculates Manhattan distances
- Recommends the 3 closest bike parking locations
- Prioritizes Gold category locations
- Interactive map with Folium

##  Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Folium
- GeoPandas
- Scikit-learn

##  Dataset:

Source: Datos Abiertos Bogotá - Cicloparqueadero

Size: 361 Parking lots

Variables: X, Y, OBJECTID,ID_CICLOPARQUEDERO, CIV, CLASECICLOP, NOMBRECICLOP, SECTORCICLOP, TIPOUSUARIOCICLOP, LOCALIDAD,
DIRECCIONCICLOP, HORARIOCICLOP, TIPOLOGIACICLOP, CUPOCICLOP, SELLOCICLOP, ANOCICLOP, GLOBALID. 

## Project Structure:

App Cicloparking/
│
├── app.py
├── Cicloparqueadero.csv
├── Exploracion.ipynb
├── README.md
└── requirements.txt

## Technologies Implemented:

- Python
- Pandas
- geopandas
- folium
- Streamlit
- Streamlit-folium
- Streamlit-js_eval

## How to Run

### Clone the repository
```bash

git clone https://github.com/quirozromero8-cmyk/CicloParking.git
cd CicloParking
```
### Create a virtual environment

```bash
python -m venv venv
```
### Activate the virtual environment
```bash
.\venv\Scripts\activate
```
### Install dependencies
```bash
pip install -r requirements.txt
````
### Run the Streamlit app
```bash
streamlit run app.py
```
### Open in your browser
```bash
http://localhost:8501
```
## Autor:

Tomas Eduardo Quiroz
