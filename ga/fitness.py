import subprocess
import json
import os

def run_rips_docker():
    # Thay rips_container bằng tên container bạn chạy
    container_name = "rips_container"

    # Chạy lệnh RIPS scan trong Docker container
    cmd = [
        "docker", "exec", container_name,
        "rips", "scan", "/var/www/html", "--output", "/var/www/html/report.json"
    ]
    subprocess.run(cmd, check=True)

def read_report(report_path="report/report.json"):
    if not os.path.exists(report_path):
        print("Report file not found:", report_path)
        return 0
    with open(report_path, "r") as f:
        data = json.load(f)
    vulns = data.get("vulnerabilities", [])
    return len(vulns)

def fitness(individual):
    # TODO: bạn có thể dùng 'individual' để thay đổi config hoặc source trước khi chạy RIPS
    try:
        run_rips_docker()
        score = read_report()
    except Exception as e:
        print("Error running RIPS:", e)
        score = 0
    return score,
