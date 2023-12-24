import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Seftian Setia

ini adalah Dashboard sederhana mengingat waktu tinggal 1 hari lagi
"""



st.title('E-Bike Sharing Analysis')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
  st.header("Hari atau Jam dengan penyewa terbanyak?")
  st.image('jam efektif.png')


with tab2:
  st.header("Musim Terbaik dan Cuaca yang mendukung?")
  st.image('Musim terbaik.png')
  st.image('berdasar cuaca.png')

with tab3:
  st.header("Workday atau Weekend yang terbanyak penyewanya?")
  st.image('rata arat pemakaian.png')
