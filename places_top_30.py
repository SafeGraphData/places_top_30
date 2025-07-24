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
# Keep-alive comment: 2025-05-11 03:23:34.331376
# Keep-alive comment: 2025-05-11 14:23:25.877774
# Keep-alive comment: 2025-05-12 01:23:31.773219
# Keep-alive comment: 2025-05-12 12:24:02.328772
# Keep-alive comment: 2025-05-12 23:23:35.040530
# Keep-alive comment: 2025-05-13 10:24:36.346811
# Keep-alive comment: 2025-05-13 21:23:36.054268
# Keep-alive comment: 2025-05-14 08:24:04.080617
# Keep-alive comment: 2025-05-14 19:24:01.137046
# Keep-alive comment: 2025-05-15 06:24:02.803624
# Keep-alive comment: 2025-05-15 17:24:32.469435
# Keep-alive comment: 2025-05-16 04:23:47.636355
# Keep-alive comment: 2025-05-16 15:22:50.748964
# Keep-alive comment: 2025-05-17 02:23:08.768777
# Keep-alive comment: 2025-05-17 13:23:52.310873
# Keep-alive comment: 2025-05-18 00:23:06.956728
# Keep-alive comment: 2025-05-18 11:23:35.350672
# Keep-alive comment: 2025-05-18 22:23:32.677334
# Keep-alive comment: 2025-05-19 09:24:09.597699
# Keep-alive comment: 2025-05-19 20:23:08.275916
# Keep-alive comment: 2025-05-20 07:23:24.402363
# Keep-alive comment: 2025-05-20 18:24:36.447702
# Keep-alive comment: 2025-05-21 05:23:07.970654
# Keep-alive comment: 2025-05-21 16:23:17.324162
# Keep-alive comment: 2025-05-22 03:23:11.650429
# Keep-alive comment: 2025-05-22 14:23:15.902298
# Keep-alive comment: 2025-05-23 01:23:14.265574
# Keep-alive comment: 2025-05-23 12:23:14.229705
# Keep-alive comment: 2025-05-23 23:23:17.763855
# Keep-alive comment: 2025-05-24 10:23:15.669151
# Keep-alive comment: 2025-05-24 21:23:12.246270
# Keep-alive comment: 2025-05-25 08:23:12.852747
# Keep-alive comment: 2025-05-25 19:23:17.910484
# Keep-alive comment: 2025-05-26 06:23:03.030257
# Keep-alive comment: 2025-05-26 17:23:07.357329
# Keep-alive comment: 2025-05-27 04:23:13.157161
# Keep-alive comment: 2025-05-27 15:23:18.029961
# Keep-alive comment: 2025-05-28 02:23:27.185417
# Keep-alive comment: 2025-05-28 13:23:18.400922
# Keep-alive comment: 2025-05-29 00:23:10.947611
# Keep-alive comment: 2025-05-29 11:23:06.631321
# Keep-alive comment: 2025-05-29 22:23:20.550388
# Keep-alive comment: 2025-05-30 09:23:05.990937
# Keep-alive comment: 2025-05-30 20:23:06.688411
# Keep-alive comment: 2025-05-31 07:23:18.760623
# Keep-alive comment: 2025-05-31 18:23:13.315339
# Keep-alive comment: 2025-06-01 05:23:12.952830
# Keep-alive comment: 2025-06-01 16:23:25.470981
# Keep-alive comment: 2025-06-02 03:23:26.816290
# Keep-alive comment: 2025-06-02 14:23:18.437709
# Keep-alive comment: 2025-06-03 01:23:08.165751
# Keep-alive comment: 2025-06-03 12:23:23.152009
# Keep-alive comment: 2025-06-03 23:23:19.363217
# Keep-alive comment: 2025-06-04 10:23:18.125832
# Keep-alive comment: 2025-06-04 21:22:57.118322
# Keep-alive comment: 2025-06-05 08:23:20.427185
# Keep-alive comment: 2025-06-05 19:23:10.884242
# Keep-alive comment: 2025-06-06 06:23:08.116155
# Keep-alive comment: 2025-06-06 17:22:51.294958
# Keep-alive comment: 2025-06-07 04:22:53.256184
# Keep-alive comment: 2025-06-07 15:23:02.258312
# Keep-alive comment: 2025-06-08 02:23:07.273246
# Keep-alive comment: 2025-06-08 13:23:08.862387
# Keep-alive comment: 2025-06-09 00:22:51.374737
# Keep-alive comment: 2025-06-09 11:23:06.350941
# Keep-alive comment: 2025-06-09 22:23:15.312333
# Keep-alive comment: 2025-06-10 09:23:18.398172
# Keep-alive comment: 2025-06-10 20:23:11.107886
# Keep-alive comment: 2025-06-11 07:23:12.131079
# Keep-alive comment: 2025-06-11 18:25:01.876349
# Keep-alive comment: 2025-06-12 05:23:09.468979
# Keep-alive comment: 2025-06-12 16:23:12.823770
# Keep-alive comment: 2025-06-13 03:23:13.703889
# Keep-alive comment: 2025-06-13 14:23:03.095589
# Keep-alive comment: 2025-06-14 01:23:23.567103
# Keep-alive comment: 2025-06-14 12:23:09.555756
# Keep-alive comment: 2025-06-14 23:23:00.962665
# Keep-alive comment: 2025-06-15 10:22:47.760246
# Keep-alive comment: 2025-06-15 21:23:21.611550
# Keep-alive comment: 2025-06-16 08:23:18.922194
# Keep-alive comment: 2025-06-16 19:23:02.865120
# Keep-alive comment: 2025-06-17 06:23:39.548035
# Keep-alive comment: 2025-06-17 17:23:07.668350
# Keep-alive comment: 2025-06-18 04:23:13.485513
# Keep-alive comment: 2025-06-18 15:23:13.845561
# Keep-alive comment: 2025-06-19 02:23:11.318645
# Keep-alive comment: 2025-06-19 13:23:11.759005
# Keep-alive comment: 2025-06-20 00:23:07.731845
# Keep-alive comment: 2025-06-20 11:23:57.077343
# Keep-alive comment: 2025-06-20 22:23:16.274115
# Keep-alive comment: 2025-06-21 09:23:01.714370
# Keep-alive comment: 2025-06-21 20:23:13.900643
# Keep-alive comment: 2025-06-22 07:23:06.481489
# Keep-alive comment: 2025-06-22 18:22:57.383016
# Keep-alive comment: 2025-06-23 05:23:13.729477
# Keep-alive comment: 2025-06-23 16:23:07.591822
# Keep-alive comment: 2025-06-24 03:23:13.899289
# Keep-alive comment: 2025-06-24 14:22:53.713788
# Keep-alive comment: 2025-06-25 01:22:47.402854
# Keep-alive comment: 2025-06-25 12:23:09.802679
# Keep-alive comment: 2025-06-25 23:23:11.801035
# Keep-alive comment: 2025-06-26 10:23:19.470679
# Keep-alive comment: 2025-06-26 21:24:44.140772
# Keep-alive comment: 2025-06-27 08:23:12.575791
# Keep-alive comment: 2025-06-27 19:23:09.277536
# Keep-alive comment: 2025-06-28 06:23:15.758502
# Keep-alive comment: 2025-06-28 17:23:05.938870
# Keep-alive comment: 2025-06-29 04:22:55.592959
# Keep-alive comment: 2025-06-29 15:22:45.516795
# Keep-alive comment: 2025-06-30 02:23:07.026920
# Keep-alive comment: 2025-06-30 13:22:49.600088
# Keep-alive comment: 2025-07-01 00:24:53.352272
# Keep-alive comment: 2025-07-01 11:23:09.211865
# Keep-alive comment: 2025-07-01 22:23:12.969302
# Keep-alive comment: 2025-07-02 09:23:07.163828
# Keep-alive comment: 2025-07-02 20:24:56.352326
# Keep-alive comment: 2025-07-03 07:23:21.760154
# Keep-alive comment: 2025-07-03 18:22:47.867989
# Keep-alive comment: 2025-07-04 05:23:10.981810
# Keep-alive comment: 2025-07-04 16:23:06.021149
# Keep-alive comment: 2025-07-05 03:23:05.634104
# Keep-alive comment: 2025-07-05 14:23:09.931789
# Keep-alive comment: 2025-07-06 01:23:08.144240
# Keep-alive comment: 2025-07-06 12:23:04.399029
# Keep-alive comment: 2025-07-06 23:23:06.211382
# Keep-alive comment: 2025-07-07 10:23:07.237140
# Keep-alive comment: 2025-07-07 21:23:06.109119
# Keep-alive comment: 2025-07-08 08:23:10.497547
# Keep-alive comment: 2025-07-08 19:23:06.887703
# Keep-alive comment: 2025-07-09 06:23:17.015950
# Keep-alive comment: 2025-07-09 17:23:50.733855
# Keep-alive comment: 2025-07-10 04:23:05.698274
# Keep-alive comment: 2025-07-10 15:23:12.190611
# Keep-alive comment: 2025-07-11 02:23:04.768307
# Keep-alive comment: 2025-07-11 13:23:05.948623
# Keep-alive comment: 2025-07-12 00:22:51.802878
# Keep-alive comment: 2025-07-12 11:23:09.659697
# Keep-alive comment: 2025-07-12 22:23:05.669118
# Keep-alive comment: 2025-07-13 09:23:05.359075
# Keep-alive comment: 2025-07-13 20:22:50.257089
# Keep-alive comment: 2025-07-14 07:23:03.672384
# Keep-alive comment: 2025-07-14 18:23:26.600464
# Keep-alive comment: 2025-07-15 05:23:16.795172
# Keep-alive comment: 2025-07-15 16:23:11.364883
# Keep-alive comment: 2025-07-16 03:23:10.306415
# Keep-alive comment: 2025-07-16 14:23:12.056620
# Keep-alive comment: 2025-07-17 01:23:05.872531
# Keep-alive comment: 2025-07-17 12:23:12.866689
# Keep-alive comment: 2025-07-17 23:23:04.035530
# Keep-alive comment: 2025-07-18 10:23:26.200285
# Keep-alive comment: 2025-07-18 21:23:05.706610
# Keep-alive comment: 2025-07-19 08:23:45.754270
# Keep-alive comment: 2025-07-19 19:22:50.695428
# Keep-alive comment: 2025-07-20 06:23:14.943044
# Keep-alive comment: 2025-07-20 17:23:21.256293
# Keep-alive comment: 2025-07-21 04:23:16.021270
# Keep-alive comment: 2025-07-21 15:23:03.373240
# Keep-alive comment: 2025-07-22 02:23:25.234121
# Keep-alive comment: 2025-07-22 13:23:39.331921
# Keep-alive comment: 2025-07-23 00:23:12.320534
# Keep-alive comment: 2025-07-23 11:23:02.688362
# Keep-alive comment: 2025-07-23 22:23:05.149152
# Keep-alive comment: 2025-07-24 09:23:22.377388
# Keep-alive comment: 2025-07-24 20:23:07.408462