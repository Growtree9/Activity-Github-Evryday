# simulate_activity.py

import datetime
import subprocess

# تاریخ و زمان فعلی را بدست می‌آوریم
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# فرض می‌کنیم که self-hosted runner در مسیر پروژه جاری قرار دارد
project_path = "."

# ایجاد یک فایل جدید با نام simulate_activity.txt و افزودن زمان فعلی به آن
with open(f"{project_path}/simulate_activity.txt", "a") as file:
    file.write(f"Commit at {current_datetime}\n")

# اضافه کردن و commit کردن فایل تغییر یافته
subprocess.run(["git", "add", "."], cwd=project_path)
subprocess.run(["git", "commit", "-m", f"Simulate activity at {current_datetime}"], cwd=project_path)

# چاپ پیام جلسه
print("Simulating GitHub Activity!")
