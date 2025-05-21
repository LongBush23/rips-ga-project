import subprocess
import os

def run_command(cmd_list):
    """
    Chạy command shell, trả về True nếu thành công, False nếu lỗi.
    """
    try:
        subprocess.run(cmd_list, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command {cmd_list}: {e}")
        return False

def file_exists(path):
    return os.path.exists(path)

def read_json(path):
    import json
    with open(path, 'r') as f:
        return json.load(f)

def write_to_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def update_dvwa_code(individual, dvwa_path="../dvwa"):
    """
    Ví dụ hàm chỉnh sửa mã nguồn DVWA dựa trên cá thể GA.
    Có thể dùng cá thể individual để bật/tắt tính năng, sửa config,...
    """
    # Ví dụ đơn giản: ghi cá thể ra file config
    config_path = os.path.join(dvwa_path, "config_ga.txt")
    bits_str = ''.join(str(b) for b in individual)
    write_to_file(config_path, bits_str)
    print(f"Updated DVWA config with individual: {bits_str}")
