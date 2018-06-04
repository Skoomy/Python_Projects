
#!/usr/bin/env python3

import dash 
#import dash_core_components as dcc 
#import dash_html_components as html 


app = dash.DASH()

app.layout = html.Div('Dashboard')

if __name__ == '__main__': 
	app.run_server(debug=True)