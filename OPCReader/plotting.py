import matplotlib.pyplot as plt


def plot_all(data):
    """Plots all raw bin count data"""
    plt.figure()
    for x in range(16):
        plt.plot(data[data.columns[1+x]])

    plt.show()


def plot_all_rolling(data, window=15):
    """Plots all bin data with a rolling average"""
    plt.figure()
    for x in range(16):

        plt.plot(data['time'].dt.seconds/60, data[data.columns[1+x]].rolling(window=window).mean())
        plt.legend()

    plt.ylabel("Count")
    plt.xlabel("Time (min)")
    plt.show()


def hist(data, start=0, stop=None):
    """"Plots a histogram of particle count bins"""
    plt.figure()
    if stop is None:
        stop = len(data)
    for x in range(16):
        plt.bar(x, data[data.columns[1 + x]][start:stop].sum())

    plt.xlabel("Bins")
    plt.ylabel("Counts")
    plt.show()

