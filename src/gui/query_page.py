import ttkbootstrap as ttk
from src.services.query_service import query_student


def show_query(root, frame, df, status_var):

    from src.gui.menu_page import show_menu

    for w in frame.winfo_children():
        w.destroy()

    combo = ttk.Combobox(frame, values=df["name"].tolist())
    combo.pack(pady=10)

    tree = ttk.Treeview(frame)
    tree.pack(fill="both", expand=True)

    def query():

        result = query_student(df, combo.get())

        tree.delete(*tree.get_children())

        tree["columns"] = list(result.columns)
        tree["show"] = "headings"

        for c in result.columns:
            tree.heading(c, text=c)

        for _, row in result.iterrows():
            tree.insert("", "end", values=list(row))

    def clear():
        tree.delete(*tree.get_children())

    ttk.Button(frame, text="查詢", command=query).pack(pady=5)

    ttk.Button(frame, text="清除結果", command=clear).pack(pady=5)

    ttk.Button(
        frame,
        text="返回",
        command=lambda: show_menu(root, frame, df, status_var)
    ).pack(pady=10)