import streamlit as st
import numpy as np
import pandas as pd
from pages import utils, data_upload

# @st.cache
def app():
    st.markdown("## Define Model time periods")

    # Upload the dataset and save as csv
    num_time_period = 0

    num_time_period = st.slider("#No of time periods:",1,5,1)


    st.write("\n")
    time_period= []
    for ctr in range(num_time_period):
        time_period.append(st.text_input("Time period #"+str(ctr+1)+": "))


    st.write("\n")
    if st.button("Display all time"):
        st.write("Entered time periods:",", ".join(time_period))

    st.session_state.time_period = time_period
    # if st.button("Next page"):
    #
    #     data_upload.app()
