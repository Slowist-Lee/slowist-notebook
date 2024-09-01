MT = matrix(Zmod(256), [[?, ?, ?], [?, ?, ?], [?, ?, ?]]) # ? means unknown number
assert MT.is_invertible()
flag = "AAA{?????????????????????????}" # ? means unknown printable char
FT = matrix(Zmod(256), 3, 10)
for i in range(3):
	for j in range(10):
		FT[i, j] = ord(flag[i + j * 3]) #FT储存的是ord值
RT = MT * FT
result = b''
for i in range(10):
	for j in range(3):
		result += bytes([RT[j, i]])
print(result)
# b'\xfc\xf2\x1dE\xf7\xd8\xf7\x1e\xed\xccQ\x8b9:z\xb5\xc7\xca\xea\xcd\xb4b\xdd\xcb\xf2\x939\x0b\xec\xf2'
# ?????????????????????????
# TESTFLAGTESTFLAGTESTFLAGT

for i in range(32,129):
	for j in range(32,129):
		for k in range(32,129):
			for n in range(32,129):
				array[1][1]=i
[[252 242 29],[69,247,216],[247,30,237]]
[[65,65,65],[123,?,?],[?,?,?]]