import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics - Top 30",
    layout="wide"
)
### Top 30 ###
top_30_df = (
    read_from_gsheets("Countries")
    .assign(**{
        "Distinct brands": lambda df: df["Distinct brands"].astype(int),
        "Total POI": lambda df: df["Total POI"].str.replace(",", "").astype(int),
        "Branded POI": lambda df: df["Branded POI"].str.replace(",", "").astype(int),
        "% Branded": lambda df: (df["Branded POI"] / df["Total POI"]) * 100
    })
    .query('iso_country_code != "US"')
    .rename(columns={"iso_country_code": "Country Code", "country": "Country"})
    [["Country Code", "Country", "Total POI", "Distinct brands", "% Branded"]]
    .head(30)
)

top_30_df_styled = (
    top_30_df.style
    .apply(lambda x: ['background-color: #D7E8ED' if i%2==0 else '' for i in range(len(x))], axis=0)
    .format({
        "Total POI": "{:,.0f}",
        "Distinct brands": "{:,.0f}",
        "Branded POI": "{:,.0f}",
        "% Branded": "{:.1f}%"
    })
)

st.write("POI and Brand Counts - Top 30 Countries outside the US")
st.dataframe(top_30_df_styled, use_container_width=True, hide_index=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
