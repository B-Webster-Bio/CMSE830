import streamlit as st
import pandas as pd
import numpy as np
import hiplot as hip
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

st.title('Gas Exchange in Corn Inbreds :corn: :dash:')
md = '''"Breathing" or gas exchange of Carbon Dioxide (CO2) and water (H2O) through leaf stomata is an important process in plant biology that is 
associated with how much carbon and water a plant is processing. In theory these traits are related to grain production but harnessing this information for plant breeding is tricky. 
Nitrogen fertilizer is an important input that is well known to influence the total amount of grain production. 
Gas exchange and grain yield were collected from a panel of 105 corn inbreds in high and low N treatments. 
Understanding how gas exchange traits and yield change between N treatments over a diverse population of maize genotypes will enable better breeding for effecient corn lines.
'''
st.markdown(md)

md = '* Data cleaning and exploration in "Notebooks/Task0_DataIngestion.ipynb"'
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
    st.header("Yield")
    st.markdown("* KernelDryWt_PerPlant = Avg grams of grain per plant")

st.subheader('Gas exchange can be measured by a Licor')
st.image('Project/Supp/Licor.PNG', caption = 'Licor 6800 measuring plant leaf in the field')

# Note that when hosted on community cloud the root directory defaults to the top level of github dir
df = pd.read_csv('Project/Data/PlotFieldData.csv')

# visualize subpopulations
st.subheader('Represented maize subpopulations')
df_subpop = df.drop_duplicates(subset='GENOTYPE')
f1 = sns.displot(data=df_subpop, x = 'SUBPOPULATION', hue = 'SUBPOPULATION', kind='hist')
f1.set_xticklabels(rotation = 80)
st.pyplot(fig = f1)
st.caption('StiffStalk (SS), Non-StiffStalk (NSS), and Iodent (IDT) subpopulations are the cornerstone of North American corn germplams development')
st.markdown("____")

# these dfs to use later
df_forplot = df.loc[:,['NTREATMENT', 'GENOTYPE', 'SUBPOPULATION', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]

st.subheader('Pairplot')
st.pyplot(sns.pairplot(df_forplot, hue = 'NTREATMENT'))

st.subheader('Correlations')

# Create three tabs
tab1, tab2, tab3 = st.tabs(["All Data", "High N Treatment", "Low N Treatment"])

# Function to create and display heatmap for tabs
def plot_heatmap(data, title):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data.corr(), ax=ax, annot=True, vmin=-1, vmax=1, cmap='coolwarm')
    plt.title(title)
    st.pyplot(fig)

# Content for Tab 1: All Data
with tab1:
    st.header("Correlation Heatmap - All Data")
    df_cor = df_forplot.loc[:, ['NTREATMENT', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]
    label_map = {'H': 1, 'L': 0}
    df_cor['NTREATMENT'] = df_cor['NTREATMENT'].map(label_map)
    plot_heatmap(df_cor, "Correlation Heatmap - All Data")

# Content for Tab 2: High N Treatment
with tab2:
    st.header("Correlation Heatmap - High N Treatment")
    df_cor_h = df_forplot.loc[df_forplot['NTREATMENT'] == 'H', ['NTREATMENT', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]
    df_cor_h['NTREATMENT'] = df_cor_h['NTREATMENT'].map(label_map)
    plot_heatmap(df_cor_h, "Correlation Heatmap - High N Treatment")

# Content for Tab 3: Low N Treatment
with tab3:
    st.header("Correlation Heatmap - Low N Treatment")
    df_cor_l = df_forplot.loc[df_forplot['NTREATMENT'] == 'L', ['NTREATMENT', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]
    df_cor_l['NTREATMENT'] = df_cor_l['NTREATMENT'].map(label_map)
    plot_heatmap(df_cor_l, "Correlation Heatmap - Low N Treatment")

st.markdown("____")
st.subheader('Preliminary Results:')
st.markdown('''There appears to be a mildy strong association between yield and Nitrogen Treatment, this is well known. 
    There also appears to be a similar strength relationship between Yield and gas exchange parameters which is less well known. 
    The relationship remains mostly the same in High and Low N treatments respectively. CO2 assimilation rate (A) has the largest change 
    between H (0.15) and L (0.26) while the water related traits, gsw and E, remain stable. These results warrant further investigation. 
    In the future I will incorporate remote sensing data to investigate how canopy level refelctance, gas exchange, and yield are intertwined.''')

