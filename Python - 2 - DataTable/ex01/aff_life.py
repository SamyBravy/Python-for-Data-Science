from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the life expectancy of Italy over the years."""

    csv = load("life_expectancy_years.csv")
    if csv is None:
        return

    try:
        italy = csv[csv["country"] == "Italy"]
        values = italy.iloc[0, 1:].astype(float)
        years = csv.columns[1:].astype(int)

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
