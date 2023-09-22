# 通过能量检测音频文件的起始和结束位置

# 通过能量检测音频文件的起始和结束位置

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def read_audio(filename):
    # 读取音频文件
    fs, audio = wav.read(filename)
    # 将音频文件转换为浮点数
    audio = audio.astype(float)  # 使用内置的float类型
    # 将音频文件的值归一化到[-1,1]之间
    audio = audio / np.max(np.abs(audio))
    return audio, fs

def cal_energy(audio, frame_size, frame_shift):
    # 计算音频文件的帧数
    n_frames = len(audio) // frame_shift
    # 计算音频文件的能量
    energy = np.zeros(n_frames)
    for i in range(n_frames):
        start = i * frame_shift
        end = min(len(audio), start + frame_size)
        # 计算每一帧的能量
        energy[i] = np.sum(audio[start:end] ** 2)
    return energy

def vad(audio, energy, threshold):
    # 计算音频文件的起始和结束位置
    start = 0
    while start < len(energy) and energy[start] < threshold:
        start += 1
    end = len(energy) - 1
    while end >= 0 and energy[end] < threshold:
        end -= 1
    return start, end

def plot_audio(audio, fs, start, end):
    # 计算音频文件的时间
    time = np.arange(len(audio)) * (1.0 / fs)
    # 绘制音频文件的波形图
    plt.plot(time, audio, color='black')
    # 绘制音频文件的起始和结束位置
    plt.axvline(x=time[start * 160], color='red', label='Speech Start')
    plt.axvline(x=time[end * 160], color='blue', label='Speech End')
    # 设置图形的标题和坐标轴
    plt.title('Waveform of Audio')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()


if __name__ == '__main__':
    # 读取音频文件
    audio, fs = read_audio('sing.wav')
    # 计算音频文件的能量
    energy = cal_energy(audio, frame_size=400, frame_shift=160)
    # 动态选择阈值
    threshold = np.mean(energy) * 0.1
    # 通过能量检测音频文件的起始和结束位置
    start, end = vad(audio, energy, threshold)
    # 绘制音频文件的波形图
    plot_audio(audio, fs, start, end)
    print('Speech Start: {:.2f}s'.format(start * 160 / fs))
    print('Speech End: {:.2f}s'.format(end * 160 / fs))
    # 显示图形
    plt.show()