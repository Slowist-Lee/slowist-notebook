def base26_decode(s):
    base = 26
    decoded_value = 0
    for char in s:
        decoded_value = decoded_value * base + (ord(char) - ord('A'))
    return decoded_value

def decimal_to_ascii(decimal_value):
    binary_str = bin(decimal_value)[2:]
    padding = (8 - len(binary_str) % 8) % 8
    binary_str = '0' * padding + binary_str

    ascii_str = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return ascii_str

input_str = 'BPLQECUPEZFTSUJJQDZWGGXBOXZMEUZSDHVGKVMNEVWSKDKICMAIUOB'


decoded_value = base26_decode(input_str)
ascii_str = decimal_to_ascii(decoded_value)

print(ascii_str)

def base26_decode(s):
    base = 26
    decoded_value = 0
    for char in s:
        decoded_value = decoded_value * base + (ord(char) - ord('A'))
    return decoded_value

def decimal_to_ascii(decimal_value):
    ascii_str = ''
    while decimal_value > 0:
        ascii_str = chr(decimal_value % 256) + ascii_str
        decimal_value //= 256
    return ascii_str

input_str = 'BPLQECUPEZFTSUJJQDZWGGXBOXZMEUZSDHVGKVMNEVWSKDKICMAIUOB'

decoded_value = base26_decode(input_str)
ascii_str = decimal_to_ascii(decoded_value)

print(ascii_str)
