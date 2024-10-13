import streamlit as st
import pandas as pd
import numpy as np
import hiplot as hip
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Gas Exchange in Corn Inbreds')
md = '''"Breathing" or gas exchange of Carbon Dioxide (CO2) and water (H2O) through leaf stomata is an important process in plant biology that is 
associated with how much carbon and water a plant is processing. Nitrogen fertilizer is an important agricultural input that influences 
the total amount of corn grain production. Gas exchange and grain yield were collected from a panel of 105 maize inbreds in high and low N treatments. 
Understanding how gas exchange traits and yield change between N treatments over a diverse population of maize genotypes will enable better breeding for effecient corn lines.
'''
st.markdown(md)


col1, col2 = st.columns(2)
with col1:
    st.image('Project/Supp/LeafGasEx.png', caption = 'Gas exchange through leaf stomata')

with col2:
    st.header("Gas exchange parameters")
    st.markdown("* A = CO2 assimilation rate (µmol CO2 m⁻² s⁻¹)")
    st.markdown("* E = Transpiration of H2O (mol H2O m⁻² s⁻¹)")
    st.markdown("* gsw = stomatal conductance to H2O (mol H2O m⁻² s⁻¹)")
    st.markdown("* Ci = interceullar CO2 concentration ready for assimilation (ppm)")

st.subheader('Gas exchange can be measured by a Licor')
st.image('Project/Supp/Licor.PNG', caption = 'Licor 6800 measuring plant leaf in the field')

# Note that when hosted on community cloud the root directory defaults to the top level of github dir
df = pd.read_csv('Project/Data/PlotFieldData.csv')

df_subpop = df.drop_duplicates(subset='GENOTYPE')
f1 = sns.displot(data=df_subpop, x = 'SUBPOPULATION', hue = 'SUBPOPULATION', kind='hist')
f1.set_xticklabels(rotation = 80)
st.pyplot(fig = f1)
st.markdown("____")


df_b73 = df.loc[df['GENOTYPE'] == 'B73',['NTREATMENT', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]
df_forplot = df.loc[:,['NTREATMENT', 'GENOTYPE', 'SUBPOPULATION', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]
f2 = sns.pairplot(df_forplot, hue = 'NTREATMENT')
st.pyplot(fig = f2)

# 
xp = hip.Experiment.from_dataframe(df_forplot)
st.components.v1.html(xp.to_html(), height=1500)