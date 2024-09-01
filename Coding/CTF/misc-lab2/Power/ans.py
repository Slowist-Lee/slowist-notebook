import numpy as np
import matplotlib.pyplot as plt

# 加载npz文件
data = np.load('attachment.npz')
index = data['index']
input_data = data['input']
trace = data['trace']

# 初始化密钥数组
key = [''] * 13

# 遍历每个index值
for i in range(13):
    # 获取当前index对应的所有trace
    idx = np.where(index == i)[0]
    traces = trace[idx]
    inputs = input_data[idx]

    # 计算每个input的平均功耗轨迹
    unique_inputs = np.unique(inputs)
    avg_traces = []
    for ui in unique_inputs:
        ui_traces = traces[inputs == ui]
        avg_trace = np.mean(ui_traces, axis=0)
        avg_traces.append(avg_trace)

    avg_traces = np.array(avg_traces)
    
    # 找到差异最大的trace
    max_diff = 0
    best_input = ''
    for j in range(len(unique_inputs)):
        for k in range(j+1, len(unique_inputs)):
            diff = np.linalg.norm(avg_traces[j] - avg_traces[k])
            if diff > max_diff:
                max_diff = diff
                best_input = unique_inputs[j]
    
    key[i] = best_input

print("Recovered Key:", ''.join(key))