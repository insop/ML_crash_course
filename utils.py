"""Utils
"""

import matplotlib.pyplot as plt # graph
import numpy as np # number handling
import pandas as pd # structured data handling
import sklearn.linear_model
import os

def save_fig(fig_id, tight_layout=True, imabes_path='figures', fig_extension="png", resolution=300):
    path = os.path.join(imabes_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)