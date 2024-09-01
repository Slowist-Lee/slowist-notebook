import os
import subprocess

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

file_path = '/mnt/d/MyRepository/slowist-notebook/docs/Coding/CTF/lab0/heartbeat_input.bin'  # 修改为你的二进制文件路径
data = read_binary_file(file_path)

# 更改当前工作目录
os.chdir("/mnt/d/MyRepository/slowist-notebook/docs/Coding/CTF/lab0")

# 检查当前工作目录
print("Current working directory:", os.getcwd())

# 运行程序
for i in range(1):
    result = subprocess.run(["./program"], input=data, capture_output=True)
    print("Run", i+1, "output:")
    print(result.stdout)  # 直接输出二进制数据
    if result.stderr:
        print("Error output:", result.stderr)
