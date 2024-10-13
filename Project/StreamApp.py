import streamlit as st
import pandas as pd
import numpy as np
import hiplot as hip
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Gas Exchange in Corn Inbreds')

col1, col2 = st.columns(2)

with col1:
    st.header("Conceptual graphic of gas exchange")
    st.image('Project/Supp/LeafGasEx.png', caption = 'Gas exchange through leaf stomata')

with col2:
    st.header("Gas exchange parameters")
    md = ''' * A = CO2 assimilation rate (µmol CO2 m⁻² s⁻¹)  
        * E = Transpiration of H2O (mol H2O m⁻² s⁻¹)  
        * gsw = stomatal conductance (mol H2O m⁻² s⁻¹)  
        * Ci = interceullar CO2 concentration ready for assimilation (ppm)
        '''
    st.markdown(md)


st.subheader('Gas exchange can be measured by a Licor')
st.image('Project/Supp/Licor.PNG', caption = 'Licor 6800 measuring plant leaf in the field')

md = ''' * A = CO2 assimilation rate (µmol CO2 m⁻² s⁻¹)  
         * E = Transpiration of H2O (mol H2O m⁻² s⁻¹)  
         * gsw = stomatal conductance of H2O (mol H2O m⁻² s⁻¹)  
         * Ci = interceullar CO2 concentration ready for assimilation (ppm)
'''
st.markdown(md)

# Note that when hosted on community cloud the root directory defaults to the top level of github dir
df = pd.read_csv('Project/Data/PlotFieldData.csv')

df_b73 = df.loc[df['GENOTYPE'] == 'B73',['NTREATMENT', 'A', 'E', 'gsw', 'Ci']]
df_forplot = df.loc[:,['NTREATMENT', 'A', 'E', 'gsw', 'Ci']]
f1 = sns.pairplot(df_forplot, hue = 'NTREATMENT')
st.pyplot(fig = f1)

# 
xp = hip.Experiment.from_dataframe(df_forplot)
st.components.v1.html(xp.to_html(), height=1500)