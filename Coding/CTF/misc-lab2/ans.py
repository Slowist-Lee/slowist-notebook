import librosa
import soundfile
import numpy
from PIL import Image, ImageSequence

sr = 22050
num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'

img = Image.open('flag-1.gif')
frames = numpy.array([numpy.array(frame.copy().convert('RGB').getdata(),dtype=numpy.uint8).reshape(frame.size[1],frame.size[0],3) for frame in ImageSequence.Iterator(img)])
log_mel_spectrogram = numpy.array([[(frame[::quantize, (x) * (quantize * 2) + quantize, 2] == 0).sum() * quantize + min_db for x in range(num_freqs)] for frame in frames]).transpose()
print(log_mel_spectrogram.shape)
mel_spectrogram = librosa.db_to_power(log_mel_spectrogram)
reconstruct = librosa.feature.inverse.mel_to_audio(mel_spectrogram, sr, n_fft=fft_window_size, hop_length=frame_step_size, window=window_function_type)
print(reconstruct.shape)
soundfile.write('flag.wav', reconstruct, sr)