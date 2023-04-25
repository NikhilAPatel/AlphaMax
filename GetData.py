import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the list of S&P 500 tickers.
# Note: This is a simplified example. You should update this list with the actual S&P 500 tickers.
sp500_tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'TSLA', 'NVDA', 'JNJ', 'UNH', 'META', 'XOM', 'JPM', 'V', 'PG', 'CVX', 'MA', 'HD', 'PFE', 'ABBV', 'BAC', 'LLY', 'KO', 'AVGO', 'PEP', 'MRK', 'TMO', 'VZ', 'COST', 'ADBE', 'ABT', 'CMCSA', 'DIS', 'ACN', 'CSCO', 'CRM', 'MCD', 'WMT', 'WFC', 'DHR', 'INTC', 'BMY', 'LIN', 'AMD', 'PM', 'COP', 'QCOM', 'NKE', 'TXN', 'NEE', 'T', 'RTX', 'AMGN', 'UNP', 'UPS', 'HON', 'LOW', 'MDT', 'CAT', 'IBM', 'AMT', 'CVS', 'ANTM', 'MS', 'INTU', 'SPGI', 'ORCL', 'GS', 'LMT', 'DE', 'AMAT', 'NOW', 'AXP', 'C', 'SCHW', 'BKNG', 'BLK', 'PLD', 'NFLX', 'CB', 'MO', 'SBUX', 'ADP', 'ADI', 'MDLZ', 'DUK', 'GE', 'MMM', 'CI', 'EOG', 'CCI', 'ZTS', 'TMUS', 'SO', 'MMC', 'MU', 'TGT', 'GILD', 'ISRG', 'BA', 'SYK', 'CME', 'TJX', 'BDX', 'SLB', 'VRTX', 'PGR', 'NOC', 'CSX', 'PNC', 'LRCX', 'USB', 'TFC', 'CL', 'MPC', 'D', 'REGN', 'FCX', 'SHW', 'EL', 'FIS', 'PXD', 'CHTR', 'VLO', 'ATVI', 'NSC', 'HUM', 'FISV', 'EW', 'OXY', 'ITW', 'WM', 'EQIX', 'DG', 'APD', 'KLAC', 'EMR', 'ICE', 'AON', 'ETN', 'GM', 'BSX', 'NEM', 'AEP', 'COF', 'GD', 'FDX', 'PSX', 'SRE', 'F', 'PSA', 'SNPS', 'NXPI', 'DVN', 'MAR', 'LHX', 'CNC', 'ADM', 'HCA', 'MET', 'MCK', 'AIG', 'KMB', 'ROP', 'ADSK', 'MCO', 'EXC', 'WMB', 'CDNS', 'FTNT', 'ECL', 'TRV', 'AZO', 'HPQ', 'ORLY', 'GIS', 'STZ', 'TEL', 'SYY', 'APH', 'IQV', 'WELL', 'O', 'WBD', 'ALL', 'PAYX', 'A', 'HAL', 'XEL', 'CMG', 'HLT', 'MSI', 'CTSH', 'DLR', 'PRU', 'EA', 'MCHP', 'JCI', 'SBAC', 'KMI', 'BK', 'CTAS', 'AJG', 'NUE', 'ILMN', 'GPN', 'PEG', 'SPG', 'MSCI', 'DLTR', 'BKR', 'MNST', 'IFF', 'HES', 'KR', 'BAX', 'YUM', 'PH', 'DD', 'ED', 'AFL', 'TT', 'CMI', 'FAST', 'BIIB', 'PPG', 'RMD', 'PCAR', 'HSY', 'ES', 'IDXX', 'OKE', 'MTD', 'DFS', 'TDG', 'WEC', 'TWTR', 'WBA', 'AMP', 'EBAY', 'MTB', 'DXCM', 'AWK', 'WY', 'ALB', 'ROST', 'KEYS', 'LYB', 'FRC', 'FANG', 'GLW', 'SIVB', 'AVB', 'FITB', 'VRSK', 'CERN', 'APTV', 'RSG', 'CBRE', 'AME', 'ENPH', 'TROW', 'CTRA', 'LUV', 'TSN', 'FE', 'DHI', 'DAL', 'CPRT', 'ULTA', 'AEE', 'MTCH', 'STT', 'ZBH', 'WTW', 'ARE', 'EIX', 'HIG', 'EFX', 'EQR', 'MRO', 'ROK', 'ETR', 'PPL', 'CDW', 'WST', 'STE', 'ODFL', 'ANET', 'BALL', 'DTE', 'NTRS', 'EXR', 'ABC', 'TSCO', 'LH', 'ANSS', 'CF', 'CMS', 'ALGN', 'DRE', 'GWW', 'EXPE', 'RF', 'LEN', 'CNP', 'CTLT', 'HBAN', 'AMCR', 'MAA', 'SWK', 'VMC', 'TTWO', 'MKC', 'CHD', 'GPC', 'IT', 'VTR', 'MLM', 'DOV', 'MPWR', 'URI', 'CFG', 'FLT', 'WAT', 'POOL', 'EVRG', 'HOLX', 'CLX', 'APA', 'SWKS', 'PFG', 'RJF', 'ZBRA', 'TER', 'DRI', 'IP', 'J', 'K', 'PARA', 'DGX', 'STX', 'KEY', 'TDY', 'BR', 'VRSN', 'VFC', 'CINF', 'EPAM', 'EXPD', 'AKAM', 'PKI', 'KMX', 'CE', 'PWR', 'COO', 'TRMB', 'SYF', 'WDC', 'MOH', 'NDAQ', 'BBY', 'ESS', 'GNRC', 'WAB', 'FMC', 'JBHT', 'HRL', 'NVR', 'OMC', 'CAG', 'DPZ', 'CHRW', 'GRMN', 'SJM', 'ATO', 'PKG', 'TXT', 'EMN', 'HST', 'MAS', 'BRO', 'NTAP', 'LKQ', 'NLOK', 'AVY', 'IEX', 'UDR', 'LNT', 'JKHY', 'LDOS', 'INCY', 'IRM', 'AES', 'VTRS', 'TFX', 'MGM', 'LYV', 'BXP', 'CPT', 'UAL', 'WRB', 'XYL', 'TYL', 'SBNY', 'FDS', 'PEAK', 'PAYC', 'L', 'LVS', 'KIM', 'TECH', 'DXC', 'FBHS', 'PTC', 'REG', 'AAL', 'RHI', 'WHR', 'SNA', 'PHM', 'BBWI', 'NLSN', 'CBOE', 'RE', 'HAS', 'BWA', 'ABMD', 'CCL', 'AAP', 'CZR', 'FFIV', 'LUMN', 'CPB', 'LNC', 'TPR', 'QRVO', 'NDSN', 'TAP', 'CTXS', 'AIZ', 'IPG', 'GL', 'CMA', 'ALLE', 'HSIC', 'NRG', 'SEE', 'NI', 'MKTX', 'CRL', 'JNPR', 'BIO', 'RCL', 'UHS', 'PNW', 'PNR', 'ZION', 'FRT', 'DVA', 'NWL', 'IVZ', 'HII', 'BEN', 'WYNN', 'ALK', 'NWSA', 'PENN', 'XRAY', 'MHK', 'AOS', 'NCLH', 'ROL', 'NWS', 'UAA', 'VNO', 'RL', 'DISH', 'IPGP', 'PVH']

# Define the start and end dates for the data you want to retrieve.
start_date = '2021-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Function to fetch the OHLCV data for a given ticker.
def fetch_ohlcv_data(ticker, start, end):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start, end=end)
    data.reset_index(inplace=True)
    data['Ticker'] = ticker
    return data

# Fetch OHLCV data for all S&P 500 stocks and combine into a single DataFrame.
all_data = pd.DataFrame()

for ticker in sp500_tickers:
    print(f"Fetching data for {ticker}...")
    ticker_data = fetch_ohlcv_data(ticker, start_date, end_date)
    all_data = all_data._append(ticker_data, ignore_index=True)

# Save the combined OHLCV data to a CSV file.
all_data.to_csv('sp500_ohlcv_data.csv', index=False)
print("S&P 500 OHLCV data saved to 'sp500_ohlcv_data.csv'")

