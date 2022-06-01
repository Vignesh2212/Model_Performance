import os
import streamlit as st
import numpy as np

# Custom imports
from multipage import MultiPage
from pages import define_windows, data_upload, metadata, machine_learning, data_visualize, redundant

# Create an instance of the app
app = MultiPage()

# Add all your application here
app.add_page("Define Time Window", define_windows.app)
app.add_page("Upload Data", data_upload.app)
app.add_page("Change Metadata", metadata.app)
app.add_page("Machine Learning", machine_learning.app)
app.add_page("Data Analysis",data_visualize.app)
app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
