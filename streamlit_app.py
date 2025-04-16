import pandas as pd
import streamlit as st
from datetime import timedelta

# ---- 設定網頁標題與簡介 ---- #
st.set_page_config(page_title="內容成效儀表板", layout="wide")
st.title("📊 文章閱讀成效分析 Dashboard")
st.markdown("這是一份根據文章閱讀率與閱讀時間所製作的成效報表工具。\
數據來源：每日匯入的閱讀數據檔案（CSV）")

# ---- 讀取 CSV 檔案 ---- #
@st.cache_data
def load_data():
    df = pd.read_csv("infinite-article-data.csv", sep="\t", encoding="utf-16")
    df["閱讀秒數"] = pd.to_timedelta(df["總閱讀時間"]).dt.total_seconds()
    df["內容分數"] = df["平均閱讀率"] * (df["閱讀秒數"]**0.5)
    return df

df = load_data()

# ---- 側邊欄搜尋與篩選 ---- #
st.sidebar.header("🔎 篩選條件")
keyword = st.sidebar.text_input("關鍵字搜尋（標題）")
min_readrate = st.sidebar.slider("最低閱讀率 (%)", 0, 100, 30)

# ---- 篩選處理 ---- #
filtered_df = df[df["平均閱讀率"] >= min_readrate]
if keyword:
    filtered_df = filtered_df[filtered_df["標題"].str.contains(keyword, case=False)]

# ---- 排行榜表格 ---- #
st.subheader("🔥 熱門文章排行榜（依內容分數排序）")
top_n = st.slider("顯示前 N 篇文章", 5, 50, 20)
display_df = filtered_df.sort_values("內容分數", ascending=False).head(top_n)

display_df_show = display_df[["標題", "平均閱讀率", "總閱讀時間", "url"]].copy()
display_df_show.columns = ["標題", "平均閱讀率 (%)", "總閱讀時間", "原文連結"]

def make_clickable(link):
    return f'<a href="{link}" target="_blank">點我查看</a>'

display_df_show["原文連結"] = display_df_show["原文連結"].apply(make_clickable)

st.write(display_df_show.to_html(escape=False, index=False), unsafe_allow_html=True)

# ---- 圖表區塊 ---- #
st.subheader("📈 內容分數分布圖")
st.bar_chart(display_df.set_index("標題")["內容分數"])

st.caption("本工具由 AI 自動整理內容閱讀效能指標製作。")
