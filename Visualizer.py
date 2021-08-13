import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections

if __name__ == '__main__':
    cpu = collections.deque(np.zeros(10))
    ram = collections.deque(np.zeros(10))
    print("CPU: {}".format(cpu))
    print("Memory: {}".format(ram))