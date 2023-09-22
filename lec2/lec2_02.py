# 在不同采样率下生成2s、440Hz的正弦波，并播放
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

# 44100Hz,标准的 CD 音质采样率
# 8000Hz,标准的电话音频质量采样率
# 1000Hz,人耳能够听到的最低频率,也是sounddevice库最低的采样率
# 20000Hz,人耳能够听到的最高频率

fs = 1000

filename = 'sine_wave.wav'

def write_audio(filename, audio, fs):
    # 将音频文件的值归一化到[-1,1]之间
    audio = audio / np.max(np.abs(audio))
    # 将浮点数转换为整数
    audio = (audio * 32767).astype(np.short)
    # 将音频文件写入到.wav文件中
    wav.write(filename, fs, audio)

def create_sine_wave(filename, duration, freq):
    # 生成时间序列
    time = np.arange(duration * fs) / fs
    # 生成正弦波
    audio = np.sin(2 * np.pi * freq * time)
    # 将正弦波写入到.wav文件中
    write_audio(filename, audio, fs)

def play_audio(filename):
    # 读取音频文件
    fs, audio = wav.read(filename)
    # 播放音频文件
    sd.play(audio, fs)
    # 等待音频播放完成
    sd.wait()

if __name__ == '__main__':
    duration = 2  # 2秒钟
    freq = 440.0  # 440Hz
    create_sine_wave(filename, duration, freq)
    play_audio(filename)
