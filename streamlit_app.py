import pandas as pd
import streamlit as st
from datetime import timedelta

st.set_page_config(page_title="內容成效儀表板", layout="wide")
st.title("📊 文章閱讀成效分析 Dashboard")
st.markdown("這是一份根據文章閱讀率與閱讀時間所製作的成效報表工具。")

@st.cache_data
def load_data():
    df = pd.read_csv("infinite-article-data-with-category.csv", sep="\t", encoding="utf-16")
    df["閱讀秒數"] = pd.to_timedelta(df["總閱讀時間"]).dt.total_seconds()
    df["內容分數"] = df["平均閱讀率"] * (df["閱讀秒數"]**0.5)
    return df

df = load_data()

# 側邊篩選器
st.sidebar.header("🔎 篩選條件")
keyword = st.sidebar.text_input("關鍵字搜尋（標題）")
min_readrate = st.sidebar.slider("最低閱讀率 (%)", 0, 100, 30)
category_options = ["全部"] + sorted(df["分類"].unique().tolist())
selected_category = st.sidebar.selectbox("文章分類", category_options)

# 條件篩選
filtered_df = df[df["平均閱讀率"] >= min_readrate]
if selected_category != "全部":
    filtered_df = filtered_df[filtered_df["分類"] == selected_category]
if keyword:
    filtered_df = filtered_df[filtered_df["標題"].str.contains(keyword, case=False)]

# 排行榜
st.subheader("🔥 熱門文章排行榜")
top_n = st.slider("顯示前 N 篇文章", 5, 50, 20)
display_df = filtered_df.sort_values("內容分數", ascending=False).head(top_n)

display_df_show = display_df[["標題", "分類", "平均閱讀率", "總閱讀時間", "url"]].copy()
display_df_show.columns = ["標題", "分類", "平均閱讀率 (%)", "總閱讀時間", "原文連結"]

def make_clickable(link):
    return f'<a href="{link}" target="_blank">點我查看</a>'

display_df_show["原文連結"] = display_df_show["原文連結"].apply(make_clickable)
st.write(display_df_show.to_html(escape=False, index=False), unsafe_allow_html=True)

# 分數長條圖
st.subheader("📈 內容分數分布圖")
st.bar_chart(display_df.set_index("標題")["內容分數"])

# 分類分析
st.subheader("📚 分類表現分析")
category_summary = df.groupby("分類")[["內容分數", "平均閱讀率"]].mean().sort_values("內容分數", ascending=False)
st.bar_chart(category_summary["內容分數"])

st.caption("本工具由 AI 自動分類 + 閱讀資料分析產製")
