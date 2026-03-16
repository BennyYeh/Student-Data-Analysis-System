import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

rcParams['font.family'] = 'Microsoft JhengHei'
rcParams['axes.unicode_minus'] = False


def show_dashboard(root, frame, df, status_var):

    from src.gui.menu_page import show_menu

    # 清空畫面
    for w in frame.winfo_children():
        w.destroy()

    # ===== 置中容器 =====
    center_frame = ttk.Frame(frame)
    center_frame.pack(expand=True)

    ttk.Label(center_frame, text="資料分析", font=("Arial",22)).pack(pady=20)

    # ===== 男女平均 =====

    gender_frame = ttk.LabelFrame(center_frame, text="男女平均")
    gender_frame.pack(pady=10)

    row = ttk.Frame(gender_frame)
    row.pack(pady=10)

    gender_bar = ttk.BooleanVar()
    gender_line = ttk.BooleanVar()
    gender_pie = ttk.BooleanVar()

    ttk.Checkbutton(row, text="長條圖", variable=gender_bar).pack(side="left", padx=15)
    ttk.Checkbutton(row, text="折線圖", variable=gender_line).pack(side="left", padx=15)
    ttk.Checkbutton(row, text="圓餅圖", variable=gender_pie).pack(side="left", padx=15)

    # ===== 各科系平均 =====

    dept_frame = ttk.LabelFrame(center_frame, text="各科系平均")
    dept_frame.pack(pady=10)

    row2 = ttk.Frame(dept_frame)
    row2.pack(pady=10)

    dept_bar = ttk.BooleanVar()
    dept_line = ttk.BooleanVar()
    dept_pie = ttk.BooleanVar()

    ttk.Checkbutton(row2, text="長條圖", variable=dept_bar).pack(side="left", padx=15)
    ttk.Checkbutton(row2, text="折線圖", variable=dept_line).pack(side="left", padx=15)
    ttk.Checkbutton(row2, text="圓餅圖", variable=dept_pie).pack(side="left", padx=15)

    # ===== 成績分布 =====

    score_frame = ttk.LabelFrame(center_frame, text="成績分布")
    score_frame.pack(pady=10)

    row3 = ttk.Frame(score_frame)
    row3.pack(pady=10)

    score_hist = ttk.BooleanVar()
    score_box = ttk.BooleanVar()
    score_kde = ttk.BooleanVar()

    ttk.Checkbutton(row3, text="直方圖", variable=score_hist).pack(side="left", padx=15)
    ttk.Checkbutton(row3, text="箱型圖", variable=score_box).pack(side="left", padx=15)
    ttk.Checkbutton(row3, text="密度圖", variable=score_kde).pack(side="left", padx=15)

    # ===== 生成圖表 =====

    def generate_chart():

        plots = []

        if gender_bar.get():
            plots.append(("男女平均", df.groupby("gender")["score"].mean(), "bar"))

        if gender_line.get():
            plots.append(("男女平均", df.groupby("gender")["score"].mean(), "line"))

        if gender_pie.get():
            plots.append(("男女平均", df.groupby("gender")["score"].mean(), "pie"))

        if dept_bar.get():
            plots.append(("各科系平均", df.groupby("department")["score"].mean(), "bar"))

        if dept_line.get():
            plots.append(("各科系平均", df.groupby("department")["score"].mean(), "line"))

        if dept_pie.get():
            plots.append(("各科系平均", df.groupby("department")["score"].mean(), "pie"))

        if score_hist.get():
            plots.append(("成績分布", df["score"], "hist"))

        if score_box.get():
            plots.append(("成績分布", df["score"], "box"))

        if score_kde.get():
            plots.append(("成績分布", df["score"], "kde"))

        if not plots:
            return

        cols = 2
        rows = math.ceil(len(plots)/cols)

        fig, axes = plt.subplots(rows, cols, figsize=(10, rows*4))

        if len(plots) == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        for i, (name, data, chart) in enumerate(plots):

            ax = axes[i]

            if chart == "bar":
                data.plot(kind="bar", ax=ax)

            elif chart == "line":
                data.plot(kind="line", marker="o", ax=ax)

            elif chart == "pie":
                data.plot(kind="pie", autopct="%1.1f%%", ax=ax)

            elif chart == "hist":
                ax.hist(data, bins=20)

            elif chart == "box":
                ax.boxplot(data)

            elif chart == "kde":
                data.plot(kind="kde", ax=ax)

            ax.set_title(name)

        plt.tight_layout()
        plt.show()

        status_var.set("狀態: 分析圖表完成")

    ttk.Button(center_frame, text="生成圖表", command=generate_chart).pack(pady=15)

    ttk.Button(
        center_frame,
        text="返回",
        command=lambda: show_menu(root, frame, df, status_var)
    ).pack(pady=10)