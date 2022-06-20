import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO


async def build_graph(k):
    # Creating vectors X and Y
    x = np.linspace(-50, 50, 100)
    y = x - k

    # Write the plot Figure to a file-like bytes object:
    plot_file = BytesIO()

    plt.plot(x, y)

    plt.savefig(plot_file, format='png')
    plot_file.seek(0)
    return plot_file
