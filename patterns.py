import pandas as pd
import numpy as np

def detect_swing_points(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """
    Detect swing highs and lows in price data using a rolling window.
    
    Args:
        df: DataFrame with OHLC data
        window: Number of candles to check (default 3)
    
    Returns:
        DataFrame with new columns 'swing_high' and 'swing_low'
    """
    # Create copy of input DataFrame
    result_df = df.copy()
    
    # Initialize swing columns
    result_df['swing_high'] = False
    result_df['swing_low'] = False
    
    # Get correct column names based on DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        high_col = ('price', 'High')  # Note the capital H
        low_col = ('price', 'Low')    # Note the capital L
    else:
        high_col = 'High'
        low_col = 'Low'
    
    # Detect swing points
    for i in range(1, len(df) - 1):
        # Check if middle point is higher than surrounding points
        if df[high_col].iloc[i] > df[high_col].iloc[i-1] and df[high_col].iloc[i] > df[high_col].iloc[i+1]:
            result_df.iloc[i, result_df.columns.get_loc('swing_high')] = True
            
        # Check if middle point is lower than surrounding points
        if df[low_col].iloc[i] < df[low_col].iloc[i-1] and df[low_col].iloc[i] < df[low_col].iloc[i+1]:
            result_df.iloc[i, result_df.columns.get_loc('swing_low')] = True
            
    return result_df

def get_last_swing_points(df: pd.DataFrame, lookback: int = 10) -> tuple:
    """
    Get the most recent swing high and low points and the price of the swing points.
    
    Args:
        df: DataFrame with swing points marked
        lookback: Number of periods to look back
        
    Returns:
        tuple: (last_swing_high, last_swing_low)
    """
    recent_data = df.tail(lookback)
    
    # Get rows with swing points
    swing_highs = recent_data[recent_data['swing_high']]
    swing_lows = recent_data[recent_data['swing_low']]
    
    # Get last prices
    last_high_price = swing_highs[('price', 'High')].iloc[-1] if len(swing_highs) > 0 else None
    last_low_price = swing_lows[('price', 'Low')].iloc[-1] if len(swing_lows) > 0 else None
    
    return last_high_price, last_low_price