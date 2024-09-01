import subprocess
from multiprocessing import Pool, Manager

def run_elf_program(inputs):
    results = []
    for input_value in inputs:
        # 将输入值作为字符串传递给1.elf程序
        input_string = str(input_value)
        
        # 使用subprocess运行1.elf，并传递输入值
        process = subprocess.Popen(['/mnt/d/MyRepository/slowist-notebook/docs/Coding/CTF/reverse-lab1/bc/challenge2'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        stdout, _ = process.communicate(input=input_string)
        
        # 检查输出是否包含"awesome"
        if "awesome" in stdout.lower():  # 使用lower()确保不区分大小写
            results.append(input_value)
    
    return results

def main():
    manager = Manager()
    found = manager.Value('i', 0)  # 用于在多个进程间共享的标志变量

    def batch_run(batch):
        if found.value:
            return []  # 如果已经找到，立即返回空列表
        results = run_elf_program(batch)
        if results:
            found.value = 1  # 设置标志
        return results

    batch_size = 1000  # 每次处理的输入值数量，可以根据具体情况调整
    input_values = range(10000000000000000)  # 遍历0到9999999999999999的所有值
    batches = [input_values[i:i + batch_size] for i in range(0, len(input_values), batch_size)]

    with Pool(processes=20) as pool:  # 使用8个进程
        for result_batch in pool.imap_unordered(batch_run, batches):
            if result_batch:
                print(f"找到结果为 'awesome' 的输入值：{result_batch[0]}")
                pool.terminate()
                break
        else:
            print("未找到符合条件的输入值。")

if __name__ == "__main__":
    main()
