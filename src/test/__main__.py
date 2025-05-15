import matplotlib.pyplot as plt
import matplotlib
import numpy
import torch


def main():
    print(f"matplotlib:{matplotlib.__version__}")
    print(f"numpy:{numpy.__version__}")
    print(f"torch:{torch.__version__}")
    print(f"torch cuda available:{torch.cuda.is_available()}")

    x = numpy.linspace(0, 2 * numpy.pi, 100)
    y = numpy.sin(x)
    print(torch.tensor(y))
