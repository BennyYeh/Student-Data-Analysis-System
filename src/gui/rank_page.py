import ttkbootstrap as ttk
from src.services.rank_service import calculate_rank


def show_rank(root, frame, df, status_var):

    from src.gui.menu_page import show_menu

    for w in frame.winfo_children():
        w.destroy()

    tree = ttk.Treeview(frame)
    tree.pack(fill="both", expand=True)

    ranked = calculate_rank(df)

    tree["columns"] = list(ranked.columns)
    tree["show"] = "headings"

    for c in ranked.columns:
        tree.heading(c, text=c)

    for _, row in ranked.iterrows():
        tree.insert("", "end", values=list(row))

    ttk.Button(
        frame,
        text="返回",
        command=lambda: show_menu(root, frame, df, status_var)
    ).pack(pady=10)