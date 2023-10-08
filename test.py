import customtkinter as ctk


def main():
    root = ctk.CTk()
    root.title("Font Demo")

    # Tải font chữ từ tệp .ttf
    ctk.FontManager.load_font("Fonts/Play-Bold.ttf")

    # Tạo CTkLabel với font chữ custom
    label = ctk.CTkLabel(root, text="Hello, World!", font=("Play-Bold", 16))
    label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
