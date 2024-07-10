from PIL import Image
import numpy as np
import scipy.fftpack

def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

def extract_dct_coefficients(block):
    return scipy.fftpack.dct(scipy.fftpack.dct(block.T, norm='ortho').T, norm='ortho')

def extract_lsb(data):
    int_data = data.astype(int)
    return int_data & 1

def decode_message_from_lsb(lsb_data):
    bit_string = ''.join(map(str, lsb_data.flatten()))
    byte_array = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in byte_array if int(byte, 2) != 0])
    return message

def main(image_path):
    image_data = load_image(image_path)
    height, width, _ = image_data.shape

    lsb_data = []

    # Process each 8x8 block of the image
    for row in range(0, height, 8):
        for col in range(0, width, 8):
            block = image_data[row:row+8, col:col+8, 0]  # Use only one color channel (e.g., R)
            dct_block = extract_dct_coefficients(block - 128)  # Centering the pixel values
            lsb_block = extract_lsb(dct_block)
            lsb_data.extend(lsb_block.flatten())  # 展平 LSB 块，并将其添加到 lsb_data 列表中

    lsb_data = np.array(lsb_data)
    message = decode_message_from_lsb(lsb_data)

    print(f"Extracted message: {message}")

if __name__ == "__main__":
    image_path = "1.jpg"
    main(image_path)
