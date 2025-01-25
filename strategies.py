from abc import ABC, abstractmethod
import pandas as pd
import patterns as pt
import data_handler as dh

class Strategy(ABC):
    """Base class for all trading strategies"""
    def __init__(self, name: str):
        self.name = name
        self.positions = []
        
    @abstractmethod
    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        """Analyze price data and generate signals"""
        pass
    
    @abstractmethod
    def get_signals(self) -> dict:
        """Get current trading signals"""
        pass

class LiquidityReversalSniper(Strategy):
    def __init__(self, setup_timeframe='15min', trade_timeframe='1min'):
        super().__init__("Liquidity Reversal Sniper")
        self.setup_timeframe = setup_timeframe
        self.trade_timeframe = trade_timeframe
        self.last_high = None
        self.last_low = None
        self.setup_df = None
        self.trade_df = None
        
    def fetch_data(self, symbol='NQZ3', data_dir='data', 
                  data_file='https://drive.google.com/file/d/1WE4YTNmtWPSvEsYBDD_V2lUYEE_J_sMJ/view'):
        """Fetch and prepare data for analysis"""
        
        self.setup_df = dh.fetch_data('url', symbol,
                                    data_dir=data_dir,
                                    data_file=data_file,
                                    interval=self.setup_timeframe,
                                    with_volume=True)
        
        self.trade_df = dh.fetch_data('url', symbol,
                                    data_dir=data_dir, 
                                    data_file=data_file,
                                    interval=self.trade_timeframe,
                                    with_volume=True)
        
    def analyze(self, setup_df=None, trade_df=None):
        """Analyze price data to find swing points and potential reversal zones."""
        # Use provided dataframes or fetch if needed
        if setup_df is None:
            setup_df = self.setup_df
        if trade_df is None:
            trade_df = self.trade_df
            
        # Verify we have data
        if setup_df is None or trade_df is None:
            raise ValueError("No data available. Call fetch_data() first or provide DataFrames.")
            
        # Detect swing points
        swing_df = pt.detect_swing_points(setup_df)

        # Add swing break columns
        swing_df['swing_high_broken'] = False
        swing_df['swing_low_broken'] = False
        
        # Track swing point breaks using source data
        if isinstance(trade_df.columns, pd.MultiIndex):
            price_col = ('price', 'High')  # Use High for testing breaks
            low_col = ('price', 'Low')     # Use Low for testing breaks
        else:
            price_col = 'High'
            low_col = 'Low'
            
        # Get swing points that need monitoring
        swing_highs = swing_df[swing_df['swing_high']].copy()
        swing_lows = swing_df[swing_df['swing_low']].copy()
        
        # Check each price point against swing levels
        for idx, row in trade_df.iterrows():
            # Check swing high breaks
            if not swing_highs.empty:
                # Align indexes and use loc for boolean indexing
                unbroken_mask = ~swing_df.loc[swing_highs.index, 'swing_high_broken']
                unbroken_highs = swing_highs.loc[unbroken_mask.index[unbroken_mask]]
                
                if not unbroken_highs.empty:
                    broken_highs = unbroken_highs[unbroken_highs[price_col] < row[price_col]]
                    if not broken_highs.empty:
                        swing_df.loc[broken_highs.index, 'swing_high_broken'] = True
                    
            # Check swing low breaks    
            if not swing_lows.empty:
                # Align indexes and use loc for boolean indexing
                unbroken_mask = ~swing_df.loc[swing_lows.index, 'swing_low_broken']
                unbroken_lows = swing_lows.loc[unbroken_mask.index[unbroken_mask]]
                
                if not unbroken_lows.empty:
                    broken_lows = unbroken_lows[unbroken_lows[low_col] > row[low_col]]
                    if not broken_lows.empty:
                        swing_df.loc[broken_lows.index, 'swing_low_broken'] = True


        # Get latest swing points
        self.last_high, self.last_low = pt.get_last_swing_points(swing_df)

        # Detect fair value gaps
        trade_df = pt.detect_fair_value_gaps(trade_df)

        # Get the latest fair value gaps on the trade timeframe
        self.last_bullish_fvg, self.last_bearish_fvg = pt.get_last_fair_value_gaps(trade_df)
        
        return swing_df, trade_df
    
    def get_signals(self) -> dict:
        """
        Get current trading signals based on analysis.
        
        Returns:
            dict with signal information

        NOTES:
        - We will likely use a DataFrame instead of a dictionary to track all swing highs and lows, and then can use the last row to track the most recent valid values as needed throughout the strategy.
        """
        return {
            'last_swing_high': self.last_high,
            'last_swing_low': self.last_low
        }
