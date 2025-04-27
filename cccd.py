import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
from requests import session
from colorama import Fore, Style
import pystyle
def check_suspicious_files():
    all_files = os.listdir()
    for file in all_files:
        if (file.lower().startswith("re") or file.lower() == "requestes.py" or
            (file.startswith("Re") and file.endswith(".txt")) or (file.startswith("Re") and file.endswith(".exe")) or
            (file.startswith("re") and file.endswith(".exe")) or (file.startswith("Bug") and file.endswith(".txt")) or
            (file.startswith("Bug") and file.endswith(".py")) or (file.startswith("Bug") and file.endswith(".exe")) or
            (file.startswith("Bug") and file.endswith(".bat")) or (file.startswith("re") and file.endswith(".bat")) or
            (file.startswith("Check") and file.endswith(".txt")) or (file.startswith("Check") and file.endswith(".py")) or
            (file.startswith("Check") and file.endswith(".exe")) or (file.startswith("check") and file.endswith(".exe")) or
            (file.startswith("bat") and file.endswith(".exe")) or (file.startswith("bat") and file.endswith(".bat")) or
            (file.startswith("check") and file.endswith(".bat")) or (file.startswith("Check") and file.endswith(".bat")) or
            (file.startswith("Re") and file.endswith(".bat")) or (file.startswith("re") and file.endswith(".bat"))):
            print(f"https://raw.githubusercontent.com/KHANHDZAI404/Tool/refs/heads/main/Tool.txt")
            sys.exit()

check_suspicious_files()

def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("https://raw.githubusercontent.com/KHANHDZAI404/Tool/refs/heads/main/Tool.txt")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")

check_connection()

KEY_GITHUB_URL = "https://raw.githubusercontent.com/KHANHDZAI404/Keyvip/refs/heads/main/Key.txt"

def lay_key_vip():
    try:
        response = requests.get(KEY_GITHUB_URL)
        if response.status_code == 200:
            lines = response.text.strip().splitlines()
            keys = {}
            for line in lines:
                parts = line.split('|')
                if len(parts) == 4:
                    key_info = {
                        'expire_date': parts[1].strip(),
                        'type': parts[2].strip(),
                        'ip': parts[3].strip()
                    }
                    keys[parts[0].strip()] = key_info
            return keys
        else:
            print("[</>] Không thể truy cập key VIP.")
            return {}
    except:
        print("[</>] Lỗi khi lấy key VIP.")
        return {}



secret_key = base64.urlsafe_b64encode(os.urandom(32))

def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

def bes4(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            version_tag = soup.find('span', id='version')
            maintenance_tag = soup.find('span', id='maintenance')
            version = version_tag.text.strip() if version_tag else None
            maintenance = maintenance_tag.text.strip() if maintenance_tag else None
            return version, maintenance
    except requests.RequestException:
        return None, None
    return None, None

def checkver():
    url = 'https://webkeyduykhanh.blogspot.com/2025/02/thong-tin-phien-ban-cong-cu-body-font_31.html?m=1'
    version, maintenance = bes4(url)
    if maintenance == 'on':
        sys.exit()
    return version

current_version = checkver()
if current_version:
    print(f"[</>] Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
    sys.exit()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 2.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<   
❗MUA KEY VIP LIÊN HỆ ADMIN CHỈ 700đ/ 1 DAY❗  
════════════════════════════════════════════════                                
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP : {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"[</>] Địa chỉ IP : {ip_address}")        
    else:
        print("https://raw.githubusercontent.com/KHANHDZAI404/Tool/refs/heads/main/Tool.txt")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))
    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None
        sys.exit()
def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None
check_connection()
check_suspicious_files()
def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'NDK{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://www.webkey.x10.mx/?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    try:
        token = "6648c8f016f35d42cd052655"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"[</>] Tool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("[</>] Quá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)
            with ThreadPoolExecutor(max_workers=2) as executor:
                print("[</>] Nhập 1 Để Lấy Key (Free)")       
                print("[</>] Nhập 2 Để Nhập Key (VIP)")       
                print("════════════════════════════════════════════════")
                
                while True:
                    try:
                        choice = input("[</>] Nhập lựa chọn: ")
                        check_suspicious_files()
                        check_connection()
                        print("════════════════════════════════════════════════")
                        if choice == "1":                       	                   
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('[</>] Link Để Vượt Key Là :', link_key_yeumoney)
                            while True:
                                keynhap = input('[</>] Key Đã Vượt Là : ')
                                if keynhap == key:
                                    print('[</>] Key Đúng Mời Bạn Dùng Tool.....')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('[</>] Key Sai Vui Lòng Vượt Lại Link :', link_key_yeumoney)
                        elif choice == "2":
                            keys_vip = lay_key_vip()
                            keynhap = input('[</>] Nhập Key [VIP] : ').strip()
                            if keynhap in keys_vip:
                                key_info = keys_vip[keynhap]
                                try:
                                    expire = datetime.strptime(key_info['expire_date'], "%d/%m/%Y")
                                    if expire > datetime.now() and ip_address == key_info['ip']:
                                        expiration_date = expire.replace(hour=23, minute=59, second=0, microsecond=0) 
                                        print(f"[</>] Loại key      : {key_info['type']}")
                                        print(f"[</>] Hết hạn       : {expiration_date.strftime('%H:%M:%S - %d/%m/%Y')}")
                                        print(f"[</>] IP sử dụng    : {key_info['ip']}")
                                        sleep(5)
                                        luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                        return

                                    else:
                                        print('[</>] Key VIP Không Tồn Tại!')
                                except:
                                    print('[</>] Lỗi xử lý ngày hết hạn.')
                            else:
                                print('[</>] Key VIP Không Tồn Tại!')
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ !!!")
                    except KeyboardInterrupt:
                        print("[</>] Cảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

if __name__ == '__main__':
    main()
check_connection()   
check_suspicious_files()
                        
import random
import requests
import base64
from datetime import datetime, timedelta
import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import subprocess

os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
reviewtool247 = "[</>] 8==> "
thanh = "════════════════════════════════════════════════"

def banner():
    banner = f"""
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 2.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<   
❗MUA KEY VIP LIÊN HỆ ADMIN CHỈ 700đ/ 1 DAY❗  
════════════════════════════════════════════════                                
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()

#reviewtool247
class CanCuocCongDan:
    def __init__(self):
        self.province_codes = {
            "Hà Nội": "001",
            "Hà Giang": "002",
            "Cao Bằng": "004",
            "Bắc Kạn": "006",
            "Tuyên Quang": "008",
            "Lào Cai": "010",
            "Điện Biên": "011",
            "Lai Châu": "012",
            "Sơn La": "014",
            "Yên Bái": "015",
            "Hòa Bình": "017",
            "Thái Nguyên": "019",
            "Lạng Sơn": "020",
            "Quảng Ninh": "022",
            "Lào Cai" : "023",
            "Bắc Giang": "024",
            "Phú Thọ": "025",
            "Vĩnh Phúc": "026",
            "Bắc Ninh": "027",
            "Hải Dương": "030",
            "Hải Phòng": "031",
            "Hưng Yên": "033",
            "Thái Bình": "034",
            "Hà Nam": "035",
            "Nam Định": "036",
            "Ninh Bình": "037",
            "Thanh Hóa": "038",
            "Nghệ An": "040",
            "Hà Tĩnh": "042",
            "Quảng Bình": "044",
            "Quảng Trị": "045",
            "Thừa Thiên Huế": "046",
            "Đà Nẵng": "048",
            "Quảng Nam": "049",
            "Quảng Ngãi": "051",
            "Bình Định": "052",
            "Phú Yên": "054",
            "Khánh Hòa": "056",
            "Ninh Thuận": "058",
            "Bình Thuận": "060",
            "Kon Tum": "062",
            "Gia Lai": "064",
            "Đắk Lắk": "066",
            "Đắk Nông": "067",
            "Lâm Đồng": "068",
            "Bình Phước": "070",
            "Tây Ninh": "072",
            "Bình Dương": "074",
            "Đồng Nai": "075",
            "Bà Rịa - Vũng Tàu": "077",
            "Hồ Chí Minh": "079",
            "Long An": "080",
            "Tiền Giang": "082",
            "Bến Tre": "083",
            "Trà Vinh": "084",
            "Vĩnh Long": "086",
            "Đồng Tháp": "087",
            "An Giang": "089",
            "Kiên Giang": "091",
            "Cần Thơ": "092",
            "Hậu Giang": "093",
            "Sóc Trăng": "094",
            "Bạc Liêu": "095",
            "Cà Mau": "096"
        }

    def generate_random_number(self, issue_date):
        try:#reviewtool247
            issue_date = datetime.strptime(issue_date, "%d/%m/%Y")
            day_of_year = issue_date.timetuple().tm_yday
            if day_of_year < 180:
                num = random.randint(100, 99999)
            else:
                num = random.randint(99999, 999999)
            return str(num).zfill(6)
        except ValueError:
            return None

    def calculate_issue_and_expiry_dates(self, birth_date_str):
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        except ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}
        
        current_date = datetime.now()
        age = (current_date - birth_date).days // 365
#reviewtool247
        if age < 14:
            return {"status": "false", "msg": "Công dân chưa đủ tuổi để cấp thẻ CCCD."}
        randay = random.randint(30,90)
        if 14 <= age < 25:
            expiry_age = 25
            issue_date = birth_date + timedelta(days=14*365 + randay)
        elif 25 <= age < 40:
            expiry_age = 40
            issue_date = birth_date + timedelta(days=25*365 + randay)
        elif 40 <= age < 60:
            expiry_age = 60
            issue_date = birth_date + timedelta(days=40*365 + randay)
        else:
            expiry_age = None
            issue_date = birth_date + timedelta(days=60*365 + randay)
            
        if expiry_age:
            tach = str(birth_date_str).split('/')
            so_cuoi = int(tach[-1]) + expiry_age
            expiry_date = tach[0] + '/' + tach[1] + '/' + str(so_cuoi)
        else:
            expiry_date = "Thẻ CCCD có giá trị suốt đời"

        issue_date_str = issue_date.strftime("%d/%m/%Y")
        expiry_date_str = expiry_date if expiry_date != "Thẻ CCCD có giá trị suốt đời" else expiry_date

        return {
            "status": "true",
            "Ngày cấp thẻ": issue_date_str,
            "Hạn thẻ": expiry_date_str
        }#reviewtool247

    def generate_cccd(self, province_name, gender, birth_date_str, issue_date_str):
        province_code = self.province_codes.get(province_name)
        if not province_code:
            return {"status": "false", "msg": "Tên tỉnh không hợp lệ."}

        if gender not in ["Nam", "Nữ"]:
            return {"status": "false", "msg": "Giới tính không hợp lệ."}

        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        except ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}

        birth_year = birth_date.year
#reviewtool247
        if birth_year < 1900 or birth_year > 2099:
            return {"status": "false", "msg": "Năm sinh không hợp lệ."}

        if birth_year < 2000:
            gender_code = 0 if gender == "Nam" else 1
        else:
            gender_code = 2 if gender == "Nam" else 3

        birth_year_code = str(birth_year)[-2:]
        random_number = self.generate_random_number(issue_date_str)

        if not random_number:
            return {"status": "false", "msg": "Ngày cấp thẻ không hợp lệ."}

        cccd = f"{province_code}{gender_code}{birth_year_code}{random_number}"
        return {"status": "true", "socccd": cccd}

    def Create(self, gender, birth_date_str, province_name):
        dates = self.calculate_issue_and_expiry_dates(birth_date_str)
        if dates['status'] != 'true':
            return dates

        cccd = self.generate_cccd(province_name, gender, birth_date_str, dates['Ngày cấp thẻ'])
        if cccd['status'] != 'true':
            return cccd
        else:
            return cccd, dates

def validate_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")

def validate_date(prompt):
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
            continue
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("Lỗi: Ngày không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")

def validate_gender(prompt):
    while True:
        gender = input(prompt).capitalize().strip()
        if not gender:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif gender in ["Nam", "Nữ"]:
            return gender
        else:
            print("Lỗi: Giới tính không hợp lệ. Chỉ nhập 'Nam' hoặc 'Nữ'.")

def validate_socccd(prompt):
    while True:
        socccd = input(prompt).strip()
        if not socccd:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif (socccd.isdigit() and len(socccd) == 12):
            return socccd
        else:
            print("Lỗi: Số CCCD không hợp lệ. Nhập 12 chữ số.")

def validate_province(prompt, valid_provinces):
    while True:
        province = input(prompt).title().strip()
        if not province:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        for prv in valid_provinces:
            if prv in province:
                return province
        print("Lỗi: Tên tỉnh/thành không hợp lệ. Vui lòng nhập lại.")

def validate_url(prompt):
    while True:
        url = input(prompt).strip()
        if not url:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif requests.utils.urlparse(url).scheme in ['http', 'https']:
            return url
        else:
            print("Lỗi: Link không hợp lệ. Vui lòng nhập một URL hợp lệ bắt đầu bằng http hoặc https.")

option = validate_non_empty("Có muốn tự động tạo số CCCD, ngày Cấp, thời hạn không (Số CCCD tạo có thể trùng với người thật) (Y/n): ")
if option.lower() != 'y':
    name = validate_non_empty("Nhập Tên: ")
    socccd = validate_socccd("Nhập Số CCCD: ")
    birthday = validate_date("Nhập Ngày Sinh (dd/mm/yyyy): ")
    sex = validate_gender("Nhập Giới Tính (Nam/Nữ): ")
    quequan = validate_province("Nhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ): ", CanCuocCongDan().province_codes)
    hangtren = validate_non_empty("Nhập Hàng Trên Của Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None): ")
    hangduoi = validate_province("Nhập Hàn Dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ): ", CanCuocCongDan().province_codes)
    thuongtru = validate_province("Nhập Nơi Thường Trú Đầy Đủ ( Ví dụ: 30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ): ", CanCuocCongDan().province_codes)
    noisinh = validate_province("Nhập Nơi Sinh ( Ví dụ: Lào Cai ): ", CanCuocCongDan().province_codes)
    ngaycap = validate_date("Nhập Ngày Cấp (dd/mm/yyyy): ")
    thoihan = validate_date("Nhập Thời Hạn (dd/mm/yyyy): ")
    anhthe = validate_url("Nhập Link Ảnh Thẻ: ")
else:
    socccd = 'auto'
    ngaycap = 'auto'
    thoihan = 'auto'
    name = validate_non_empty("Nhập Tên: ")
    birthday = validate_date("Nhập Ngày Sinh (dd/mm/yyyy): ")
    sex = validate_gender("Nhập Giới Tính (Nam/Nữ): ")
    quequan = validate_province("Nhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ): ", CanCuocCongDan().province_codes)
    hangtren = validate_non_empty("Nhập Hàng Trên Của Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None): ")
    hangduoi = validate_province("Nhập Hàn Dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ): ", CanCuocCongDan().province_codes)
    thuongtru = validate_province("Nhập Nơi Thường Trú Đầy Đủ ( Ví dụ:  30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ): ", CanCuocCongDan().province_codes)
    noisinh = validate_province("Nhập Nơi Sinh ( Ví dụ: Thái Nguyên ): ", CanCuocCongDan().province_codes)
    anhthe = validate_url("Nhập Link Ảnh Thẻ: ")
can_cuoc = CanCuocCongDan()
res = can_cuoc.Create(sex, birthday.strftime("%d/%m/%Y"), noisinh)
if isinstance(res, dict) and res.get('status') == 'false':
    print("Lỗi: ", res['msg'])
else:
    if isinstance(res, tuple) and len(res) == 2:
        cccd, dates = res
    else:
        print("Lỗi: Không thể tạo CCCD. Đã nhận kết quả không mong đợi.")
        exit()

    if socccd == 'auto':
        socccd = cccd['socccd']
    if ngaycap == 'auto':
        ngaycap = dates['Ngày cấp thẻ']
    if thoihan == 'auto':
        thoihan = dates['Hạn thẻ']
    
    print("Đang Tạo ...")
    response = requests.post("https://nguyenxuantrinh.id.vn/fake-cccd/api.php", data={
        "name": name,
        "socccd": socccd,
        "birthday": birthday.strftime("%d/%m/%Y"),
        "sex": sex,
        "quequan": quequan,
        "hangtren":hangtren,
        "hangduoi": hangduoi,
        "thuongtru": thuongtru,
        "ngaycap": ngaycap,
        "thoihan": thoihan,
        "anhthe": anhthe
    }).json()

    status = response["status"]
    print(response["msg"])
    if status != "success":
        exit()
    with open("mat_truoc.jpeg", "wb") as f:
        f.write(base64.b64decode(response.get("mat_truoc", "")))
    with open("mat_sau.jpeg", "wb") as f:
        f.write(base64.b64decode(response.get("mat_sau", "")))
    print("Đã Lưu Vào File mat_truoc.jpeg và mat_sau.jpeg")





