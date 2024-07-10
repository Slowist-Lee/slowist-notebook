s='BPLQECUPEZFTSUJJQDZWGGXBOXZMEUZSDHVGKVMNEVWSKDKICMAIUOB'
output=0
for i in range(len(s)):
    output=output*26+(ord(s[i])-65)
# convert to bytes, then group -> hex
anss=bin(output)[2:]
while len(anss)%8!=0:
    anss = '0' +anss # make sure can -> hex
ans=''
for i in range(0,len(anss),8):
    byte=anss[i:i+8]
    num10=int(byte,2)
    ans+=chr(num10)
print(ans)
