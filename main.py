import pandas as pd
import data_handler as dh
import patterns as pt
from utils import debug_df

setup_timeframe = '15min' # For minute-based intervals use 'min' instead of 'm'.
trade_timeframe = '1min' # For minute-based intervals use 'min' instead of 'm'.

# Load and preprocess DataBento CSV data for NQZ3 for the setup_timeframe.
setup_df = dh.fetch_data('csv', 'NQZ3', data_dir='data', data_file='NQZ3_DataBento_trades_Dec_2023.csv', interval=setup_timeframe)

setup_df = pt.detect_swing_points(setup_df)
last_high_price, last_low_price = pt.get_last_swing_points(setup_df)

debug_df(setup_df[['price', 'swing_high', 'swing_low']], min_rows=20)

print(f"Most recent swing high price: {last_high_price}")
print(f"Most recent swing low price: {last_low_price}")
