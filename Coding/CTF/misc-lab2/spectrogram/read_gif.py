from PIL import Image, ImageSequence
import librosa
import soundfile
import numpy as np
file = Image.open("D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lab2/spectrogram/flag-2.gif")
gif_data = np.array([np.array(frame.copy().convert('RGB').getdata(),dtype=np.uint8).reshape(frame.size[1],frame.size[0],3) for frame in ImageSequence.Iterator(file)])

num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'
sr=22050
spectrogram = np.zeros((len(gif_data), num_freqs))
id=0
for frame in gif_data:
    for i in range(num_freqs):
        s = i * (quantize * 2) + quantize
        data=frame[::quantize,s,0]
        b = (data == 0).sum()
        value=b*quantize+min_db
        spectrogram[id, i]=value
    id+=1
audio = librosa.feature.inverse.mel_to_audio(librosa.db_to_power(spectrogram.transpose()),  hop_length=frame_step_size, window=window_function_type)
# reconstruct = librosa.istft(mel_spectrogram, hop_length=frame_step_size, window=window_function_type)
print(type(audio))
# save
soundfile.write('D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lab2/spectrogram/flag-6.wav', audio, sr)
