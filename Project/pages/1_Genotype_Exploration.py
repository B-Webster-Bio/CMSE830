import streamlit as st
import hiplot as hip
import pandas as pd


# Note that when hosted on community cloud the root directory defaults to the top level of github dir
# I think there should be a way for pages to share tables?
df = pd.read_csv('Project/Data/PlotFieldData.csv')
df_forplot = df.loc[:,['NTREATMENT', 'GENOTYPE', 'SUBPOPULATION', 'A', 'E', 'gsw', 'Ci', 'KERNELDRYWT_PERPLANT']]

st.subheader('Individual genotype exploration')
st.markdown('''Understanding general trends is nice but often as a plant breeder you are asked to make selections about individual genotypes. 
            A HiPlot will allow exploration on the genotypic level of the relationship between subpopulation, treatment, yield, and gas exchange''')

# Interactive HiPlot
st.subheader('Interactive HiPlot')
xp = hip.Experiment.from_dataframe(df_forplot)
st.components.v1.html(xp.to_html(), height=1500)