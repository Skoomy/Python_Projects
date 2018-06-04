#!/bin/bash


pip uninstall dash.ly
pip uninstall dash
pip uninstall dash-renderer
pip uninstall dash-html-components
pip uninstall dash-core-components
pip uninstall plotly


# install file 

pip install dash==0.21.1  # The core dash backend
pip install dash-renderer==0.13.0  # The dash front-end
pip install dash-html-components==0.11.0  # HTML components
pip install dash-core-components==0.23.0  # Supercharged components
pip install plotly --upgrade  # Latest Plotly graphing library
