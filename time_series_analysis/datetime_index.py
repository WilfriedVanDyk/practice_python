# Other index types, like PeriodIndex,
# are based on time intervals such as hours or months.
# %%
import pandas as pd
import numpy as np
import plotly.express as px
# found module but no type hints or library stubs
pd.options.plotting.backend = "plotly"

daily_index = pd.date_range("2020-02-28", periods=4, freq="D")
# print(daily_index)
#  out = DatetimeIndex(['2020-02-28', '2020-02-29', '2020-03-01',
#                       '2020-03-02'],
#        dtype='datetime64[ns]', freq='D')

weekly_index = pd.date_range("2020-01-01", "2020-01-31", freq="W-SUN")
# print(weekly_index)

weekly_index_1 = pd.DataFrame(data=[21, 15, 33, 34],
                              columns=["visitors"],
                              index=weekly_index)
# print(weekly_index_1)

# msft = pd.read_csv("csv/MSFT.csv")
# msft.info()
# The first one is to run the to_datetime function on that column.
# Make sure to assign the transformed column back to the original DataFrame
# msft.loc[:, "Date"] = pd.to_datetime(msft["Date"])
# print(msft.dtypes)
# msft.info()
# print("\n\n")
# if you want to change it at the source:
# msft = pd.read_csv("../csv/MSFT.csv",
                #    index_col="Date", parse_dates=["Date"])
# print(msft.dtypes)
# msft.info()
# If you would need to change another data type (let’s say you wanted Volume to
# be a float instead of an int), you again have two options: either provide
# dtype={"Volume": float} as argument to the read_csv function
msft = pd.read_csv("../csv/MSFT.csv",
                   index_col="Date",
                   parse_dates=["Date"],
                   dtype={"Volume": float})
# or apply the astype method as follows:
# msft.loc[:, "Volume"] = msft["Volume"].astype("float")
# msft["Volume"].dtype
# Out[11]: dtype('float64')


msft = msft.sort_index()  # PREFFERABLE!!!

a = msft.index.date  # to access only parts of a DatetimeIndex,
# print(a)
# Instead of date, you can also use parts of a date like year, month, day, etc.
# To access the same functionality on a regular column with data type datetime,
# you will have to use the dt attribute, e.g., df["column_name"].dt.date.


#       Filtering a DatetimeIndex
msft.loc["2019", "Adj Close"]

msft.loc["2019-06":"2020-05", "Adj Close"].plot()

# nasdaq closes at 4: 00 p.m. To add this additional information to the DataFrame’s
# index, first add the closing hour to the date via DateOffset, then attach the correct
# time zone to the timestamps via tz_localize. Since the closing hour is only applicable
# to the close price, let’s create a new DataFrame with it
# print(msft.head(2))

# Add the time information to the date
msft_close = msft.loc[:, ["Adj Close"]].copy()
msft_close.index = msft_close.index + pd.DateOffset(hours=16)
msft_close.head(2)

#                     Adj Close
# Date
# 1986-03-13 16:00:00 0.062205
# 1986-03-14 16:00:00 0.064427

# Make the timestamps time-zone-aware
msft_close = msft_close.tz_localize("America/New_York")
msft_close.head(2)

# UTC stands for Coordinated Universal Time and is the successor of
# Greenwich Mean Time(GMT). Note how the closing hours change in UTC depending
# on whether daylight saving time(DST) is in effect or not in New York:
msft_close = msft_close.tz_convert("UTC")
a = msft_close.loc["2020-01-02", "Adj Close"]  # 21:00 without DST
# Out[18]: Date
# 2020-01-02 21: 00: 00+00: 00 159.737595
# Name: Adj Close, dtype: float64

b = msft_close.loc["2020-05-01", "Adj Close"]  # 20:00 with DST
# Out[19]: Date
# 2020-05-01 20: 00: 00+00: 00 174.085175
# Name: Adj Close, dtype: float64


#       Common Time Series Manipulations
# Excel uses LN to denote the natural logarithm and LOG for the logarithm
# with base 10. 
# Python’s math module and NumPy, however, use log for the natural logarithm 
# and log10 for the logarithm with base 10
# print(msft_close.head())
# print(msft_close.shift(1).head())

returns = np.log(msft_close / msft_close.shift(1))
returns = returns.rename(columns={"Adj Close": "returns"})
d = returns.head()
# print(d)
# Out[22]: returns
# Date
# 1986-03-13 21: 00: 00+00: 00 NaN
# 1986-03-14 21: 00: 00+00: 00 0.035097
# 1986-03-17 21: 00: 00+00: 00 0.017082
# 1986-03-18 21: 00: 00+00: 00 - 0.025749
# 1986-03-19 21: 00: 00+00: 00 - 0.017547

# Plot a histogram with the daily log returns
returns.plot.hist()

#       simple returns: simple returns instead, 
# use pandas’ built-in pct_change method. By default, it 
# calculates the percentage change from the previous row,
# which is also the definition of simple returns
simple_rets = msft_close.pct_change()
simple_rets = simple_rets.rename(columns={"Adj Close": "simple rets"})
simple_rets.head()
# Out[24]: simple rets
# Date
# 1986-03-13 21:00:00+00:00 NaN
# 1986-03-14 21:00:00+00:00 0.035721
# 1986-03-17 21:00:00+00:00 0.017229
# 1986-03-18 21:00:00+00:00 -0.025421
# 1986-03-19 21:00:00+00:00 -0.017394


#       Rebasing and Correlation
parts = []  # List to collect individual DataFrames
for ticker in ["AAPL", "AMZN", "GOOGL", "MSFT"]:
    # "usecols" allows us to only read in the Date and Adj Close
    adj_close = pd.read_csv(f"../csv/{ticker}.csv",
                            index_col="Date", parse_dates=["Date"],
                            usecols=["Date", "Adj Close"])
    # Rename the column into the ticker symbol
    adj_close = adj_close.rename(columns={"Adj Close": ticker})
    # Append the stock's DataFrame to the parts list
    parts.append(adj_close)
# Combine the 4 DataFrames into a single DataFrame
adj_close = pd.concat(parts, axis=1)
print(adj_close)
# Dropping all rows that contain missing values
# will make sure that all stocks have the same amount of data points:
adj_close = adj_close.dropna()
adj_close.info()

# Let’s now rebase the prices so that all time series start at 100. This allows us to compare
# their relative performance in a chart; see Figure 6-4. To rebase a time series,
# divide every value by its starting value and multiply by 100, the new base. 
# If you did this in Excel, you would typically write a formula with a combination of absolute and
# relative cell references, then copy the formula for every row and every time series.
# In pandas, thanks to vectorization and broadcasting, you are dealing with a single
# formula:
# Use a sample from June 2019 - May 2020
adj_close_sample = adj_close.loc["2019-06":"2020-05", :]
rebased_prices = adj_close_sample / adj_close_sample.iloc[0, :] * 100
rebased_prices.head(2)
# Out[28]: AAPL AMZN GOOGL MSFT
# Date
# 2019-06-03 100.000000 100.000000 100.00000 100.000000
# 2019-06-04 103.658406 102.178197 101.51626 102.770372
rebased_prices.plot()


#   correlation heat map
# Correlation of daily log returns
returns = np.log(adj_close / adj_close.shift(1))
returns.corr()
# Out[30]: AAPL AMZN GOOGL MSFT
# AAPL 1.000000 0.424910 0.503497 0.486065
# AMZN 0.424910 1.000000 0.486690 0.485725
# GOOGL 0.503497 0.486690 1.000000 0.525645
# MSFT 0.486065 0.485725 0.525645 1.000000
# import plotly.express as px
fig = px.imshow(returns.corr(),
                        x=adj_close.columns,
                        y=adj_close.columns,
                        color_continuous_scale=list(
                            reversed(px.colors.sequential.RdBu)),
                        zmin=-1, zmax=1)
fig.show()

#       Resampling
# Upsampling means that the time series is converted into one with a higher frequency,
# downsampling means # that it is converted into one with a lower frequency.
# resample method:
# accepts a frequency string like
# M for end-of-calendar-month
# BM for end-of-business-month
# last: to take the last element of the month
# method that works on groupby, like sum or last or mean.
# There is also ohlc, which conveniently returns the open, high, low, and close values over that period.
# This may serve as the source to create the typical candlestick charts that are often used with stock prices
end_of_month = adj_close.resample("M").last() # M = end of the month
end_of_month.head()

# upsampling:
# asfreq: you are telling pandas not to apply any transformation 
# and hence you will see most of the values showing NaN. 
# If you wanted to forward-fill the last known value instead, use
# the ffill method: 
# D = daily
end_of_month.resample("D").asfreq().head()  # No transformation
# Out[34]: AAPL AMZN GOOGL MSFT
# Date
# 2004-08-31 2.132708 38.139999 51.236237 17.67363
# 2004-09-01 NaN NaN NaN NaN
# 2004-09-02 NaN NaN NaN NaN
# 2004-09-03 NaN NaN NaN NaN
# 2004-09-04 NaN NaN NaN NaN
end_of_month.resample("W-FRI").ffill().head()  # Forward fill
# W-FRI = weekly frequency (Fridays)
# Out[35]: AAPL AMZN GOOGL MSFT
# Date
# 2004-09-03 2.132708 38.139999 51.236237 17.673630
# 2004-09-10 2.132708 38.139999 51.236237 17.673630
# 2004-09-17 2.132708 38.139999 51.236237 17.673630
# 2004-09-24 2.132708 38.139999 51.236237 17.673630
# 2004-10-01 2.396127 40.860001 64.864868 17.900215

#   Rolling Windows
# Downsampling data is one way of smoothing a time series. Calculating statistics over
# a rolling window is another way, as we will see next.(fe rolling AVG over 25 days)
# DataFrames have a rolling method, 
# which accepts the number of observations as argument

# Plot the moving average for MSFT with data from 2019
msft19 = msft.loc["2019", ["Adj Close"]].copy()
# Add the 25 day moving average as a new column to the DataFrame
# Instead of mean, you can use many other statistical measures including count, sum,
# median, min, max, std(standard deviation), or var(variance)
msft19.loc[:, "25day average"] = msft19["Adj Close"].rolling(25).mean()
msft19.plot()

# %%
