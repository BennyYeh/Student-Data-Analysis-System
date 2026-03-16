#處理資料來源
import pandas as pd
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
from src.data.generate_data import generate_student_data
from src.data.load_data import load_csv_to_db
from src.database.db_connection import connect_db


def show_data_source(root, frame, status_var):

    # 清空畫面
    for w in frame.winfo_children():
        w.destroy()

    # ===== 置中容器 =====
    center_frame = ttk.Frame(frame)
    center_frame.pack(expand=True)

    ttk.Label(center_frame, text="選擇資料來源", font=("Arial", 28)).pack(pady=30)

    # =========================
    # 生成資料
    # =========================

    def generate_page():

        for w in frame.winfo_children():
            w.destroy()

        ttk.Label(frame, text="輸入生成資料筆數").pack(pady=10, padx=10)

        entry = ttk.Entry(frame)
        entry.pack()

        def generate():

            from src.gui.menu_page import show_menu

            try:
                n = int(entry.get())

                generate_student_data(n)
                df = load_csv_to_db()

                status_var.set(f"狀態: 成功生成 {n} 筆資料")

                show_menu(root, frame, df, status_var)

            except:
                status_var.set("狀態: 請輸入正確數字")

        ttk.Button(frame, text="確認生成", command=generate).pack(pady=10)

        ttk.Button(
            frame,
            text="返回",
            command=lambda: show_data_source(root, frame, status_var)
        ).pack(pady=10)

    # =========================
    # 匯入 CSV
    # =========================

    def load_csv():

        from src.gui.menu_page import show_menu

        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if not file:
            return

        try:
            df = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="cp950")

        status_var.set("狀態: CSV匯入成功")

        show_menu(root, frame, df, status_var)



    # =========================
    # 匯入 Excel
    # =========================

    def load_excel():

        from src.gui.menu_page import show_menu

        file = filedialog.askopenfilename(
            filetypes=[("Excel", "*.xlsx")]
        )

        if file:
            df = pd.read_excel(file)

            df.to_sql(
                "students",
                connect_db(),
                if_exists="replace",
                index=False
            )

            messagebox.showinfo("成功", "Excel 匯入成功")

            status_var.set("狀態: Excel 匯入成功")

            show_menu(root, frame, df, status_var)

    # =========================
    # 按鈕區
    # =========================

    ttk.Button(center_frame, text="自行生成資料", width=20, command=generate_page).pack(pady=10)

    ttk.Button(center_frame, text="匯入 CSV", width=20, command=load_csv).pack(pady=10)

    ttk.Button(center_frame, text="匯入 Excel", width=20, command=load_excel).pack(pady=10)

    ttk.Button(center_frame, text="關閉程式", width=20, bootstyle="danger", command=root.destroy).pack(pady=20)