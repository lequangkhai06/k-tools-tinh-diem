import customtkinter as ctk
import webbrowser
from PIL import Image


def Loading():
    root = ctk.CTk()
    root.title("Đang Tải Phần Mềm...")
    root.geometry('800x600')
    root.after(0, lambda: root.state('zoomed'))
    logo_path = ctk.CTkImage(Image.open(
        "Images/logo.png"), size=(270, 270))
    logo = ctk.CTkLabel(root, image=logo_path, text="")
    logo.pack(pady=150)
    progress = ctk.CTkProgressBar(
        root, orientation='horizontal', mode='determinate', progress_color="#50C878")
    progress.pack()
    progress.set(0)
    progress.start()
    ctk.CTkLabel(root, text="Đang tải dữ liệu...",
                 font=('Arial', 15)).pack(pady=10)
    ctk.CTkLabel(root, text="© 2023 By LEQUANGKHAI",
                 font=('Helvetica', 10)).pack(pady=2, side="bottom")
    root.after(2000, root.destroy)
    root.mainloop()


class CongCuTinhDiem(ctk.CTkTabview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(expand=True, pady=0, padx=0, fill="y")
        # config
        self.root = root
        self.update_idletasks()
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")
        self.root.geometry("900x700")
        self.root.title("CÔNG CỤ TÍNH ĐIỂM - THPT TRƯỜNG CHINH ĐĂK NÔNG")
        self.root.after(0, lambda: root.state('zoomed'))
        # Tạo tabs
        self.add("XẾP LOẠI HỌC SINH")
        self.add("TÍNH ĐIỂM TB MÔN")
        self.add("TÍNH ĐIỂM TB NĂM")
        self.add("TÍNH ĐIỂM XÉT TỐT NGHIỆP")
        self.add("VỀ PHẦN MỀM")
        # Thêm widgets vào tabs
        self.label1 = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="", anchor="center")
        # self.label1.grid(sticky='e')
        self.label2 = ctk.CTkLabel(master=self.tab("TÍNH ĐIỂM TB NĂM"))
        self.label2.grid(row=0, column=0)
        self.label3 = ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="", anchor="center")
        self.label3.grid(row=0, column=0, padx=20, pady=10)
        self.label4 = ctk.CTkLabel(master=self.tab(
            "VỀ PHẦN MỀM"), text="")
        self.label4.grid(row=0, column=0)
        self.label4 = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="")
        self.label4.grid(row=0, column=0)
        # images
        clearIcon = ctk.CTkImage(dark_image=Image.open("Images/clear.png"))
        resultIcon = ctk.CTkImage(dark_image=Image.open("Images/result.png"))
        offIcon = ctk.CTkImage(dark_image=Image.open("Images/turn-off.png"))
        # chuyển theme
        self.is_on = True
        self.lights_control = ctk.CTkFrame(self)
        self.lights_control.grid(row=0, column=0, rowspan=1, padx=(
            5, 5), pady=(10, 10), sticky="new")
        self.dark_theme_switch = ctk.CTkSwitch(
            master=self.lights_control, text="Mặc định", command=self.dark_theme)
        self.dark_theme_switch.grid(
            row=0, column=0, pady=10, padx=20, sticky="n")
        # đóng phần mềm
        ctk.CTkButton(master=self, image=offIcon, text="Đóng phần mềm", command=self.close_window,
                      fg_color="#fff", text_color="#000", hover_color="#fff", width=0).grid(pady=10, padx=10)
        # ============ TÍNH ĐIỂM TRUNG BÌNH MÔN: TAB 1 ============= #
        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="Tổng điểm kiểm tra 15p / điểm miệng", anchor="center").grid(
            row=0, column=0, padx=10, pady=10)
        self.entry1 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), placeholder_text="Ví dụ: (8 + 7 + 9) => 24")
        self.entry1.grid(row=0, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="Điểm kiểm tra giữa kỳ").grid(
            row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry2 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), placeholder_text="0")
        self.entry2.grid(row=1, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="Điểm kiểm tra cuối kỳ").grid(
            row=2, column=0, padx=10, pady=10, sticky="ew")
        self.entry3 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), placeholder_text="0")
        self.entry3.grid(row=2, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="Tổng số lần tham gia kiểm tra 15p / điểm miệng").grid(
            row=3, column=0, padx=10, pady=10, sticky="ew")
        self.entry4 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), placeholder_text="Ví dụ: 3 lần => 3")
        self.entry4.grid(row=3, column=1)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), image=clearIcon, text="Nhập lại", command=self.func_tinh_diem_tb_hoc_ky_reset, fg_color="#dc3545", hover_color="#FF0001").grid(row=4, column=0)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), image=resultIcon, text="Xem kết quả", command=self.func_tinh_diem_tb_hoc_ky).grid(row=4, column=1)

        self.ket_qua_tb_mon = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="")
        self.ket_qua_tb_mon.grid(row=5, columnspan=2, pady=10)

        # ========== TÍNH ĐIỂM TB NĂM: TAB 2 ============ #

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), text="Điểm trung bình học kỳ 1", anchor="center").grid(
            row=0, column=0, padx=10, pady=10)
        self.entry5 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), placeholder_text="0")
        self.entry5.grid(row=0, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), text="Điểm trung bình học kỳ 2").grid(
            row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry6 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), placeholder_text="0")
        self.entry6.grid(row=1, column=1)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), image=clearIcon, text="Nhập lại", command=self.func_tinh_diem_tb_nam_hoc_reset, fg_color="#dc3545", hover_color="#FF0001").grid(row=4, column=0)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), image=resultIcon, text="Xem kết quả", command=self.func_tinh_diem_tb_nam_hoc).grid(row=4, column=1)

        self.ket_qua_tb_mon = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="")
        self.ket_qua_tb_mon.grid(row=5, columnspan=2, pady=10)

        self.ket_qua_tb_nam_hoc = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB NĂM"), text="")
        self.ket_qua_tb_nam_hoc.grid(row=5, columnspan=2, pady=10)

        # ============ XẾP LOẠI HỌC SINH: TAB 3 ========== #

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Toán học", anchor="center").grid(
            row=0, column=0, padx=10, pady=10)
        self.entry7 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry7.grid(row=0, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Tin học").grid(
            row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry8 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry8.grid(row=1, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Ngữ văn").grid(
            row=2, column=0, padx=10, pady=10, sticky="ew")
        self.entry9 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry9.grid(row=2, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Lịch sử").grid(
            row=3, column=0, padx=10, pady=10, sticky="ew")
        self.entry10 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry10.grid(row=3, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Địa lí").grid(
            row=4, column=0, padx=10, pady=10, sticky="ew")
        self.entry11 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry11.grid(row=4, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Ngoại ngữ").grid(
            row=5, column=0, padx=10, pady=10, sticky="ew")
        self.entry12 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry12.grid(row=5, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: GDCD").grid(
            row=6, column=0, padx=10, pady=10, sticky="ew")
        self.entry13 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry13.grid(row=6, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: Công nghệ").grid(
            row=7, column=0, padx=10, pady=10, sticky="ew")
        self.entry14 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry14.grid(row=7, column=1)

        ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Điểm trung bình: GDQP").grid(
            row=8, column=0, padx=10, pady=10, sticky="ew")
        self.entry15 = ctk.CTkEntry(master=self.tab(
            "XẾP LOẠI HỌC SINH"), placeholder_text="0")
        self.entry15.grid(row=8, column=1)

        ctk.CTkButton(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="Nhập lại", command=self.phan_loai_hoc_luc_reset, image=clearIcon, fg_color="#dc3545", hover_color="#FF0001").grid(row=10, column=0)

        ctk.CTkButton(master=self.tab(
            "XẾP LOẠI HỌC SINH"), image=resultIcon, text="Xem kết quả", command=self.phan_loai_hoc_luc).grid(row=10, column=1)

        self.ket_qua_loai_hoc_sinh = ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="")
        self.ket_qua_loai_hoc_sinh.grid(row=11, columnspan=2)

        # VỀ PHẦN MỀM: TAB 4
        textbox = ctk.CTkTextbox(master=self.tab(
            "VỀ PHẦN MỀM"), width=600, corner_radius=15)
        text = """
        Xin chào, đây là một phần mềm tính điểm sử dụng Python và thư viện Customtkinter.
        Được phát triển bởi Lê Quang Khải, học sinh trường THPT Trường Chinh - Đăk Nông khóa 2021 - 2024.
        Phần mềm này hy vọng sẽ trở thành công cụ hữu ích giúp các bạn dễ dàng tính toán và thống kê điểm số. 
        Ngoài ra, vì là mã nguồn mở nên hi vọng sẽ giúp các bạn phần nào đó trong việc tiếp cận ngôn ngữ lập trình dễ dàng hơn. 
        Nếu còn có bất cứ thắc mắc gì về ứng dụng, báo lỗi. Liên hệ với tôi Zalo: 0387290231

        Changelog: 07-10-2023
        """
        textbox.insert("0.0", text)
        textbox.configure(state="disabled")
        textbox.place(relx=0.5, rely=0.5, anchor="center")

        # TÍNH ĐIỂM XÉT TỐT NGHIỆP: TAB 5

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Toán:", anchor="center").grid(
            row=0, column=0, padx=10, pady=10)
        self.entry16 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry16.grid(row=0, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Ngữ văn:").grid(
            row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry17 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry17.grid(row=1, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Ngoại ngữ:").grid(
            row=2, column=0, padx=10, pady=10, sticky="ew")
        self.entry18 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry18.grid(row=2, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Vật lí (hoặc Lịch sử):").grid(
            row=3, column=0, padx=10, pady=10, sticky="ew")
        self.entry19 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry19.grid(row=3, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Hóa học (hoặc Địa lí):").grid(
            row=4, column=0, padx=10, pady=10, sticky="ew")
        self.entry20 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry20.grid(row=4, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm môn Sinh học (hoặc GDCD):").grid(
            row=5, column=0, padx=10, pady=10, sticky="ew")
        self.entry21 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry21.grid(row=5, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm trung bình cả năm lớp 12:").grid(
            row=6, column=0, padx=10, pady=10, sticky="ew")
        self.entry22 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry22.grid(row=6, column=1)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm khuyến khích (nếu có):").grid(
            row=7, column=0, padx=10, pady=10, sticky="ew")
        self.entry23 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry23.grid(row=7, column=1)
        self.entry23.insert(0, 0)

        ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập điểm ưu tiên (nếu có):").grid(
            row=8, column=0, padx=10, pady=10, sticky="ew")
        self.entry24 = ctk.CTkEntry(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), placeholder_text="0")
        self.entry24.grid(row=8, column=1)
        self.entry24.insert(0, 0)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="Nhập lại", command=self.func_tinh_diem_tot_nghiep_thpt_reset, image=clearIcon, fg_color="#dc3545", hover_color="#FF0001").grid(row=10, column=0, padx=10)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), image=resultIcon, text="Xem kết quả hệ THPT", command=self.func_tinh_diem_tot_nghiep_thpt).grid(row=10, column=1, padx=10)

        ctk.CTkButton(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), image=resultIcon, text="Xem kết quả hệ GDTX", command=self.func_tinh_diem_tot_nghiep_gdtx, fg_color="#0d6efd", hover_color="#0d6efd").grid(row=10, column=2, padx=10)

        self.ket_qua_xet_tot_nghiep_thpt = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM XÉT TỐT NGHIỆP"), text="")
        self.ket_qua_xet_tot_nghiep_thpt.grid(row=11, columnspan=2)

    # =============== HÀM TÍNH ĐIỂM ================== #

    def func_tinh_diem_tb_hoc_ky(self):
        try:
            tong_diem_thuong_xuyen = float(self.entry1.get())
            diem_giua_ky = float(self.entry2.get())
            diem_hoc_ky = float(self.entry3.get())
            so_luong_bai_kiem_tra = float(self.entry4.get())
            if (tong_diem_thuong_xuyen > 40 or diem_giua_ky > 10 or so_luong_bai_kiem_tra < 1 or tong_diem_thuong_xuyen < 0):
                self.ket_qua_tb_mon.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10)
            else:
                diemtbhk = (tong_diem_thuong_xuyen + 2 * diem_giua_ky +
                            3 * diem_hoc_ky) / (so_luong_bai_kiem_tra + 5)
                self.ket_qua_tb_mon.configure(
                    text=f"Điểm trung bình môn của bạn là: {round(diemtbhk, 1)}", corner_radius=10)
        except ValueError:
            self.ket_qua_tb_mon.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10)

    def func_tinh_diem_tb_nam_hoc(self):
        try:
            diem_hoc_ky_1 = float(self.entry5.get())
            diem_hoc_ky_2 = float(self.entry6.get())
            if (diem_hoc_ky_1 > 10 or diem_hoc_ky_2 > 10 or diem_hoc_ky_1 < 0 or diem_hoc_ky_2 < 0):
                self.ket_qua_tb_nam_hoc.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10)
            else:
                diemtbnam = (diem_hoc_ky_1 + 2 * diem_hoc_ky_2) / 3
                self.ket_qua_tb_nam_hoc.configure(
                    text=f"Điểm trung bình cả năm của bạn là: {round(diemtbnam,1)}", corner_radius=10)
        except ValueError:
            self.ket_qua_tb_nam_hoc.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10)

    def phan_loai_hoc_luc(self):
        try:
            if (float(self.entry7.get()) >= 0 or float(self.entry8.get()) >= 0 or float(self.entry9.get()) >= 0 or float(self.entry10.get()) >= 0 or float(self.entry11.get()) >= 0 or float(self.entry12.get()) >= 0 or float(self.entry13.get()) >= 0 or float(self.entry14.get()) >= 0 or float(self.entry15.get()) >= 0):
                diem_hoc_ky = []
                entries = [self.entry7, self.entry8, self.entry9, self.entry10,
                           self.entry11, self.entry12, self.entry13, self.entry14, self.entry15]
                for entry in entries:
                    diem_hoc_ky.append(float(entry.get()))
                """
                Phân loại học lực của học sinh theo thông tư 22
                Tốt, Khá, Đạt, Chưa đạt
                Args:
                diem_hoc_ky: Danh sách điểm học kì từng môn của học sinh.
                Returns:
                Mức học lực của học sinh.
                """
                diemtb = sum(diem_hoc_ky)/len(diem_hoc_ky)
                so_mon_chua_dat = sum(
                    diem_hoc_ky_mon < 5.0 for diem_hoc_ky_mon in diem_hoc_ky)
                # Kiểm tra điều kiện để đạt mức Tốt.

                if (all(diem_hoc_ky_mon >= 6.5 for diem_hoc_ky_mon in diem_hoc_ky) and
                        sum(diem_hoc_ky_mon >= 8.0 for diem_hoc_ky_mon in diem_hoc_ky) >= 6):
                    result = "Tốt"
                # Kiểm tra điều kiện để đạt mức Khá.

                elif (all(diem_hoc_ky_mon >= 5.0 for diem_hoc_ky_mon in diem_hoc_ky) and
                        sum(diem_hoc_ky_mon >= 6.5 for diem_hoc_ky_mon in diem_hoc_ky) >= 6):
                    result = "Khá"

                # Kiểm tra điều kiện để đạt mức Đạt.
                elif so_mon_chua_dat <= 1 and all(diem_hoc_ky_mon >= 3.5 for diem_hoc_ky_mon in diem_hoc_ky):
                    result = "Đạt"

                # Các trường hợp còn lại đều là Chưa đạt.

                else:
                    result = "Chưa đạt"

                self.ket_qua_loai_hoc_sinh.configure(
                    text=f"""
                        {"Học sinh xuất sắc!" if result == "Tốt" else ""}
                        Kết quả học tập: {result}
                        Điểm trung bình: {round(diemtb,2)}
                        """, corner_radius=10)

            else:
                self.ket_qua_loai_hoc_sinh.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)

        except ValueError:
            self.ket_qua_loai_hoc_sinh.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)

    def func_tinh_diem_tot_nghiep_thpt(self):
        try:
            toan = float(self.entry16.get())
            van = float(self.entry17.get())
            ngoai_ngu = float(self.entry18.get())
            # ============================================= #
            mon_phu_1 = float(self.entry19.get())
            mon_phu_2 = float(self.entry20.get())
            mon_phu_3 = float(self.entry21.get())
            diem_tb_lop_12 = float(self.entry22.get())
            diem_khuyen_khich = float(self.entry23.get())
            diem_uu_tien = float(self.entry24.get())
            # ============================================= #
            if any(diem < 0 for diem in [toan, van, ngoai_ngu, mon_phu_1, mon_phu_2, mon_phu_3, diem_tb_lop_12, diem_khuyen_khich, diem_uu_tien]):
                self.ket_qua_xet_tot_nghiep_thpt.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)
            else:
                diem_to_hop = (mon_phu_1+mon_phu_2+mon_phu_3)/3
                diemtn = round(((diem_to_hop+toan+van+ngoai_ngu +
                          diem_khuyen_khich)/4*7+diem_tb_lop_12*3)/10+diem_uu_tien, 2)
                if (any(diem <= 1 for diem in [toan, van, ngoai_ngu, mon_phu_1, mon_phu_2, mon_phu_3]) or diemtn < 5):
                    self.ket_qua_xet_tot_nghiep_thpt.configure(
                        text=f"""
                        Bạn đã trượt tốt nghiệp có môn điểm liệt hoặc điểm tốt nghiệp dưới 5!!
                        Điểm xét tốt nghiệp của bạn là: {diemtn}
                        Bạn cần ít nhất {round(5-diemtn, 2)} điểm nữa để đỗ tốt nghiệp
                        """, corner_radius=10)
                else:
                    self.ket_qua_xet_tot_nghiep_thpt.configure(
                        text=f"""
                    Bạn đã đỗ tốt nghiệp!
                    Điểm xét tốt nghiệp của bạn là: {diemtn}
                    """, corner_radius=10)
        except ValueError:
            self.ket_qua_xet_tot_nghiep_thpt.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)

    def func_tinh_diem_tot_nghiep_gdtx(self):
        try:
            toan = float(self.entry16.get())
            van = float(self.entry17.get())
            ngoai_ngu = float(self.entry18.get())
            # ============================================= #
            mon_phu_1 = float(self.entry19.get())
            mon_phu_2 = float(self.entry20.get())
            mon_phu_3 = float(self.entry21.get())
            diem_tb_lop_12 = float(self.entry22.get())
            diem_khuyen_khich = float(self.entry23.get())
            diem_uu_tien = float(self.entry24.get())
            # ============================================= #
            if any(diem < 0 for diem in [toan, van, ngoai_ngu, mon_phu_1, mon_phu_2, mon_phu_3, diem_tb_lop_12, diem_khuyen_khich, diem_uu_tien]):
                self.ket_qua_xet_tot_nghiep_thpt.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)
            else:
                diem_to_hop = (mon_phu_1+mon_phu_2+mon_phu_3)/3
                diemtn = round((((diem_to_hop+toan+van)/3 + diem_khuyen_khich/4)
                          * 7+diem_tb_lop_12*3)/10+diem_uu_tien, 2)
                if (any(diem <= 1 for diem in [toan, van, ngoai_ngu, mon_phu_1, mon_phu_2, mon_phu_3]) or diemtn < 5):
                    self.ket_qua_xet_tot_nghiep_thpt.configure(
                        text=f"""
                        Bạn đã trượt tốt nghiệp có môn điểm liệt hoặc điểm tốt nghiệp dưới 5
                        Điểm xét tốt nghiệp của bạn là: {diemtn}
                        Bạn cần ít nhất {round(5-diemtn, 2)} điểm nữa để đỗ tốt nghiệp
                        """, corner_radius=10)
                else:
                    self.ket_qua_xet_tot_nghiep_thpt.configure(
                        text=f"""
                    Bạn đã đỗ tốt nghiệp!
                    Điểm xét tốt nghiệp của bạn là: {diemtn}
                    """, corner_radius=10)
        except ValueError:
            self.ket_qua_xet_tot_nghiep_thpt.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)
    # ====== ĐÓNG PHẦN MỀM ============ #

    def close_window(self):
        self.root.destroy()
    # ====== CHUYỂN ĐỔI THEME ========= #

    def dark_theme(self, event=None):
        if self.is_on:
            ctk.set_appearance_mode("Dark")
            self.dark_theme_switch.configure(text="Tối")
            self.is_on = False
        else:
            ctk.set_appearance_mode("Light")
            self.dark_theme_switch.configure(text="Sáng")
            self.is_on = True

    # ========= HÀM XOÁ ĐIỂM ======== #
    def func_tinh_diem_tb_hoc_ky_reset(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.ket_qua_tb_mon.configure(
            text="", text_color="#dc3545", corner_radius=10)

    def func_tinh_diem_tb_nam_hoc_reset(self):
        self.entry5.delete(0, 'end')
        self.entry6.delete(0, 'end')
        self.ket_qua_tb_nam_hoc.configure(
            text="", text_color="#dc3545", corner_radius=10)

    def phan_loai_hoc_luc_reset(self):
        self.entry7.delete(0, 'end')
        self.entry8.delete(0, 'end')
        self.entry9.delete(0, 'end')
        self.entry10.delete(0, 'end')
        self.entry11.delete(0, 'end')
        self.entry12.delete(0, 'end')
        self.entry13.delete(0, 'end')
        self.entry14.delete(0, 'end')
        self.entry15.delete(0, 'end')
        self.ket_qua_loai_hoc_sinh.configure(
            text="", text_color="#dc3545", corner_radius=10)

    def func_tinh_diem_tot_nghiep_thpt_reset(self):
        self.entry16.delete(0, 'end')
        self.entry17.delete(0, 'end')
        self.entry18.delete(0, 'end')
        self.entry19.delete(0, 'end')
        self.entry20.delete(0, 'end')
        self.entry21.delete(0, 'end')
        self.entry22.delete(0, 'end')
        self.entry23.delete(0, 'end')
        self.entry24.delete(0, 'end')
        self.ket_qua_xet_tot_nghiep_thpt.configure(
            text="", text_color="#dc3545", corner_radius=10)


def open_web():
    webbrowser.open('//fb.com/KhaiDeveloper')


Loading()
root = ctk.CTk()
app = CongCuTinhDiem(master=root)
copyright_label = ctk.CTkLabel(
    master=root, text="© 2023 By LEQUANGKHAI", corner_radius=20, cursor="hand2")
copyright_label.pack(side="bottom")
copyright_label.bind("<Button-1>", lambda e: open_web())
root.mainloop()