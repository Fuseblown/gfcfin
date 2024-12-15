from abc import ABC, abstractmethod
import pandas as pd
import patterns as pt

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
    """Strategy that trades reversals at liquidity levels marked by swing points"""
    
    def __init__(self):
        super().__init__("Liquidity Reversal Sniper")
        self.last_high = None
        self.last_low = None
        
    def analyze(self, setup_df: pd.DataFrame, trade_df: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze price data to find swing points and potential reversal zones.
        
        Args:
            df: DataFrame with OHLC data
        
        Returns:
            DataFrame with analysis results
        """
        # Detect swing points
        swing_df = pt.detect_swing_points(setup_df)
        
        # Get latest swing points
        self.last_high, self.last_low = pt.get_last_swing_points(swing_df)
        
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
