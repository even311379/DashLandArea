import dash_core_components as dcc
import pandas as pd

countries_data = pd.read_csv('CountriesInfo.csv')
countries_options = []

for index, row in countries_data.iterrows():
    countries_options.append({'label': row['name'], 'value': f"{row['latitude']}, {row['longitude']}"})

country_dropdown = dcc.Dropdown(
    options=countries_options,
    value='24.5, 121.5',
    id='country-dropdown',
    style={'width':'150px', 'font-size':'14px'}
)