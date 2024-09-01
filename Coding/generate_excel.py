# 1. Xenoticas 112 11 74 144 10 121 172 218
# 2. 两三口 131 31 58 134 200 128 93
# 3. Dogma 18 46 66 101 116 124 147 156 226
# 4. chyka 26 65 90 109 127  130 149 185 196 199 211 212 223 228
# 5. Alex 135 136 161 221 242
# 6. 好就行🌟  88 150 188
# 7. 拾熙Azure 17 152 160
import pandas as pd
first_column = range(1, 257)
df = pd.DataFrame(first_column, columns=['id'])
df['situation'] = 0
print(df)


