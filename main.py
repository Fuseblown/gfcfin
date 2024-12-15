import pandas as pd
import data_handler as dh
import patterns as pt
from utils import debug_df

setup_timeframe = '15min' # For minute-based intervals use 'min' instead of 'm'.
trade_timeframe = '1min' # For minute-based intervals use 'min' instead of 'm'.

# Load and preprocess data for the setup_timeframe.
# ---------------------------------------------------------------
# By default, this fetches the sample granular data from the Google Drive URL mentioned in README.md.
# If it doesn't already exist at './{data_dir}/NQZ3_DataBento_trades_Dec_2023.csv', it will be downloaded and saved to that location. If the above file does already exist in the 'data_dir', it will be loaded from the local source instead.
# The data is then be resampled to the setup_timeframe and the swing points detected.
setup_df = dh.fetch_data('url', 'NQZ3', data_dir='data', data_file='https://drive.google.com/file/d/1WE4YTNmtWPSvEsYBDD_V2lUYEE_J_sMJ/view', interval=setup_timeframe, with_volume=True)

setup_df = pt.detect_swing_points(setup_df)
last_high_price, last_low_price = pt.get_last_swing_points(setup_df)

debug_df(setup_df[['price', 'swing_high', 'swing_low']], min_rows=20)

print(f"Most recent swing high price: {last_high_price}")
print(f"Most recent swing low price: {last_low_price}")
