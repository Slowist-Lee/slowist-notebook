from PIL import Image
import numpy as np

def load_image(path):
    return Image.open(path)

def compare_images(img1, img2):
    # Ensure both images have the same mode and size
    if img1.mode != img2.mode or img1.size != img2.size:
        raise ValueError("Images must have the same mode and size to be compared")

    # Convert images to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Calculate the difference
    diff = np.abs(arr1 - arr2)

    # Summarize differences
    total_diff = np.sum(diff)
    num_diff_pixels = np.count_nonzero(diff)
    
    return total_diff, num_diff_pixels, diff

def main():
    img1_path = 'image_with_steganography.png'
    img2_path = 'image_without_steganography.png'

    img1 = load_image(img1_path)
    img2 = load_image(img2_path)

    total_diff, num_diff_pixels, diff = compare_images(img1, img2)

    print(f'Total difference: {total_diff}')
    print(f'Number of differing pixels: {num_diff_pixels}')
    
    # Optionally save the diff image for visualization
    diff_image = Image.fromarray(diff)
    diff_image.save('diff_image.png')

if __name__ == "__main__":
    main()
