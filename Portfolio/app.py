
#!/usr/bin/env python3

import sys 
import os 

## DASH dependencies
import dash_core_components as dcc 
import dash_html_components as html 
import dash 


modulename = 'dash'
if modulename not in sys.modules:
    print('You have not imported the {} module',format(modulename))



app = dash.Dash(__name__)

# focus on dataFin 
app.layout = html.Div('Dashboard')

if __name__ == '__main__': 
	app.run_server(debug=True)