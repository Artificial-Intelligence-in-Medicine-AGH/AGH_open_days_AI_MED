import matplotlib.pyplot as plt
import numpy as np

def show_together(img1, label1, img2, label2, map='gray'): 
    """
    Show two images together with their labels.
    """

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    # Display first image
    ax[0].imshow(img1, cmap=map)
    ax[0].set_title(label1)
    ax[0].axis('off')

    # Display second image
    ax[1].imshow(img2, cmap=map)
    ax[1].set_title(label2)
    ax[1].axis('off')

    plt.show()