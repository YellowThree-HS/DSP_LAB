# DSP_LAB

## lec2_01.py
- 通过能量检测音频文件的起始和结束位置

## lec2_02.py
- 在不同采样率下生成2s、440Hz的正弦波，并播放

## lec2_03.py
- 验证信道+1，信噪比+6%

## lec2_04.py
- 对一个正弦信号进行上抽样和下抽样，观察时域和频域的变化

## lec2_05.py
- 可以用滤波的方法计算卷积运算

## lec2_ex2.py

**要求:**
1. 读入一段语音，将采样率变为8kHz，将时域信号变为: y(n) = (-1)^n * x(n)，听一下两个信号并分析比较它们在幅度谱上的区别。
2. 如果我们拿到 y(n) 的傅里叶变换 Y(ejω)，如何还原 x(n)? 请用 Python 实现

**结果:**
- 降采样后的信号很像原始信号，但是音调变了，变成了低音调。
- 时域反转后的信号在幅度上和原始信号完全相同，但是相位相反，音调变了，变成了低音调。
- 使用逆离散傅立叶变换 (IDFT) 恢复原始信号，勉强能听出原来的音调，但是如果使用上抽想要恢复采样率时，幅度变小，且声音变成了青蛙叫，暂未找到原因。
