
#!/usr/bin/python
# -*- coding: utf-8 -*-
import dash 
import dash_core_components as dcc 
import dash_html_components as html 


import sys 

print(sys.prefix)

app = dash.Dash()

app.layout = html.Div('Dashboard')

if __name__ == '__main__': 
	app.run_server(debug=True)