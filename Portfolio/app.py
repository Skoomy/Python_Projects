
<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: utf-8 -*-
import dash 
import dash_core_components as dcc 
import dash_html_components as html 


import sys 
=======
#!/usr/bin/env python3

import sys 
import os 

## DASH dependencies
import dash_core_components as dcc 
import dash_html_components as html 
import dash 
>>>>>>> 008573f9c84f85bf9320ec9771ff0bceae499789

print(sys.prefix)

<<<<<<< HEAD
app = dash.Dash()
=======
modulename = 'dash'
if modulename not in sys.modules:
    print('You have not imported the {} module',format(modulename))



app = dash.Dash(__name__)
>>>>>>> 008573f9c84f85bf9320ec9771ff0bceae499789

# focus on dataFin 
app.layout = html.Div('Dashboard')

if __name__ == '__main__': 
	app.run_server(debug=True)