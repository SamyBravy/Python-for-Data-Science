import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file."""

    if not isinstance(path, str):
        print("Error: path must be a string")
        return None
    try:
        df = pd.read_csv(path, on_bad_lines='error')
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: No data")
        return None
    except pd.errors.ParserError:
        print("Error: Parse error")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    print("Loading dataset of dimension", df.shape)
    return df
