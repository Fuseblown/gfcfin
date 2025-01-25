import pandas as pd

def detect_swing_points(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Detect swing highs and lows in price data using a rolling window. Default is 3 data points (OHLC candlesticks)"""
    # Create copy of input DataFrame
    result_df = df.copy()
    
    # Initialize swing columns
    result_df['swing_high'] = False
    result_df['swing_low'] = False
    result_df['swing_high_broken'] = False
    result_df['swing_low_broken'] = False
    result_df['swing_invalidated'] = False
    
    # Get correct column names based on DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        # For MultiIndex columns from resampled data
        high_col = ('price', 'High')
        low_col = ('price', 'Low')
    else:
        # For standard columns
        high_col = 'High'
        low_col = 'Low'

    # Initialize tracking variables
    last_valid_high_idx = None
    last_valid_low_idx = None
   
    # Detect swing points
    for i in range(1, len(df) - 1):
        current_idx = df.index[i]
        
        # Check for swing high
        if df[high_col].iloc[i] > df[high_col].iloc[i-1] and df[high_col].iloc[i] > df[high_col].iloc[i+1]:
            result_df.iloc[i, result_df.columns.get_loc('swing_high')] = True
            
            # Check if invalidates previous unbroken swing high
            if last_valid_high_idx is not None:
                prev_idx = df.index.get_loc(last_valid_high_idx)
                if result_df.iloc[prev_idx]['swing_high_broken'].item() == False:
                    result_df.iloc[prev_idx, result_df.columns.get_loc('swing_invalidated')] = True
            
            last_valid_high_idx = current_idx
            
        # Check for swing low    
        if df[low_col].iloc[i] < df[low_col].iloc[i-1] and df[low_col].iloc[i] < df[low_col].iloc[i+1]:
            result_df.iloc[i, result_df.columns.get_loc('swing_low')] = True
            
            # Check if invalidates previous unbroken swing low
            if last_valid_low_idx is not None:
                prev_idx = df.index.get_loc(last_valid_low_idx)
                if result_df.iloc[prev_idx]['swing_low_broken'].item() == False:
                    result_df.iloc[prev_idx, result_df.columns.get_loc('swing_invalidated')] = True
            
            last_valid_low_idx = current_idx
            
    return result_df

def get_last_swing_points(df: pd.DataFrame) -> tuple[float, float]:
    """
    Get the most recent swing high and low points.
    
    Args:
        df: DataFrame with swing_high and swing_low columns
        
    Returns:
        tuple: (last_swing_high_price, last_swing_low_price)
    """
    # Get price column based on DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        price_high = ('price', 'High')
        price_low = ('price', 'Low')
    else:
        price_high = 'High'
        price_low = 'Low'
        
    # Find last swing high
    last_swing_high_mask = df['swing_high']
    last_swing_high = df[last_swing_high_mask][price_high].iloc[-1] if any(last_swing_high_mask) else None
    
    # Find last swing low
    last_swing_low_mask = df['swing_low']
    last_swing_low = df[last_swing_low_mask][price_low].iloc[-1] if any(last_swing_low_mask) else None

    return last_swing_high, last_swing_low

def detect_fair_value_gaps(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Detect all fair value gaps in price data using a rolling window."""
    # Create copy of input DataFrame
    result_df = df.copy()
    
    # Initialize fair value gap columns
    result_df['bullish_fvg'] = False
    result_df['bearish_fvg'] = False
    
    # Get correct column names based on DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        # For MultiIndex columns from resampled data
        high_col = ('price', 'High')
        low_col = ('price', 'Low')
    else:
        # For standard columns
        high_col = 'High'
        low_col = 'Low'
   
    # Detect swing points
    for i in range(1, len(df) - 1):
        try:
            # Check if low of the previous (1st) candle is higher than high of the next (3rd) candle
            if df[low_col].iloc[i-1] > df[high_col].iloc[i+1]:
                result_df.iloc[i+1, result_df.columns.get_loc('bearish_fvg')] = True
                
            # Check if high of the previous (1st) candle is lower than low of the next (3rd) candle    
            if df[high_col].iloc[i-1] < df[low_col].iloc[i+1]:
                result_df.iloc[i+1, result_df.columns.get_loc('bullish_fvg')] = True

        except KeyError as e:
            print(f"Error accessing columns: {e}")
            print(f"Available columns: {df.columns}")
            raise
            
    return result_df

def get_last_fair_value_gaps(df: pd.DataFrame) -> tuple[float, float]:
    """
    Get the most recent bullish and bearish fair value gaps.
    
    Args:
        df: DataFrame with bullish_fvg and bearish_fvg columns
        
    Returns:
        tuple: (last_bullish_fvg, last_bearish_fvg)

    NOTES: The True and False values in the columns are shifted by 1 candle to the right (they are listed in the same row as the third data point in the pattern) to avoid lookahead bias.
    """
    # Get price column based on DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        price_high = ('price', 'High')
    else:
        price_high = 'High'
        
    # Find last swing high
    last_bullish_fvg_mask = df['bullish_fvg']
    last_bullish_fvg = df[last_bullish_fvg_mask][price_high].iloc[-1] if any(last_bullish_fvg_mask) else None
    
    # Find last swing low
    last_bearish_fvg_mask = df['bearish_fvg']
    last_bearish_fvg = df[last_bearish_fvg_mask][price_high].iloc[-1] if any(last_bearish_fvg_mask) else None

    return last_bullish_fvg, last_bearish_fvg
