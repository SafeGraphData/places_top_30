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
# Keep-alive comment: 2025-07-25 07:23:02.437419
# Keep-alive comment: 2025-07-25 18:23:07.685657
# Keep-alive comment: 2025-07-26 05:23:00.522146
# Keep-alive comment: 2025-07-26 16:23:05.604184
# Keep-alive comment: 2025-07-27 03:23:01.007801
# Keep-alive comment: 2025-07-27 14:22:51.051534
# Keep-alive comment: 2025-07-28 01:23:13.173790
# Keep-alive comment: 2025-07-28 12:23:08.325118
# Keep-alive comment: 2025-07-28 23:23:12.235947
# Keep-alive comment: 2025-07-29 10:22:41.666556
# Keep-alive comment: 2025-07-29 21:23:11.981365
# Keep-alive comment: 2025-07-30 08:23:08.248003
# Keep-alive comment: 2025-07-30 19:23:17.295342
# Keep-alive comment: 2025-07-31 06:23:21.259283
# Keep-alive comment: 2025-07-31 17:23:07.151581
# Keep-alive comment: 2025-08-01 04:23:04.891718
# Keep-alive comment: 2025-08-01 15:23:16.987803
# Keep-alive comment: 2025-08-02 02:23:00.197497
# Keep-alive comment: 2025-08-02 13:23:11.026062
# Keep-alive comment: 2025-08-03 00:23:06.314578
# Keep-alive comment: 2025-08-03 11:23:11.633824
# Keep-alive comment: 2025-08-03 22:23:06.499299
# Keep-alive comment: 2025-08-04 09:23:04.062054
# Keep-alive comment: 2025-08-04 20:23:08.949541
# Keep-alive comment: 2025-08-05 07:23:11.868783
# Keep-alive comment: 2025-08-05 18:23:12.764372
# Keep-alive comment: 2025-08-06 05:23:06.094236
# Keep-alive comment: 2025-08-06 16:24:57.626080
# Keep-alive comment: 2025-08-07 03:23:10.341688
# Keep-alive comment: 2025-08-07 14:23:13.124392
# Keep-alive comment: 2025-08-08 01:23:01.327756
# Keep-alive comment: 2025-08-08 12:23:12.849829
# Keep-alive comment: 2025-08-08 23:23:13.111457
# Keep-alive comment: 2025-08-09 10:23:05.879573
# Keep-alive comment: 2025-08-09 21:23:28.291732
# Keep-alive comment: 2025-08-10 08:23:12.254005
# Keep-alive comment: 2025-08-10 19:23:11.909473
# Keep-alive comment: 2025-08-11 06:23:06.781850
# Keep-alive comment: 2025-08-11 17:23:12.983420
# Keep-alive comment: 2025-08-12 04:23:13.010770
# Keep-alive comment: 2025-08-12 15:23:04.925980
# Keep-alive comment: 2025-08-13 02:23:12.384739
# Keep-alive comment: 2025-08-13 13:23:10.249664
# Keep-alive comment: 2025-08-14 00:23:05.826269
# Keep-alive comment: 2025-08-14 11:23:13.980294
# Keep-alive comment: 2025-08-14 22:23:06.962396
# Keep-alive comment: 2025-08-15 09:23:06.732793
# Keep-alive comment: 2025-08-15 20:22:56.291440
# Keep-alive comment: 2025-08-16 07:23:20.592035
# Keep-alive comment: 2025-08-16 18:23:07.524843
# Keep-alive comment: 2025-08-17 05:23:10.059461
# Keep-alive comment: 2025-08-17 16:23:05.547986
# Keep-alive comment: 2025-08-18 03:23:07.400713
# Keep-alive comment: 2025-08-18 14:23:09.194740
# Keep-alive comment: 2025-08-19 01:23:06.990758
# Keep-alive comment: 2025-08-19 12:23:13.522894
# Keep-alive comment: 2025-08-19 23:23:34.359514
# Keep-alive comment: 2025-08-20 10:23:09.796261
# Keep-alive comment: 2025-08-20 21:23:12.391004
# Keep-alive comment: 2025-08-21 08:23:08.966444
# Keep-alive comment: 2025-08-21 19:23:14.052474
# Keep-alive comment: 2025-08-22 06:23:12.451632
# Keep-alive comment: 2025-08-22 17:23:07.598065
# Keep-alive comment: 2025-08-23 04:23:16.094068
# Keep-alive comment: 2025-08-23 15:23:05.662434
# Keep-alive comment: 2025-08-24 02:23:05.323671
# Keep-alive comment: 2025-08-24 13:23:07.067098
# Keep-alive comment: 2025-08-25 00:23:12.914888
# Keep-alive comment: 2025-08-25 11:23:12.750745
# Keep-alive comment: 2025-08-25 22:23:07.247711
# Keep-alive comment: 2025-08-26 09:23:09.184623
# Keep-alive comment: 2025-08-26 20:23:12.982028
# Keep-alive comment: 2025-08-27 07:23:17.499982
# Keep-alive comment: 2025-08-27 18:22:47.415917
# Keep-alive comment: 2025-08-28 05:23:17.855160
# Keep-alive comment: 2025-08-28 16:23:07.735066
# Keep-alive comment: 2025-08-29 03:22:51.168544
# Keep-alive comment: 2025-08-29 14:22:58.724964
# Keep-alive comment: 2025-08-30 01:22:56.126222
# Keep-alive comment: 2025-08-30 12:22:52.043573
# Keep-alive comment: 2025-08-30 23:22:55.416448
# Keep-alive comment: 2025-08-31 10:22:51.514576
# Keep-alive comment: 2025-08-31 21:23:02.867326
# Keep-alive comment: 2025-09-01 08:23:06.991404
# Keep-alive comment: 2025-09-01 19:23:03.100040
# Keep-alive comment: 2025-09-02 06:22:52.412708
# Keep-alive comment: 2025-09-02 17:23:03.990331
# Keep-alive comment: 2025-09-03 04:22:55.417765
# Keep-alive comment: 2025-09-03 15:22:59.066773
# Keep-alive comment: 2025-09-04 02:23:00.368833
# Keep-alive comment: 2025-09-04 13:23:11.781439
# Keep-alive comment: 2025-09-05 00:22:51.902835
# Keep-alive comment: 2025-09-05 11:22:48.067518
# Keep-alive comment: 2025-09-05 22:22:57.154316
# Keep-alive comment: 2025-09-06 09:22:52.491421
# Keep-alive comment: 2025-09-06 20:22:51.962300
# Keep-alive comment: 2025-09-07 07:22:57.101876
# Keep-alive comment: 2025-09-07 18:22:57.065628
# Keep-alive comment: 2025-09-08 05:22:53.111942
# Keep-alive comment: 2025-09-08 16:22:59.940876
# Keep-alive comment: 2025-09-09 03:23:24.420061
# Keep-alive comment: 2025-09-09 14:22:59.898280
# Keep-alive comment: 2025-09-10 01:22:50.993367
# Keep-alive comment: 2025-09-10 12:23:04.205777
# Keep-alive comment: 2025-09-10 23:22:52.411669
# Keep-alive comment: 2025-09-11 10:22:55.262732
# Keep-alive comment: 2025-09-11 21:22:52.253758
# Keep-alive comment: 2025-09-12 08:23:07.791428
# Keep-alive comment: 2025-09-12 19:22:58.060869
# Keep-alive comment: 2025-09-13 06:22:45.259618
# Keep-alive comment: 2025-09-13 17:22:51.835454
# Keep-alive comment: 2025-09-14 04:22:41.897402
# Keep-alive comment: 2025-09-14 15:22:53.448193
# Keep-alive comment: 2025-09-15 02:22:51.114184
# Keep-alive comment: 2025-09-15 13:22:54.614488
# Keep-alive comment: 2025-09-16 00:22:52.216347
# Keep-alive comment: 2025-09-16 11:22:57.960199
# Keep-alive comment: 2025-09-16 22:22:51.568217
# Keep-alive comment: 2025-09-17 09:22:54.799662
# Keep-alive comment: 2025-09-17 20:23:04.002545
# Keep-alive comment: 2025-09-18 07:22:59.529057
# Keep-alive comment: 2025-09-18 18:22:59.233306
# Keep-alive comment: 2025-09-19 05:22:53.665557
# Keep-alive comment: 2025-09-19 16:23:28.549842
# Keep-alive comment: 2025-09-20 03:22:56.615729
# Keep-alive comment: 2025-09-20 14:22:58.415451
# Keep-alive comment: 2025-09-21 01:22:58.021028
# Keep-alive comment: 2025-09-21 12:22:58.118642
# Keep-alive comment: 2025-09-21 23:22:53.158006
# Keep-alive comment: 2025-09-22 10:22:56.722759
# Keep-alive comment: 2025-09-22 21:22:52.546904
# Keep-alive comment: 2025-09-23 08:22:55.498635
# Keep-alive comment: 2025-09-23 19:23:01.131622
# Keep-alive comment: 2025-09-24 06:22:53.518120
# Keep-alive comment: 2025-09-24 17:22:59.932359
# Keep-alive comment: 2025-09-25 15:23:04.393542
# Keep-alive comment: 2025-09-26 02:22:58.890807
# Keep-alive comment: 2025-09-26 13:23:03.295337
# Keep-alive comment: 2025-09-26 19:31:30.694650
# Keep-alive comment: 2025-09-27 05:31:34.782176
# Keep-alive comment: 2025-09-27 15:31:29.980973
# Keep-alive comment: 2025-09-28 01:31:34.183186
# Keep-alive comment: 2025-09-28 11:31:35.354693
# Keep-alive comment: 2025-09-28 21:31:35.216132
# Keep-alive comment: 2025-09-29 07:31:41.659038
# Keep-alive comment: 2025-09-29 17:31:50.801613
# Keep-alive comment: 2025-09-30 03:31:29.256828
# Keep-alive comment: 2025-09-30 13:31:37.028869
# Keep-alive comment: 2025-09-30 23:31:54.146300
# Keep-alive comment: 2025-10-01 09:32:02.889932
# Keep-alive comment: 2025-10-01 19:31:35.641510
# Keep-alive comment: 2025-10-02 05:32:03.178807
# Keep-alive comment: 2025-10-02 15:32:01.623680
# Keep-alive comment: 2025-10-03 01:31:34.071610
# Keep-alive comment: 2025-10-03 11:31:55.473738
# Keep-alive comment: 2025-10-03 21:31:30.114568
# Keep-alive comment: 2025-10-04 07:31:29.079298
# Keep-alive comment: 2025-10-04 17:31:39.853541
# Keep-alive comment: 2025-10-05 03:31:33.594435
# Keep-alive comment: 2025-10-05 13:31:38.817160
# Keep-alive comment: 2025-10-05 23:31:59.475741
# Keep-alive comment: 2025-10-06 09:32:05.616742
# Keep-alive comment: 2025-10-06 19:31:39.694752
# Keep-alive comment: 2025-10-07 05:31:36.875053
# Keep-alive comment: 2025-10-07 15:31:58.881945
# Keep-alive comment: 2025-10-08 01:31:34.973844
# Keep-alive comment: 2025-10-08 11:31:36.776385
# Keep-alive comment: 2025-10-08 21:31:35.872677
# Keep-alive comment: 2025-10-09 07:31:39.137191
# Keep-alive comment: 2025-10-09 17:31:39.251506
# Keep-alive comment: 2025-10-10 03:31:25.194109
# Keep-alive comment: 2025-10-10 13:31:18.008218
# Keep-alive comment: 2025-10-10 23:31:29.672240
# Keep-alive comment: 2025-10-11 09:31:35.179479
# Keep-alive comment: 2025-10-11 19:31:29.154847
# Keep-alive comment: 2025-10-12 05:31:32.350269
# Keep-alive comment: 2025-10-12 15:31:38.159880
# Keep-alive comment: 2025-10-13 01:31:31.529625
# Keep-alive comment: 2025-10-13 11:32:03.440364
# Keep-alive comment: 2025-10-13 21:31:26.082398
# Keep-alive comment: 2025-10-14 07:31:30.255754
# Keep-alive comment: 2025-10-14 17:31:33.335711
# Keep-alive comment: 2025-10-15 03:31:30.176267
# Keep-alive comment: 2025-10-15 13:31:33.687313
# Keep-alive comment: 2025-10-15 23:31:36.200702
# Keep-alive comment: 2025-10-16 09:31:32.927435
# Keep-alive comment: 2025-10-16 19:31:39.283607
# Keep-alive comment: 2025-10-17 05:31:36.762831
# Keep-alive comment: 2025-10-17 15:31:53.928309
# Keep-alive comment: 2025-10-18 01:31:31.104524
# Keep-alive comment: 2025-10-18 11:31:55.575551
# Keep-alive comment: 2025-10-18 21:32:05.129816
# Keep-alive comment: 2025-10-19 07:31:24.986824
# Keep-alive comment: 2025-10-19 17:32:00.133865
# Keep-alive comment: 2025-10-20 03:31:58.779780
# Keep-alive comment: 2025-10-20 13:31:38.441677
# Keep-alive comment: 2025-10-20 23:31:31.209059
# Keep-alive comment: 2025-10-21 09:31:37.656657
# Keep-alive comment: 2025-10-21 19:33:39.204637
# Keep-alive comment: 2025-10-22 05:31:32.281731
# Keep-alive comment: 2025-10-22 15:32:38.942504
# Keep-alive comment: 2025-10-23 01:31:32.473219
# Keep-alive comment: 2025-10-23 11:31:44.258142
# Keep-alive comment: 2025-10-23 21:31:33.719717
# Keep-alive comment: 2025-10-24 07:32:52.752325
# Keep-alive comment: 2025-10-24 17:31:42.594209
# Keep-alive comment: 2025-10-25 03:31:35.665103
# Keep-alive comment: 2025-10-25 13:31:59.289605
# Keep-alive comment: 2025-10-25 23:31:31.845125
# Keep-alive comment: 2025-10-26 09:31:24.801410
# Keep-alive comment: 2025-10-26 19:32:01.842949
# Keep-alive comment: 2025-10-27 05:31:41.832397
# Keep-alive comment: 2025-10-27 15:31:59.253855
# Keep-alive comment: 2025-10-28 01:31:35.067331
# Keep-alive comment: 2025-10-28 11:31:37.751681
# Keep-alive comment: 2025-10-28 21:31:25.758345
# Keep-alive comment: 2025-10-29 07:31:32.437380
# Keep-alive comment: 2025-10-29 17:31:42.080961
# Keep-alive comment: 2025-10-30 03:31:32.022356
# Keep-alive comment: 2025-10-30 13:32:04.559163
# Keep-alive comment: 2025-10-30 23:31:36.984740
# Keep-alive comment: 2025-10-31 09:32:51.880636
# Keep-alive comment: 2025-10-31 19:31:26.853284
# Keep-alive comment: 2025-11-01 05:31:35.508974
# Keep-alive comment: 2025-11-01 15:31:23.948108
# Keep-alive comment: 2025-11-02 01:31:36.679308
# Keep-alive comment: 2025-11-02 11:31:37.287053
# Keep-alive comment: 2025-11-02 21:31:51.258776
# Keep-alive comment: 2025-11-03 07:31:33.121259
# Keep-alive comment: 2025-11-03 17:31:38.936763
# Keep-alive comment: 2025-11-04 03:31:36.715739
# Keep-alive comment: 2025-11-04 13:32:05.043740
# Keep-alive comment: 2025-11-04 23:31:56.667539
# Keep-alive comment: 2025-11-05 09:32:08.473340
# Keep-alive comment: 2025-11-05 19:31:37.085858
# Keep-alive comment: 2025-11-06 05:32:06.539435
# Keep-alive comment: 2025-11-06 15:31:51.069201
# Keep-alive comment: 2025-11-07 01:31:34.547980
# Keep-alive comment: 2025-11-07 11:31:40.932444
# Keep-alive comment: 2025-11-07 21:31:38.795065
# Keep-alive comment: 2025-11-08 07:31:25.438322
# Keep-alive comment: 2025-11-08 17:31:40.927102
# Keep-alive comment: 2025-11-09 03:32:15.364705
# Keep-alive comment: 2025-11-09 13:31:36.906647
# Keep-alive comment: 2025-11-09 23:31:26.589037
# Keep-alive comment: 2025-11-10 09:31:34.121382
# Keep-alive comment: 2025-11-10 19:31:49.273190
# Keep-alive comment: 2025-11-11 05:31:33.422758
# Keep-alive comment: 2025-11-11 15:31:32.670439
# Keep-alive comment: 2025-11-12 01:31:38.810200
# Keep-alive comment: 2025-11-12 11:31:42.281283
# Keep-alive comment: 2025-11-12 21:31:58.958023
# Keep-alive comment: 2025-11-13 07:31:22.567265
# Keep-alive comment: 2025-11-13 17:31:33.594966
# Keep-alive comment: 2025-11-14 03:31:39.798076
# Keep-alive comment: 2025-11-14 13:32:00.869495
# Keep-alive comment: 2025-11-14 23:31:32.167398
# Keep-alive comment: 2025-11-15 09:31:35.376336
# Keep-alive comment: 2025-11-15 19:31:40.801919
# Keep-alive comment: 2025-11-16 05:31:32.705856
# Keep-alive comment: 2025-11-16 15:31:36.854636
# Keep-alive comment: 2025-11-17 01:31:27.128583
# Keep-alive comment: 2025-11-17 11:32:00.597720
# Keep-alive comment: 2025-11-17 21:31:30.143443
# Keep-alive comment: 2025-11-18 07:31:32.381321
# Keep-alive comment: 2025-11-18 17:31:32.946594
# Keep-alive comment: 2025-11-19 03:31:35.676032
# Keep-alive comment: 2025-11-19 13:31:28.811277
# Keep-alive comment: 2025-11-19 23:31:29.872575
# Keep-alive comment: 2025-11-20 09:31:38.008759
# Keep-alive comment: 2025-11-20 19:33:27.714798
# Keep-alive comment: 2025-11-21 05:31:32.642291
# Keep-alive comment: 2025-11-21 15:31:38.855955
# Keep-alive comment: 2025-11-22 01:31:41.001403
# Keep-alive comment: 2025-11-22 11:31:25.911860
# Keep-alive comment: 2025-11-22 21:31:37.249132