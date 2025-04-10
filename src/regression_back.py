import matplotlib.pyplot as plt

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


    plt.show()  

