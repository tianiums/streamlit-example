import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""



st.title('E-Bike Sharing Analysis')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
  st.header("Hari atau Jam dengan penyewa terbanyak?")
  st.image('jam efektif.png')


with tab2:
  st.header("Musim Terbaik dan Cuaca yang mendukung?")
  st.image('Musim terbaik.png')
  st.image('berdasarkan cuaca.png')

with tab3:
  st.header("Workday atau Weekend yang terbanyak penyewanya?")
  st.image('rata arat pemakaian.png')
