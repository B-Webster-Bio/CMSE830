# to run app navigate to this file in cmd prompt and then execute "streamlit run Stream2.py"
# Strange that streamlit needed to be installed twice

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns=['a', 'b', 'c'])

st.line_chart(chart_data)