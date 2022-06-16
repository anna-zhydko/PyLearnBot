import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO


async def build_graph():
    # Creating vectors X and Y
    x = np.linspace(-2, 2, 100)
    y = x ** 2

    # Write the plot Figure to a file-like bytes object:
    plot_file = BytesIO()

    plt.plot(x, y, linestyle='--', color='k', lw=3, scalex=False, scaley=False)

    plt.savefig(plot_file, format='png')
    plot_file.seek(0)
    return plot_file
