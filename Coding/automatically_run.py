# import subprocess
# filename='998_00bb42a0.zip'
# result = subprocess.run('python3 crc32revise.py',input=bytes(filename), stderr=subprocess.DEVNULL, capture_output=True, text=True, shell=True)
# filename=result.stdout
# while result.stdout!='':
#     result = subprocess.run('python3 crc32revise.py',input=bytes(filename), stderr=subprocess.DEVNULL, capture_output=True, text=True, shell=True)
#     filename=result.stdout

# import subprocess

# filename = '998_00bb42a0.zip'

# def update_crc(filename):
#     result = subprocess.run(['python3', 'crc32revise.py'], input=filename, stderr=subprocess.DEVNULL, capture_output=True, text=True)
#     process = subprocess.Popen('cd'+result.stdout)
#     return result.stdout

# filename = update_crc(filename).strip()
# while filename:
#     filename = update_crc(filename).strip()

import subprocess
import os

def update_crc(filename):
    result = subprocess.run(['python3', 'crc32revise.py'], input=filename.encode(), stderr=subprocess.DEVNULL, capture_output=True, text=True)
    return result.stdout

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing: {file_path}")
            filename = update_crc(file_path).strip()
            while filename:
                filename = update_crc(filename).strip()

# 设置要处理的根目录
root_directory = '998_00bb42a0'

process_directory(root_directory)
