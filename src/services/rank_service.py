def calculate_rank(df):

    df = df.sort_values(  #排序成績
        "score",          #指定排序的欄位
        ascending=False   #由大到小排序
    ).copy()

    df["rank"] = df["score"].rank(
        method="min",     #同分使用最小名次
        ascending=False   #由大到小排序
    ).astype(int)         #將 rank 的型別轉換為 整數

    cols = ["rank"] + [c for c in df.columns if c!="rank"]
    #list 名稱為cols 他裝了rank和其他不是rank的欄位

    return df[cols]      #回傳cols的結果