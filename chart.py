import pandas as pd
import matplotlib.pyplot as plt


def create_data(numbers):
    series_numbers = pd.Series(numbers)
    counts = series_numbers.value_counts()
    frequencies = counts / len(numbers)

    df = pd.DataFrame({
        'x': frequencies.index,
        'y': frequencies.values
    })
    df = df.sort_values(by='x').reset_index(drop=True)
    return df


def make_chart(numbers):
    df = create_data(numbers)

    # Create the fig and ax objects
    fig, ax = plt.subplots()
    ax.set_facecolor('none')
    fig.set_facecolor('none')

    x_line = [2, 7, 12]
    y_line = [1 / 36, 1 / 6, 1 / 36]
    ax.plot(x_line, y_line, color='red', linewidth=4, zorder=1)

    ax.bar(df.x, df.y, color='orange', width=0.7, zorder=2)

    x_values = list(range(2, 13))
    ax.set_xlim(1, 13)
    ax.set_ylim(0, 7 / 36)
    ax.set_xticks(x_values)
    ax.set_xticklabels(x_values, fontsize=19, color='white')
    ax.tick_params(axis='x', which='both', length=0)
    ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    for spine in ax.spines.values():
        spine.set_visible(False)

    return fig
