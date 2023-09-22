# 对一个正弦信号进行上抽样和下抽样，观察时域和频域的变化

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# 生成原始信号
fs_original = 1000  # 原始采样率
t = np.linspace(0, 1, fs_original, endpoint=False)  # 时间向量
signal_frequency = 10  # 信号频率（Hz）
original_signal = np.sin(2 * np.pi * signal_frequency * t)

# 上抽样（增加采样率）
upsampling_factor = 3
fs_upsampled = fs_original * upsampling_factor  # 新的采样率
upsampled_signal = np.zeros(len(original_signal) * upsampling_factor)
upsampled_signal[::upsampling_factor] = original_signal

# 下抽样（降低采样率）
downsampling_factor = 3
fs_downsampled = fs_original // downsampling_factor  # 新的采样率
downsampled_signal = original_signal[::downsampling_factor]

# 计算频域图
original_signal_fft = fft(original_signal)
upsampled_signal_fft = fft(upsampled_signal)
downsampled_signal_fft = fft(downsampled_signal)

plt.figure(figsize=(14, 8))

# 绘制时域图
plt.subplot(3, 2, 1)
plt.plot(t, original_signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 2)
plt.plot(np.arange(len(upsampled_signal)) / fs_upsampled, upsampled_signal)
plt.title('Upsampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 3)
plt.plot(np.arange(len(downsampled_signal)) / fs_downsampled, downsampled_signal)
plt.title('Downsampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 计算频域图
original_signal_fft = fft(original_signal)
upsampled_signal_fft = fft(upsampled_signal)
downsampled_signal_fft = fft(downsampled_signal)

plt.subplot(3, 2, 4)
plt.plot(np.fft.fftfreq(len(original_signal), 1 / fs_original), np.abs(original_signal_fft))
plt.title('Original Signal Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

# 绘制频域图
plt.subplot(3, 2, 5)
plt.plot(np.fft.fftfreq(len(upsampled_signal), 1 / fs_upsampled), np.abs(upsampled_signal_fft))
plt.title('Upsampled Signal Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 6)
plt.plot(np.fft.fftfreq(len(downsampled_signal), 1 / fs_downsampled), np.abs(downsampled_signal_fft))
plt.title('Downsampled Signal Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

