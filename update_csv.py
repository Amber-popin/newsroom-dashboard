import pandas as pd
from datetime import date

# 讀取原始資料
df = pd.read_csv("infinite-article-data.csv", sep="\t", encoding="utf-16")

# 自動加入當天日期
df["日期"] = date.today().isoformat()

# 自動分類規則
def classify_article(title):
    title = str(title)
    if any(k in title for k in ["血壓", "心臟", "膽固醇", "心血管"]):
        return "心血管健康"
    elif any(k in title for k in ["皮膚", "指甲", "護膚", "毛孔", "保養"]):
        return "美容護理"
    elif any(k in title for k in ["飲食", "食物", "糖分", "營養", "熱量"]):
        return "飲食營養"
    elif any(k in title for k in ["癌", "檢查", "症狀", "疾病", "治療"]):
        return "疾病與預防"
    elif any(k in title for k in ["腎臟", "尿", "泌尿", "排尿"]):
        return "泌尿健康"
    else:
        return "其他"

df["分類"] = df["標題"].apply(classify_article)

# 匯出處理後的檔案
df.to_csv("infinite-article-data-with-category.csv", sep="\t", encoding="utf-16", index=False)

