# 验证信道+1，信噪比+6%
import numpy as np
import matplotlib.pyplot as plt

# 生成原始信号
fs = 1000  # 采样率
t = np.linspace(0, 1, fs, endpoint=False)  # 时间向量
signal_frequency = 10  # 信号频率（Hz）
original_signal = np.sin(2 * np.pi * signal_frequency * t)

# 8位量化：基本无影响，56.52dB
# 7位量化：基本无影响，50.44dB
# 6位量化：基本无影响，45.40dB
# 5位量化：基本无影响，39.78dB
# 4位量化：开始出现疙瘩，32.95dB
# 3位量化：明显疙瘩，25.72dB
# 2位量化：很多疙瘩，20.22dB
# 1位量化：阶梯状，14.52dB
quantization_bits = 1
quantization_levels = 2 ** quantization_bits
quantization_step = 1 / quantization_levels
quantized_signal = np.round(original_signal / quantization_step) * quantization_step

# 计算信噪比
signal_power = np.sum(original_signal ** 2) / len(original_signal)
noise_power = np.sum((original_signal - quantized_signal) ** 2) / len(original_signal)
snr = 10 * np.log10(signal_power / noise_power)
print('SNR = %.2f dB' % snr)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, original_signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.plot(t, quantized_signal)
plt.title('Quantized Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.plot(t, original_signal - quantized_signal)
plt.title('Quantization Error')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

