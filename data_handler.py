from datetime import datetime
from typing import Optional, Union
import yfinance as yf
import pandas as pd

def fetch_data(
        source: str,
        symbol: str,
        period: str = 'max',
        interval: str = '1d',
        start: Optional[Union[str, datetime]] = None,
        end: Optional[Union[str, datetime]] = None,
        data_dir: Optional[str] = None,
        data_file: Optional[str] = None,
        with_volume: bool = True
) -> pd.DataFrame:
    """
    Fetch historical data for a given symbol from a given source.

    Parameters:
    - source (str): The data source (e.g. 'yfinance' or 'csv').
    - symbol (str): The symbol of the asset.
    - period (str): (Optional) The period range to fetch data from (e.g. 'max', 'ytd', '10y', '5y', '2y', '1y', '6mo', '3mo', '1mo', '5d', '1d').
    - interval (str): (Optional) The data interval to fetch within the period range (e.g. '3mo', '1mo', '1wk', '5d', '1d', '1h', '90m', '60m', '30m', '15m', '5m', '2m', '1m'). You must use 'min' instead of 'm' for minute-based intervals when fetching from any local or remote DataBento source.
    - start (datetime): (Optional) The start date to fetch data from (e.g. 'YYYY-MM-DD').
    - end (datetime): (Optional) The end date to fetch data from (e.g. 'YYYY-MM-DD').
    - data_dir (str): (Optional) The directory where the local source data file is located.
    - data_file (str): (Optional) The local source data file name.
    - with_volume (bool): (Optional) Default is True. Whether to include volume data in the fetched data. This currently only applies to data that has been resampled/aggregated, otherwise it is ignored for individual trade data.

    Returns:
    - pd.DataFrame: The historical data for the given symbol from the given source.

    Examples:
    >>> fetch_data('yfinance', 'AAPL', period='1y', interval='1d')
    >>> fetch_data('csv', 'NQZ3', data_dir='data', data_file='NQZ3_DataBento_trades_Dec_2023.csv', interval='1min', with_volume=True)

    TO-DO:
    - Add support for other data sources such as the DataBento API.
    - Save fetched data locally (csv, database, etc.).
    - Store all raw data in a database for easy access, retrieval, and cost reduction.
    """
    if source == 'yfinance':
        if start is not None and end is not None:
            data = yf.download(symbol, interval=interval, start=start, end=end)
        else:
            data = yf.download(symbol, period=period, interval=interval)

    elif source == 'csv':
        data = pd.read_csv(f'{data_dir}/{data_file}')
        data['ts_recv'] = pd.to_datetime(data['ts_recv'], format='ISO8601', dayfirst=False)
        data['ts_recv'] = data['ts_recv'].dt.tz_convert('US/Eastern')
        data.set_index('ts_recv', inplace=True)

        if interval is not None:
            if with_volume is True:
                data = data.resample(interval).agg({'price': 'ohlc', 'size': 'sum'})

            else:
                data = data.resample(interval).agg({'price': 'ohlc'})
            
            data.reset_index(inplace=True)
            data = data.rename(columns={'ts_recv': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'size': 'Volume'})
            data.set_index('Date', inplace=True)

    else:
        raise ValueError(f"Data source '{source}' is not currently supported.")
    
    return data
