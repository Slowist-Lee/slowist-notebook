result = b'\xfc\xf2\x1dE\xf7\xd8\xf7\x1e\xed\xccQ\x8b9:z\xb5\xc7\xca\xea\xcd\xb4b\xdd\xcb\xf2\x939\x0b\xec\xf2'
RT = [[0] * 10 for _ in range(3)]

index = 0
for i in range(10):
    for j in range(3):
        RT[j][i] = result[index]
        index += 1

# 打印恢复的 RT
for row in RT:
    print(row)
