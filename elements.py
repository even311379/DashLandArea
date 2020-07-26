import dash_core_components as dcc
import pandas as pd

countries_data = pd.read_csv('CountriesInfo.csv')
country_name_data = pd.read_csv('CountriesNameTW.csv')
countries_options = []

for ename, code, lat, lon in zip(countries_data.name, countries_data.code, countries_data.latitude, countries_data.longitude):
    if code in country_name_data.code.tolist():
        try:
            name_tw = country_name_data[country_name_data.code == code].iloc[0][0]
        except:
            print(code)
    else:
        name_tw = ename
    countries_options.append({'label': name_tw, 'value': f"{lat}, {lon}"})

country_dropdown = dcc.Dropdown(
    options=countries_options,
    value='24.5, 121.5',
    id='country-dropdown',
    style={'width':'150px', 'font-size':'14px'}
)