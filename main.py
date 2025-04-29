import time
import random
import string
import requests
from fake_useragent import UserAgent

# Mã mời của bạn
INVITE_CODE = "56495544"

# Số tài khoản muốn tạo
TOTAL_ACCOUNTS = 20

# Thời gian delay giữa mỗi lần (từ 10 đến 30 giây, bạn có thể chỉnh)
DELAY_RANGE = (10, 30)

# Fake User-Agent cho mỗi lần gửi
ua = UserAgent()

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@gmail.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def register_novelah(email, password):
    headers = {
        "User-Agent": ua.random,
        "Content-Type": "application/json",
    }

    data = {
        "email": email,
        "password": password,
        "invite_code": INVITE_CODE
    }

    try:
        response = requests.post("https://api.novelah.com/api/register", json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"[✅] Đăng ký thành công: {email}")
        else:
            print(f"[❌] Lỗi khi đăng ký ({email}):", response.text)
    except Exception as e:
        print(f"[⚠️] Lỗi kết nối: {e}")

# Chạy vòng lặp tạo tài khoản
for i in range(TOTAL_ACCOUNTS):
    print(f"\n📨 Tạo tài khoản thứ {i+1}/{TOTAL_ACCOUNTS}")
    email = generate_random_email()
    password = generate_random_password()
    register_novelah(email, password)
    
    delay = random.randint(*DELAY_RANGE)
    print(f"⏳ Đợi {delay} giây trước khi tiếp tục...\n")
    time.sleep(delay)

print("\n🎉 Hoàn tất tạo tài khoản!")
