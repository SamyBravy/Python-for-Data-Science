from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the life expectancy of Italy over the years."""

    csv = load("life_expectancy_years.csv")
    if csv is None:
        return

    try:
        csv.set_index("country", inplace=True)

        values = csv.loc["Italy"].astype(float)
        years = csv.columns.astype(int)

        plt.plot(years, values)
        plt.title("Italy Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::40])
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
