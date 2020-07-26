import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
from dash.dependencies import Input, Output, State, ALL

import flask
import requests
import json
import shapely.geometry as sg

import style
from setting import app
from elements import  country_dropdown

server = app.server

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row('土地面積計算', className="h1 text-primary py-5", justify='center'),
        dbc.Row(
            [
                dbc.Col(
                    dl.Map([dl.TileLayer(url='http://mt0.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', maxZoom=20), dl.LayerGroup(id="drawing"), dl.LayerGroup([], id="polygons")],
                           id="map", style=style.map, center=(23.5, 120.5), zoom=8),
                    width=6, className='pl-5'
                ),
                dbc.Col(
                    [dbc.Row('', id='client_ip'),
                     dbc.Row(country_dropdown)]
                    , width=6, className='pr-5')
            ]
        ),
        dcc.Store(id="store", data=[])
    ]
    , fluid=True
)


@app.callback([Output("store", "data"), Output("drawing", "children"), Output("polygons", "children")],
              [Input("map", "click_lat_lng"), Input({'role': 'marker', 'index': ALL}, "n_clicks")],
              [State("store", "data"), State("polygons", "children")])
def map_click(click_lat_lng, n_clicks, data, polygons):
    trigger = dash.callback_context.triggered[0]["prop_id"]
    print(trigger)
    # The map was clicked, add a new point.
    if trigger.split(".")[1] == "click_lat_lng":
        if len(polygons) > 0:
            for polygon in polygons:
                # print(polygon['props']['positions'])
                sg_poly = sg.Polygon(polygon['props']['positions'])
                if (sg.Point(float(click_lat_lng[0]), float(click_lat_lng[1])).within(sg_poly)):
                    print('you are within existing polygon')
                    return data, '', polygons

        data.append(click_lat_lng)
        markers = [dl.CircleMarker(center=pos, id={'role': 'marker', 'index': i}) for i, pos in enumerate(data)]
        polyline = dl.Polyline(positions=data)
        drawing = markers + [polyline]
    # A marker was clicked, close the polygon and reset drawing.
    else:
        polygons.append(dl.Polygon(positions=data))
        data, drawing = [], []
    print(data, drawing, polygons)
    return data, drawing, polygons

@app.callback(Output('client_ip','children'),
              [Input('url', 'pathname')])
def OnRequest(url):
    ip = flask.request.remote_addr
    r = json.loads(requests.get(f'http://ip-api.com/json/{ip}').text)
    if 'lat' in r.keys():
        lat = r['lat']
        lon = r['lon']
        return f'your location is: {lat}, {lon}'
    else:
        return f"Can't get geo info from your ip ({ip})."

@app.callback(Output('map','center'),
              [Input('country-dropdown','value')])
def NavToCountry(value):
    if value == None:
        return (23.5, 120.5)
    return eval(value)

# @app.callback(Output('json-text', 'children'),
#               [Input('store','data')])
# def ShoeMapClickData:

if __name__ == "__main__":
    app.run_server(debug=True)