import matplotlib.pyplot as plt
import matplotlib
import numpy


def main():
    print(f"matplotlib:{matplotlib.__version__}")
    print(f"numpy:{numpy.__version__}")

    x = numpy.linspace(0, 2 * numpy.pi, 100)
    y = numpy.sin(x)
    plt.plot(x, y)
    plt.savefig("sine_wave.png")  # 将图形保存到文件
