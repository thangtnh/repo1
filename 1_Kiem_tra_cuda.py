import torch
print(torch.cuda.is_available())  # Trả về True nếu CUDA khả dụng
print(torch.cuda.get_device_name(0))  # In ra tên GPU nếu có

#---------------------------------------------------------
import torch

# Kiểm tra xem CUDA có được hỗ trợ không
print(torch.cuda.is_available())

# Kiểm tra số lượng thiết bị GPU
print(torch.cuda.device_count())

# Kiểm tra tên của GPU đầu tiên nếu có
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))