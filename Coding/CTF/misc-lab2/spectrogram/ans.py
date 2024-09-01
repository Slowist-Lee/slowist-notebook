from PIL import Image, ImageSequence
import librosa
import numpy as np
import soundfile as sf

file = Image.open("D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lab2/spectrogram/flag-1.gif")
gif_data = []
# for frame in ImageSequence.Iterator(file):
#     gif_data.append(np.array(frame))
# from PIL import Image
# file = Image.open("flag.gif")

try:
    while True:
        gif_data.append(np.array(file))
        file.seek(file.tell() + 1)
except:
    print("[+] Read gif file")


num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'
sample_rate = 22050

spectrogramT = []

for data in gif_data:
    res = []
    transposed_data = data.transpose()  # Transpose the 2D array
    # print(transposed_data)
    for ind, line in enumerate(transposed_data):
        num = sum(line)
        print(ind)
        if ind % 4 == 3:
            print(1)
            res.append(num + min_db)
        # print(num)
    # print(res)
    spectrogramT.append(res)
# print(spectrogramT)
# Ensure all rows in spectrogramT have the same length
max_len = max(len(row) for row in spectrogramT)
spectrogramT = [row + [min_db] * (max_len - len(row)) for row in spectrogramT]

spectrogram = np.array(spectrogramT).transpose()

# Convert to audio
y = librosa.feature.inverse.mel_to_audio(
    librosa.db_to_power(spectrogram),
    sr=sample_rate,
    n_fft=fft_window_size,
    hop_length=frame_step_size,
    win_length=fft_window_size,
    window=window_function_type,
)
# Save to file
sf.write("flag-ans.wav", y, sample_rate)


