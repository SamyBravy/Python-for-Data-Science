from load_csv import load
import matplotlib.pyplot as plt


def magnitude(series):
    """Convert a pandas Series with suffixes to float."""

    series = series.str.replace("B", "e9", regex=False)
    series = series.str.replace("M", "e6", regex=False)
    series = series.str.replace("k", "e3", regex=False)
    return series.astype(float)


def magnitude_formatter(x, pos):
    """Format the y-axis labels with appropriate suffixes."""

    if x >= 1e9:
        return f"{x/1e9:.2f}".rstrip('0').rstrip('.') + 'B'
    elif x >= 1e6:
        return f"{x/1e6:.2f}".rstrip('0').rstrip('.') + 'M'
    elif x >= 1e3:
        return f"{x/1e3:.2f}".rstrip('0').rstrip('.') + 'k'
    else:
        return str(int(x))


def main():
    """Plot the population projections of France and Italy over the years."""

    csv = load("population_total.csv")
    if csv is None:
        return

    try:
        csv.set_index("country", inplace=True)

        csv = csv.loc[:, "1800":"2050"]

        france = magnitude(csv.loc["France"])
        italy = magnitude(csv.loc["Italy"])
        years = csv.columns.astype(int)

        _, ax = plt.subplots()  # Create the canvas and axes (the plot area)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(magnitude_formatter))
        ax.plot(years, france, label="France")
        ax.plot(years, italy, label="Italy")
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.set_xticks(years[::40])
        ax.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
