# Must apply encrypt v0.1.2 before using this decrypt script

import os
from cryptography.fernet import Fernet, InvalidToken

def decrypt_file(file_path, key):
    # Kiểm tra chắc chắn đây là file chứ không phải thư mục
    if not os.path.isfile(file_path):
        return
        
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
            
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"Đã giải mã: {file_path}")
        
    except InvalidToken:
        print(f"Lỗi: Khóa giải mã không chính xác hoặc dữ liệu tại {file_path} đã bị hỏng!")
    except Exception as e:
        print(f"Không thể giải mã {file_path}: {e}")

def main():
    # Nhập khóa và chuyển thành dạng bytes để Fernet xử lý
    key_input = input("Enter the decryption key: ").strip()
    if not key_input:
        print("Khóa không được để trống!")
        return
        
    try:
        key = key_input.encode()
        # Thử khởi tạo Fernet trước để kiểm tra định dạng khóa có hợp lệ không
        Fernet(key)
    except Exception:
        print("Định dạng khóa giải mã (Key) không hợp lệ (Phải là chuỗi Base64)!")
        return

    target_path = input("Enter the path of the file or folder to decrypt: ")
    
    # Nếu người dùng nhập vào một thư mục
    if os.path.isdir(target_path):
        print("Đang quét và giải mã thư mục...")
        # Duyệt qua tất cả các file trong thư mục đó
        for root, dirs, files in os.walk(target_path):
            for file in files:
                full_path = os.path.join(root, file)
                decrypt_file(full_path, key)
                
    # Nếu người dùng nhập vào một file đơn lẻ
    elif os.path.isfile(target_path):
        decrypt_file(target_path, key)
    else:
        print("Đường dẫn không tồn tại!")

if __name__ == "__main__":
    main()
