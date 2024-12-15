import data_handler as dh
import utils
from strategies import LiquidityReversalSniper

# Initialize strategy
strategy = LiquidityReversalSniper()

# Setup parameters
setup_timeframe = '15min'  # For minute-based intervals use 'min' instead of 'm'.
trade_timeframe = '1min'  # For minute-based intervals use 'min' instead of 'm'.

# Load and analyze data
setup_df = dh.fetch_data('url', 'NQZ3', 
                        data_dir='data', 
                        data_file='https://drive.google.com/file/d/1WE4YTNmtWPSvEsYBDD_V2lUYEE_J_sMJ/view', 
                        interval=setup_timeframe, 
                        with_volume=True)

trade_df = dh.fetch_data('url', 'NQZ3', 
                        data_dir='data', 
                        data_file='https://drive.google.com/file/d/1WE4YTNmtWPSvEsYBDD_V2lUYEE_J_sMJ/view', 
                        interval=trade_timeframe, 
                        with_volume=True)

# Run strategy analysis
analyzed_setup_df, analyzed_trade_df = strategy.analyze(setup_df, trade_df)

# Get signals
signals = strategy.get_signals()

# Display results
print("\nSetup Timeframe Analysis:")
utils.debug_df(analyzed_setup_df[['price', 'swing_high', 'swing_low']], min_rows=20)
print(f"\nStrategy Signals:")
print(f"Last swing high: {signals['last_swing_high']}")
print(f"Last swing low: {signals['last_swing_low']}")
print("\nTrade Timeframe Data:")
utils.debug_df(analyzed_trade_df)