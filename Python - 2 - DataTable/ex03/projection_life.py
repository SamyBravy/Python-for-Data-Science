from load_csv import load
import matplotlib.pyplot as plt


def magnitude(series):
    """Convert string representations of numbers with suffixes to floats."""

    def convert(x):
        if isinstance(x, str):
            x = x.replace("B", "e9", regex=False)\
                    .replace("M", "e6", regex=False)\
                    .replace("k", "e3", regex=False)
            return float(x)
        else:
            return float(x)
    return series.apply(convert)


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
    """Plot life expectancy against GDP per capita for the year 1900."""

    life = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if life is None or income is None:
        return

    try:
        income_1900 = magnitude(income["1900"])

        _, ax = plt.subplots()
        ax.set_xscale("log")
        ax.xaxis.set_major_formatter(plt.FuncFormatter(magnitude_formatter))
        ax.scatter(income_1900, life["1900"])
        ax.set_title("1900")
        ax.set_xlabel("Gross Domestic Product")
        ax.set_ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
