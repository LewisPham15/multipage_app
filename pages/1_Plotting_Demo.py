import time

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

last_rows = pd.DataFrame(np.random.randn(1, 1), columns=["value"])
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_values = last_rows["value"].iloc[-1] + np.random.randn(5).cumsum()
    new_rows = pd.DataFrame(new_values, columns=["value"])
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

st.button("Re-run")