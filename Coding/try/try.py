import os
import subprocess
import zipfile

def run_crc32revise(filename):
    try:
        # 确保 input 参数正确，并确保以换行符结尾
        result = subprocess.run(
            ['python', '"D:/MyRepository/slowist-notebook/docs/Coding/try/crc32revise.py'],
            input=filename + '\n',
            capture_output=True,
            text=True,
            check=True
        )
        print(f"crc32revise.py output:\n{result.stdout}")  # 打印修复脚本的输出
        return result.returncode == 0  # 返回是否成功执行
    except subprocess.CalledProcessError as e:
        print(f"Error running crc32revise.py on {filename}:\n{e.stderr}")
        return False

def unzip_file(filepath, extract_to):
    try:
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return True
    except zipfile.BadZipFile:
        print(f"Bad Zip File: {filepath}")
        return False

def process_zip(filepath):
    current_file = filepath
    while True:
        print(f"Processing file: {current_file}")
        
        # 修复ZIP文件
        if not run_crc32revise(current_file):
            print(f"Failed to run crc32revise on {current_file}")
            break
        
        # 解压缩文件
        extract_dir = os.path.splitext(current_file)[0]
        if not unzip_file(current_file, extract_dir):
            print(f"Failed to unzip {current_file}")
            break
        
        # 找到新的ZIP文件
        new_zip_files = [f for f in os.listdir(extract_dir) if f.endswith('.zip')]
        if not new_zip_files:
            print("No more ZIP files to process")
            break
        
        # 更新路径为下一个嵌套的ZIP文件
        current_file = os.path.join(extract_dir, new_zip_files[0])
        print(f"Next file to process: {current_file}")

if __name__ == "__main__":
    initial_zip = "D:/MyRepository/slowist-notebook/docs/Coding/new/998_00bb42a0/997_7e1b2bb5/996_9b0398f2/995_0930b46b.zip"  # 起始压缩包的名称
    process_zip(initial_zip)


# import os
# import subprocess
# import zipfile

# def run_crc32revise(filename):
#     try:
#         # 使用 input 参数传递输入，并确保以换行符结尾
#         result = subprocess.run(
#             ['python3', 'crc32revise.py'],
#             input=filename + '\n',
#             capture_output=True,
#             text=True,
#             check=True
#         )
#         print(f"Output: {result.stdout}")  # 打印修复脚本的输出，方便调试
#         return result.returncode == 0  # 返回是否成功执行
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e.stderr}")
#         return False

# def unzip_file(filepath, extract_to):
#     try:
#         with zipfile.ZipFile(filepath, 'r') as zip_ref:
#             zip_ref.extractall(extract_to)
#         return True
#     except zipfile.BadZipFile:
#         print(f"Bad Zip File: {filepath}")
#         return False

# def process_zip(filepath):
#     current_file = filepath
#     while True:
#         print(f"Processing file: {current_file}")
        
#         # 修复ZIP文件
#         if not run_crc32revise(current_file):
#             print(f"Failed to run crc32revise on {current_file}")
#             break
        
#         # 解压缩文件
#         extract_dir = os.path.splitext(current_file)[0]
#         if not unzip_file(current_file, extract_dir):
#             print(f"Failed to unzip {current_file}")
#             break
        
#         # 找到新的ZIP文件
#         new_zip_files = [f for f in os.listdir(extract_dir) if f.endswith('.zip')]
#         if not new_zip_files:
#             print("No more ZIP files to process")
#             break
        
#         # 更新路径为下一个嵌套的ZIP文件
#         current_file = os.path.join(extract_dir, new_zip_files[0])
#         print(f"Next file to process: {current_file}")

# if __name__ == "__main__":
#     initial_zip = "D:/MyRepository/slowist-notebook/docs/Coding/new/998_00bb42a0/997_7e1b2bb5/996_9b0398f2/995_0930b46b.zip"  # 起始压缩包的名称
#     process_zip(initial_zip)
