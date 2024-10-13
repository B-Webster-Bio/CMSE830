import streamlit as st
import pandas as pd
import numpy as np
import hiplot as hip
import os

st.write(f"Current working directory: {os.getcwd()}")
df = pd.read_csv('Project/Data/PlotFieldData.csv')

df_forplot = df.loc[df['GENOTYPE'] == 'B73',['NTREATMENT', 'A', 'E', 'gsw', 'Ci']]
st.scatter_chart(data=df_forplot, x = 'E', y = 'A', color='NTREATMENT')
#st.scatter_chart(data=df_forplot, x = 'KERNELDRYWT_PERPLANT', y = 'A', color='NTREATMENT')

st.write('B73 ONLY')
xp = hip.Experiment.from_dataframe(df_forplot)
st.components.v1.html(xp.to_html(), height=1500)