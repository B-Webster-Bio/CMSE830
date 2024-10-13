import streamlit as st
import pandas as pd
import numpy as np
import hiplot as hip
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Gas Exchange in Corn Hybrids')
st.image('Project/Supp/LeafGasEx.png', caption = 'Gas exchange through leaf stomata')

st.subheader('Gas exchange can be measured by a Licor')
st.image('Project/Supp/Licor.png', caption = 'Licor 6800 measuring plant in the field')
# Note that when hosted on community cloud the root directory defaults to the top level of github dir
md = ''' * A = CO2 assimilation rate (µmol CO2 m⁻² s⁻¹)  
 * E = Transpiration of H2O (mol H2O m⁻² s⁻¹)  
 * Gsw = stomatal conductance (mol H2O m⁻² s⁻¹)  
 * Ci = interceullar CO2 concentration ready for assimilation (ppm)
'''
st.markdown(md)

df = pd.read_csv('Project/Data/PlotFieldData.csv')

df_forplot = df.loc[df['GENOTYPE'] == 'B73',['NTREATMENT', 'A', 'E', 'gsw', 'Ci']]
f1 = sns.pairplot(df_forplot, hue = 'NTREATMENT')
st.pyplot(fig = f1)

st.write('B73 ONLY')
xp = hip.Experiment.from_dataframe(df_forplot)
st.components.v1.html(xp.to_html(), height=1500)