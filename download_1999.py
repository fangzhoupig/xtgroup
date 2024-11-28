import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import subprocess

months = ["12"]
# months = ["03"]
# 目标网站的URL
base_url = "http://geoschemdata.wustl.edu/ExtData/GEOS_0.5x0.625_AS/MERRA2/2006/"
download_dir = "2006/"
os.makedirs(download_dir, exist_ok=True)

for month in months:
    # 构建每个月份的URL
    month_url = urljoin(base_url, month + "/")

    # 发起HTTP请求并获取页面内容
    response = requests.get(month_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 创建一个目录来存储下载的文件
    month_folder = os.path.join(download_dir, month)
    os.makedirs(month_folder, exist_ok=True)

    # 遍历页面上的链接
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.endswith(".nc4"):  # 假设您想下载.nc文件
            file_url = urljoin(month_url, href)
            file_name = os.path.basename(file_url)
            file_path = os.path.join(month_folder, file_name)

            # 检查文件是否已经存在，如果存在就跳过
            if os.path.exists(file_path):
                print(f"File {file_name} already exists. Skipping...")
                continue

            # 使用wget下载文件
            wget_command = ["wget", "-c", "-O", file_path, file_url]
            try:
                subprocess.run(wget_command, check=True)
                print(f"Downloaded {file_name} successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error downloading {file_name}: {e}")

print("下载完成！")
