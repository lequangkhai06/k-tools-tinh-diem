import customtkinter as ctk
import webbrowser
from PIL import Image


class CongCuTinhDiem(ctk.CTkTabview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(expand=False, pady=0, padx=0, fill="y")
        # config
        self.root = root
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root.geometry("900x700")
        self.root.title("CÔNG CỤ TÍNH ĐIỂM - THPT TRƯỜNG CHINH ĐĂK NÔNG")
        # Tạo tabs
        self.add("XẾP LOẠI HỌC SINH")
        self.add("TÍNH ĐIỂM TB MÔN")
        self.add("TÍNH ĐIỂM TB NĂM")
        self.add("VỀ ỨNG DỤNG")
        # Thêm widgets vào tabs
        self.label1 = ctk.CTkLabel(master=self.tab(
            "TÍNH ĐIỂM TB MÔN"), text="", anchor="center")
        self.label1.grid(row=0, column=0)
        self.label2 = ctk.CTkLabel(master=self.tab("TÍNH ĐIỂM TB NĂM"))
        self.label2.grid(row=0, column=0)
        self.label3 = ctk.CTkLabel(master=self.tab(
            "XẾP LOẠI HỌC SINH"), text="")
        self.label3.grid(row=0, column=0)
        self.label4 = ctk.CTkLabel(master=self.tab(
            "VỀ ỨNG DỤNG"), text="")
        self.label4.grid(row=0, column=0)
        # images
        clearIcon = ctk.CTkImage(dark_image=Image.open("Images/clear.png"))
        resultIcon = ctk.CTkImage(dark_image=Image.open("Images/result.png"))
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

        # VỀ ỨNG DỤNG: TAB 4
        self.about_us = ctk.CTkLabel(master=self.tab(
            "VỀ ỨNG DỤNG"), text="""
            Xin chào, đây là một ứng dụng sử dụng ngôn ngữ lập trình Python
            và thư viện Customtkinter để tạo giao diện người dùng cho hệ thống
            công cụ tính điểm, theo quy định công văn số 22 của Bộ Giáo Dục.
            Được phát triển bởi Lê Quang Khải, học sinh khóa 2021 - 2024
            Ứng dụng này hy vọng sẽ trở thành công cụ hữu ích giúp các bạn dễ dàng trong việc tính toán và thống kê điểm số.
            Ngoài ra, vì là mã nguồn mở nên hi vọng sẽ giúp ích các bạn phần nào
            đó trong việc tiếp cận ngôn ngữ lập trình.
            Cảm ơn!!!

            Changelog: 07-10-2023



                        Nếu còn có bất cứ thắc mắc gì về ứng dụng, báo lỗi. Liên hệ với tôi tại zalo/0387290231
            """, anchor="center", font=('Arial',12))
        self.about_us.grid(row=0)

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
                average_score = (tong_diem_thuong_xuyen + 2 * diem_giua_ky +
                                 3 * diem_hoc_ky) / (so_luong_bai_kiem_tra + 5)
                self.ket_qua_tb_mon.configure(
                    text=f"Điểm trung bình môn của bạn là: {round(average_score,1)}", text_color="#fff", corner_radius=10)
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
                average_score = (diem_hoc_ky_1 + 2 * diem_hoc_ky_2) / 3
                self.ket_qua_tb_nam_hoc.configure(
                    text=f"Điểm trung bình cả năm của bạn là: {round(average_score,1)}", text_color="#fff", corner_radius=10)
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
                        Điểm trung bình: {round(diemtb,1)}
                        """, text_color="#fff", corner_radius=10)

            else:
                self.ket_qua_loai_hoc_sinh.configure(
                    text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)

        except ValueError:
            self.ket_qua_loai_hoc_sinh.configure(
                text="Vui lòng nhập điểm hợp lệ.", text_color="#dc3545", corner_radius=10, pady=20)

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


def open_web():
    webbrowser.open('//fb.com/KhaiDeveloper')


root = ctk.CTk()
app = CongCuTinhDiem(master=root)
copyright_label = ctk.CTkLabel(
    master=root, text="Design by LEQUANGKHAI", text_color="#ffcc70", corner_radius=20, cursor="hand2")
copyright_label.pack(side="bottom")
copyright_label.bind("<Button-1>", lambda e: open_web())
root.mainloop()