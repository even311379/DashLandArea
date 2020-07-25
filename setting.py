import dash
import dash_bootstrap_components as dbc
from flask import Flask

external_scripts = []
external_styles = [dbc.themes.JOURNAL, "https://fonts.googleapis.com/css?family=Noto+Sans+TC|Noto+Serif&display=swap"]


app = dash.Dash(
    '土地面積計算',
    external_stylesheets= external_styles,
    external_scripts=external_scripts,
    meta_tags=[
        {"name": "viewport", "content":"width=device-width, initial-scale=1"},
        {"content_type":"text/html"}
    ],
)

app.title = '土地面積計算'

