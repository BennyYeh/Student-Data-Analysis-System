import ttkbootstrap as ttk

from src.gui.query_page import show_query
from src.gui.rank_page import show_rank
from src.gui.dashboard_page import show_dashboard


def show_menu(root, frame, df, status_var):

    for w in frame.winfo_children():
        w.destroy()

    ttk.Label(frame, text="學生資料系統", font=("Arial", 20)).pack(pady=20)

    ttk.Button(
        frame,
        text="成績查詢",
        command=lambda: show_query(root, frame, df, status_var)
    ).pack(pady=10)

    ttk.Button(
        frame,
        text="成績排行",
        command=lambda: show_rank(root, frame, df, status_var)
    ).pack(pady=10)

    ttk.Button(
        frame,
        text="資料分析",
        command=lambda: show_dashboard(root, frame, df, status_var)
    ).pack(pady=10)

    ttk.Button(
        frame,
        text="關閉程式",
        bootstyle="danger",
        command=root.destroy
    ).pack(pady=20)