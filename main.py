import utils
from strategies import LiquidityReversalSniper

# Initialize strategy with timeframe parameters
strategy = LiquidityReversalSniper(setup_timeframe='15min', trade_timeframe='1min')

# Fetch data
strategy.fetch_data()

# Run strategy analysis
analyzed_setup_df, analyzed_trade_df = strategy.analyze()

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
