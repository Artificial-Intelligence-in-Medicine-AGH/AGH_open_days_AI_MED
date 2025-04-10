import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use("fivethirtyeight")


def figure1(x_train, y_train, x_val, y_val):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].scatter(x_train, y_train, color="blue")
    ax[0].set_title("Dane treningowe")
    ax[0].set_xlabel("X - lata doświadczenia")
    ax[0].set_ylabel("Y - zarobki [tys. zł]" )

    ax[0].set_xlim(-1, 11)

    ax[0].set_yticks(range(0, 51, 5))

    ax[1].scatter(x_val, y_val, color="red")
    ax[1].set_title("Dane walidacyjne")
    ax[1].set_xlabel("X - lata doświadczenia")
    ax[1].set_ylabel("Y - zarobki [tys. zł]" )

    ax[1].set_xlim(-1, 11)

    ax[1].set_yticks(range(0, 51, 5))
 
    return fig, ax 


def figure2(x_train, y_train, b, w, color="k"):
    # Generates evenly spaced x feature
    x_range = np.linspace(0, 10, 100)
    # Computes yhat
    yhat_range = b + w * x_range

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.set_xlabel("X - lata doświadczenia")
    ax.set_ylabel("Y - zarobki [tys. zł]")
    ax.set_yticks(range(-10, 51, 5))

    # Dataset
    ax.scatter(x_train, y_train)
    # Predictions
    ax.plot(x_range, yhat_range, label="Model's predictions", c=color, linestyle="--")

    # Annotations
    ax.annotate("b = {:.4f} a = {:.4f}".format(b[0], w[0]), xy=(2, 5), c=color)
    ax.legend(loc=0)
    fig.tight_layout()

    return fig, ax


def figure3(x_train, y_train, b, w):
    fig, ax = figure2(x_train, y_train, b, w)

    # First data point
    x0, y0 = x_train[0][0], y_train[0][0]
    # First data point
    ax.scatter([x0], [y0], c="r")
    # Vertical line showing error between point and prediction
    ax.set_yticks(range(-10, 51, 5))
    ax.plot([x0, x0], [b[0] + w[0] * x0, y0 - 0.03], c="r", linewidth=2, linestyle="--")
    ax.arrow(
        x0,
        y0 - 0.03,
        0,
        0.03,
        color="r",
        shape="full",
        lw=0,
        length_includes_head=True,
        head_width=0.03,
    )
    ax.arrow(
        x0,
        b[0] + w[0] * x0 + 0.05,
        0,
        -0.03,
        color="r",
        shape="full",
        lw=0,
        length_includes_head=True,
        head_width=0.03,
    )
    # Annotations
    ax.annotate(r"$error_0$", xy=(8, -10))

    fig.tight_layout()

    return fig, ax


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_training(x_train, y_train, epochs, lr):
    # Initialize parameters
    a = np.random.randn(1)
    b = np.random.randn(1)

    # Prepare the figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x_train, y_train, color="blue", label="Training Data")
    (line,) = ax.plot([], [], color="red", linestyle="--", label="Model Prediction")
    ax.set_xlim(x_train.min() - 1, x_train.max() + 1)
    ax.set_ylim(y_train.min() - 5, y_train.max() + 5)
    ax.set_xlabel("X - lata doświadczenia")
    ax.set_ylabel("Y - zarobki [tys. zł]")
    ax.legend()

    # Gradient descent function
    def gradient_descent_step(a, b, x_train, y_train, lr):
        y_pred = a * x_train + b
        error = y_pred - y_train
        b_grad = 2 * error.mean()
        a_grad = 2 * (x_train * error).mean()
        b -= lr * b_grad
        a -= lr * a_grad
        return a, b

    # Update function for animation
    def update(frame):
        nonlocal a, b
        a, b = gradient_descent_step(a, b, x_train, y_train, lr)
        x_range = np.linspace(x_train.min(), x_train.max(), 100)
        y_range = a * x_range + b
        line.set_data(x_range, y_range)
        return (line,)

    # Create the animation
    anim = FuncAnimation(fig, update, frames=epochs, interval=100, blit=False)

    plt.show()
    return anim
