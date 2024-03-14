## Phần mềm tính điểm
    Mã nguồn mở Python tính điểm cho học sinh THPT

Xin chào, đây là một phần mềm tính điểm sử dụng Python và thư viện Customtkinter. Được phát triển bởi Lê Quang Khải, học sinh trường THPT Trường Chinh. Phần mềm này hy vọng sẽ trở thành công cụ hữu ích giúp các bạn dễ dàng tính toán và thống kê điểm số. Ngoài ra, vì là mã nguồn mở nên hi vọng sẽ giúp các bạn phần nào đó trong việc tiếp cận ngôn ngữ lập trình dễ dàng hơn. Nếu còn có bất cứ thắc mắc gì về ứng dụng, báo lỗi vui lòng liên hệ với tôi tại Zalo: 0387290231

## Chức Năng Chính
    1. Xếp loại học sinh (theo thông tư 22)
    2. Tính điểm trung bình môn
    3. Tính điểm trung bình năm
    4. Tính điểm xét tốt nghiệp

# Hướng Dẫn Sử Dụng
1. Cài đặt Python tại website https://www.python.org/ phiên bản mới nhất
2. Mở Terminal hoặc Command Prompt.
3. Điều hướng đến thư mục chứa file `requirements.txt`.
4. Chạy lệnh sau để cài đặt các thư viện cần thiết:

    ```bash
    pip install -r requirements.txt
    ```

Lệnh trên sẽ cài đặt tất cả các thư viện được liệt kê trong file `requirements.txt` với phiên bản tương ứng.

Lưu ý: Đảm bảo rằng bạn đã kích hoạt môi trường ảo (nếu có) trước khi chạy lệnh trên.

5. Ở cửa sổ Terminal hoặc Command Prompt hiện tại, gõ lệnh

    ```bash
    python ktools.py
    ```
để chạy phần mềm

6. Hoàn tất!
## Công Nghệ
**Python**

**UI**: customtkinter


## Authors

- [@lequangkhai06](https://www.github.com/lequangkhai06)


## Chuyển Đổi Từ File Python -> .exe

Để chuyển đổi một file Python sang định dạng thực thi (.exe) trên Windows, bạn có thể sử dụng công cụ `pyinstaller`. Dưới đây là các bước để thực hiện điều này:

1. **Cài đặt PyInstaller**: Đầu tiên, bạn cần cài đặt PyInstaller. Bạn có thể làm điều này bằng cách mở Terminal hoặc Command Prompt và chạy lệnh sau:

```bash
pip install pyinstaller
```

2. **Chuyển đổi file Python sang .exe**: Sau khi đã cài đặt PyInstaller, bạn có thể sử dụng nó để chuyển đổi file Python của mình thành một file .exe. Để làm điều này, hãy mở Terminal hoặc Command Prompt, điều hướng đến thư mục chứa file Python của bạn và chạy lệnh sau:

```bash
pyinstaller --onefile your_script.py
```

Trong đó, `your_script.py` là tên của file Python bạn muốn chuyển đổi. Lệnh trên sẽ tạo ra một file .exe trong thư mục `dist` trong thư mục hiện tại.

Lưu ý: Nếu mã nguồn của bạn sử dụng các thư viện không phải là phần của thư viện chuẩn Python, bạn cần đảm bảo rằng tất cả các thư viện này cũng đã được cài đặt trên máy tính nơi bạn chạy PyInstaller.