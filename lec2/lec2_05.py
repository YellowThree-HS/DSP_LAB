# 可以用滤波的方法计算卷积运算

import numpy as np
from scipy.signal import convolve

# 创建一个输入信号
input_signal = np.array([1, 2, 3, 4, 5])

# 创建一个卷积核（滤波器）
filter_kernel = np.array([0.5, 1.0, 0.5])  # 例如，一个简单的平滑滤波器

# 执行卷积运算
output_signal = convolve(input_signal, filter_kernel, mode='full')

# 标准卷积运算
standard_output_signal = np.convolve(input_signal, filter_kernel, mode='full')

# 输出结果
print("Input Signal:", input_signal)
print("Filter Kernel:", filter_kernel)
print("Output Signal (Using SciPy Convolution):", output_signal)
print("Output Signal (Using Standard Convolution):", standard_output_signal)
