{\rtf1\ansi\ansicpg950\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import streamlit as st\
from datetime import timedelta\
\
# ---- \uc0\u35373 \u23450 \u32178 \u38913 \u27161 \u38988 \u33287 \u31777 \u20171  ---- #\
st.set_page_config(page_title="\uc0\u20839 \u23481 \u25104 \u25928 \u20736 \u34920 \u26495 ", layout="wide")\
st.title("\uc0\u55357 \u56522  \u25991 \u31456 \u38321 \u35712 \u25104 \u25928 \u20998 \u26512  Dashboard")\
st.markdown("\uc0\u36889 \u26159 \u19968 \u20221 \u26681 \u25818 \u25991 \u31456 \u38321 \u35712 \u29575 \u33287 \u38321 \u35712 \u26178 \u38291 \u25152 \u35069 \u20316 \u30340 \u25104 \u25928 \u22577 \u34920 \u24037 \u20855 \u12290 \\n\u25976 \u25818 \u20358 \u28304 \u65306 \u27599 \u26085 \u21295 \u20837 \u30340 \u38321 \u35712 \u25976 \u25818 \u27284 \u26696 \u65288 CSV\u65289 ")\
\
# ---- \uc0\u35712 \u21462  CSV \u27284 \u26696  ---- #\
@st.cache_data\
def load_data():\
    df = pd.read_csv("infinite-article-data.csv", sep="\\t", encoding="utf-16")\
    # \uc0\u36681 \u25563 \u26178 \u38291 \u26684 \u24335 \u28858 \u31186 \u25976 \u65288 \u26041 \u20415 \u35336 \u31639 \u65289 \
    df["\uc0\u38321 \u35712 \u31186 \u25976 "] = pd.to_timedelta(df["\u32317 \u38321 \u35712 \u26178 \u38291 "]).dt.total_seconds()\
    df["\uc0\u20839 \u23481 \u20998 \u25976 "] = df["\u24179 \u22343 \u38321 \u35712 \u29575 "] * (df["\u38321 \u35712 \u31186 \u25976 "]**0.5)\
    return df\
\
df = load_data()\
\
# ---- \uc0\u20596 \u37002 \u27396 \u25628 \u23563 \u33287 \u31721 \u36984  ---- #\
st.sidebar.header("\uc0\u55357 \u56590  \u31721 \u36984 \u26781 \u20214 ")\
keyword = st.sidebar.text_input("\uc0\u38364 \u37749 \u23383 \u25628 \u23563 \u65288 \u27161 \u38988 \u65289 ")\
min_readrate = st.sidebar.slider("\uc0\u26368 \u20302 \u38321 \u35712 \u29575  (%)", 0, 100, 30)\
\
# ---- \uc0\u31721 \u36984 \u34389 \u29702  ---- #\
filtered_df = df[df["\uc0\u24179 \u22343 \u38321 \u35712 \u29575 "] >= min_readrate]\
if keyword:\
    filtered_df = filtered_df[filtered_df["\uc0\u27161 \u38988 "].str.contains(keyword, case=False)]\
\
# ---- \uc0\u25490 \u34892 \u27036 \u34920 \u26684  ---- #\
st.subheader("\uc0\u55357 \u56613  \u29105 \u38272 \u25991 \u31456 \u25490 \u34892 \u27036 \u65288 \u20381 \u20839 \u23481 \u20998 \u25976 \u25490 \u24207 \u65289 ")\
top_n = st.slider("\uc0\u39023 \u31034 \u21069  N \u31687 \u25991 \u31456 ", 5, 50, 20)\
display_df = filtered_df.sort_values("\uc0\u20839 \u23481 \u20998 \u25976 ", ascending=False).head(top_n)\
\
display_df_show = display_df[["\uc0\u27161 \u38988 ", "\u24179 \u22343 \u38321 \u35712 \u29575 ", "\u32317 \u38321 \u35712 \u26178 \u38291 ", "url"]].copy()\
display_df_show.columns = ["\uc0\u27161 \u38988 ", "\u24179 \u22343 \u38321 \u35712 \u29575  (%)", "\u32317 \u38321 \u35712 \u26178 \u38291 ", "\u21407 \u25991 \u36899 \u32080 "]\
\
def make_clickable(link):\
    return f'<a href="\{link\}" target="_blank">\uc0\u40670 \u25105 \u26597 \u30475 </a>'\
\
display_df_show["\uc0\u21407 \u25991 \u36899 \u32080 "] = display_df_show["\u21407 \u25991 \u36899 \u32080 "].apply(make_clickable)\
\
st.write(display_df_show.to_html(escape=False, index=False), unsafe_allow_html=True)\
\
# ---- \uc0\u22294 \u34920 \u21312 \u22602  ---- #\
st.subheader("\uc0\u55357 \u56520  \u20839 \u23481 \u20998 \u25976 \u20998 \u24067 \u22294 ")\
st.bar_chart(display_df.set_index("\uc0\u27161 \u38988 ")["\u20839 \u23481 \u20998 \u25976 "])\
\
st.caption("\uc0\u26412 \u24037 \u20855 \u30001  AI \u33258 \u21205 \u25972 \u29702 \u20839 \u23481 \u38321 \u35712 \u25928 \u33021 \u25351 \u27161 \u35069 \u20316 \u12290 ")\
}