# 读入一段语音，将采样率变为8kHz,将时域信号变为:y(n) =(-1)"x(n),听一下两个信号并分析比较它们在幅度谱上的区别;
# 如果我们拿到y(n)的傅里叶变换Y(ej“)，如何还原x(n)?请用python实现
# 降采样后的信号很像原始信号，但是音调变了，变成了低音调
# 时域反转后的信号在幅度上和原始信号完全相同，但是相位相反，音调变了，变成了低音调
# 使用逆离散傅立叶变换 (IDFT) 恢复原始信号，
import numpy as np
import scipy.io.wavfile as wavfile
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play

import playsound
# 读取音频文件
input_filename = "sing.wav"
sample_rate, x = wavfile.read(input_filename)

# 降低采样率到 8kHz
target_sample_rate = 8000
downsample_factor = sample_rate // target_sample_rate
x_downsampled = x[::downsample_factor]

# 将 x_downsampled 转换为一维数组
x_downsampled = x_downsampled.flatten()
# 保存降采样后的音频
output_filename = "downsampled_sing.wav"
wavfile.write(output_filename, target_sample_rate, x_downsampled.astype(np.int16))
# 播放降采样后的音频
# playsound.playsound(input_filename)
# 播放降采样后的音频
# playsound.playsound(output_filename)

# 应用时域反转操作 y(n) = (-1)^n * x(n)
n = np.arange(len(x_downsampled))
y = (-1)**n * x_downsampled

# 比较原始信号和变换后的信号在幅度上的区别
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(x_downsampled)
plt.title("Original Signal")
plt.subplot(2, 1, 2)
plt.plot(y)
plt.title("Transformed Signal")
plt.tight_layout()
plt.show()

# 保存变换后的信号
output_filename = "transformed_sing.wav"
wavfile.write(output_filename, target_sample_rate, y.astype(np.int16))

# 对变换后的信号做傅里叶变换
Y = np.fft.fft(y)
# 计算频率轴
freqs = np.fft.fftfreq(len(y), 1 / target_sample_rate)


# 从频域信号恢复原始信号
def reconstruct_signal(freqs, Y):
    # 将频率轴和频域信号转换为一维数组
    freqs = freqs.flatten()
    Y = Y.flatten()

    # 使用逆离散傅立叶变换 (IDFT) 恢复原始信号
    x_restored = np.fft.ifft(Y)

    return x_restored

# 从频域信号恢复原始信号
y_reconstructed = reconstruct_signal(freqs, Y)
# 上抽样（增加采样率）
upsampling_factor = sample_rate // target_sample_rate  # 采样率的倍数
upsampling_signal = np.zeros(len(y_reconstructed) * upsampling_factor)
upsampling_signal[::upsampling_factor] = y_reconstructed

# 绘制恢复后的信号
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(y_reconstructed)
plt.title("Reconstructed Signal")
plt.subplot(2, 1, 2)
plt.plot(upsampling_signal)
plt.title("Upsampled Signal")
plt.tight_layout()
plt.show()

# 保存恢复后的信号
output_filename = "upsampling_signal.wav"
upsampling_signal = abs(upsampling_signal)
wavfile.write(output_filename, target_sample_rate, upsampling_signal.astype(np.int16))


