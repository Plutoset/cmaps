import cmaps
import numpy as np
import inspect

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('text', usetex=False)


def list_cmaps():
    attributes = inspect.getmembers(cmaps, lambda _: not (inspect.isroutine(_)))
    colors = [_[0] for _ in attributes if
              not (_[0].startswith('__') and _[0].endswith('__'))]
    return colors


if __name__ == '__main__':
    color = list_cmaps()

    a = np.outer(np.arange(0, 1, 0.001), np.ones(10))
    plt.figure(figsize=(40, 20))
    plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
    ncmaps = len(color)
    ncols = 8
    for i, k in enumerate(color):
        plt.subplot(ncmaps // ncols + 1, ncols * 2, 2 * (i + 1))
        plt.axis('off')
        plt.imshow(a.T, aspect='auto', cmap=getattr(cmaps, k), origin='lower')
        plt.text(0, 0, k, fontsize=10, ha='right', va='bottom')
    plt.savefig('colormaps.png', dpi=300)
    plt.close()
