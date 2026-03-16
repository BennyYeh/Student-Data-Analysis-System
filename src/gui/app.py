import ttkbootstrap as ttk
from src.gui.data_source_page import show_data_source


def start_app():

    root = ttk.Window(themename="solar")  # 將root設定為視窗並將顏色設定為暖色調
    root.title("學生資料分析系統")

    # ===== 視窗置中 =====
    window_width = 1000
    window_height = 700

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # ===== 狀態列 =====
    status_var = ttk.StringVar()
    status_var.set("狀態: 等待資料選擇")

    # ===== 可滾動Canvas =====
    main_canvas = ttk.Canvas(root)
    main_canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
    scrollbar.pack(side="right", fill="y")

    main_canvas.configure(yscrollcommand=scrollbar.set)

    # ===== GUI內容容器 =====
    main_frame = ttk.Frame(main_canvas)

    # anchor 改成 center 讓內容水平置中
    main_canvas.create_window((0, 0), window=main_frame, anchor="n")

    def on_configure(event):
        main_canvas.configure(scrollregion=main_canvas.bbox("all"))

    main_frame.bind("<Configure>", on_configure)

    # ===== 滑鼠滾輪 =====
    def _on_mousewheel(event):
        main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    main_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # ===== 狀態列 =====
    status_label = ttk.Label(root, textvariable=status_var)
    status_label.pack(side="bottom", fill="x")

    # ===== 第一頁 =====
    show_data_source(root, main_frame, status_var)

    root.mainloop()