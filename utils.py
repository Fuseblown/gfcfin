import pandas as pd

def debug_df(df, *, min_rows=10, max_columns=None, width=1000):
    """
    Display debugging DataFrame with consistent formatting options.
    
    Args:
        df: pandas DataFrame to display
        min_rows: minimum number of rows to display (default: 10, which shows first and last 5 rows)
        max_columns: maximum number of columns (default: None shows all)
        width: display width (default: 1000)
    """
    with pd.option_context(
        "display.min_rows", min_rows,
        "display.max_columns", max_columns,
        "display.width", width
    ):
        print(df)
