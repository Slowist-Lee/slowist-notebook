import numpy as np
import librosa
import soundfile as sf
from PIL import Image

# 参数设置
num_freqs = 32
min_db = -60
max_db = 30
quantize = 2
color_pixel = (0, 0, 255)
sr = 22050
fft_window_size = 2048
frame_step_size = 512
n_mels = 32

# 读取GIF文件
def read_gif(path):
    with Image.open(path) as im:
        frames = []
        try:
            while True:
                frame = np.array(im.convert("RGB"))
                frames.append(frame)
                im.seek(im.tell() + 1)
        except EOFError:
            pass
    return frames

# 将梅尔频谱图转换为音频信号
def spectrogram_to_audio(spectrogram, sr, fft_window_size, hop_length, n_mels):
    spectrogram = np.array(spectrogram).T  # 转置以匹配 librosa 的输入格式
    spectrogram = librosa.db_to_power(spectrogram)
    stft_matrix = librosa.feature.inverse.mel_to_stft(spectrogram, sr=sr, n_fft=fft_window_size, power=2.0)
    audio = librosa.griffinlim(stft_matrix, hop_length=hop_length, win_length=fft_window_size)
    return audio

# 从 GIF 中提取帧
frames = read_gif("flag-1.gif")
spectrogram = []

for frame in frames:
    frame_height, frame_width, _ = frame.shape
    spectrogram_frame = np.zeros(num_freqs)

    for freq in range(num_freqs):
        for i in range(min_db, max_db + 1, quantize):
            y = frame_height - 1 - int((i - min_db) / quantize)
            if (frame[y, 2*freq] == color_pixel).all():
                spectrogram_frame[freq] = i
                break

    spectrogram.append(spectrogram_frame)

# 将梅尔频谱图转换为音频信号
audio = spectrogram_to_audio(spectrogram, sr, fft_window_size, frame_step_size, n_mels)

# 保存音频文件
sf.write('flag-1.wav', audio, sr)
