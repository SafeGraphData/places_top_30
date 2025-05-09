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

st.markdown("#### POI and Brand Counts - Top 30 Countries outside the US")
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

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-04-25 16:08:44.007548
# Keep-alive comment: 2025-04-25 16:18:41.948398
# Keep-alive comment: 2025-04-26 00:24:16.716828
# Keep-alive comment: 2025-04-26 11:24:11.129614
# Keep-alive comment: 2025-04-26 22:23:10.508322
# Keep-alive comment: 2025-04-27 09:23:41.574542
# Keep-alive comment: 2025-04-27 20:23:36.389744
# Keep-alive comment: 2025-04-28 07:24:07.306776
# Keep-alive comment: 2025-04-28 18:24:27.006382
# Keep-alive comment: 2025-04-29 05:23:56.106057
# Keep-alive comment: 2025-04-29 16:24:41.273984
# Keep-alive comment: 2025-04-30 03:23:31.039156
# Keep-alive comment: 2025-04-30 14:23:59.763314
# Keep-alive comment: 2025-05-01 01:24:10.654832
# Keep-alive comment: 2025-05-01 12:23:42.127931
# Keep-alive comment: 2025-05-01 23:23:15.113950
# Keep-alive comment: 2025-05-02 10:24:01.326897
# Keep-alive comment: 2025-05-02 21:23:12.597347
# Keep-alive comment: 2025-05-03 08:23:36.864096
# Keep-alive comment: 2025-05-03 19:23:55.088079
# Keep-alive comment: 2025-05-04 06:24:00.693821
# Keep-alive comment: 2025-05-04 17:23:09.595030
# Keep-alive comment: 2025-05-05 04:24:20.493010
# Keep-alive comment: 2025-05-05 15:23:39.859155
# Keep-alive comment: 2025-05-06 02:24:30.505710
# Keep-alive comment: 2025-05-06 13:23:32.498593
# Keep-alive comment: 2025-05-07 00:23:31.103424
# Keep-alive comment: 2025-05-07 11:23:43.819901
# Keep-alive comment: 2025-05-07 22:23:42.226216
# Keep-alive comment: 2025-05-08 09:23:44.302762
# Keep-alive comment: 2025-05-08 20:23:43.373504
# Keep-alive comment: 2025-05-09 07:23:52.859850
# Keep-alive comment: 2025-05-09 18:24:05.380122
# Keep-alive comment: 2025-05-10 05:23:48.457574
# Keep-alive comment: 2025-05-10 16:23:34.784580