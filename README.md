# Genetic Algorithm + RIPS Static Analysis for DVWA

## Mục tiêu

Sử dụng thuật toán di truyền (Genetic Algorithm - GA) để tối ưu hóa việc phát hiện lỗ hổng bảo mật trên ứng dụng DVWA
bằng công cụ phân tích mã nguồn tĩnh RIPS.

---

## Cấu trúc dự án

- `dvwa/`: source code DVWA.
- `rips/`: Dockerfile và script để chạy RIPS phân tích.
- `ga/`: mã nguồn Python chạy thuật toán GA, bao gồm hàm fitness kết nối với RIPS.
- `report/`: nơi lưu file kết quả phân tích JSON.
- `requirements.txt`: thư viện Python cần cài.

---

## Hướng dẫn chạy

### 1. Build và chạy container RIPS

```bash
cd rips
docker build -t rips_image .
docker run -d --name rips_container -p 8080:80 -v $(pwd)/../dvwa:/var/www/html rips_image
```

### 2. Cài thư viện Python

pip install -r requirements.txt

### 3. Chạy thuật toán GA

python ga/ga_main.py
