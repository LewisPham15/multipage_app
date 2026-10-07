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
chart_area = st.empty()

values = [float(np.random.randn())]

for i in range(1, 101):
    steps = values[-1] + np.random.randn(5).cumsum()
    for step in steps:
        values.append(float(step))

    frame = pd.DataFrame({"value": values})
    chart_area.line_chart(frame)

    status_text.text(f"{i}% complete")
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()

st.button("Re-run")