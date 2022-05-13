"""
Other index types, like PeriodIndex,
are based on time intervals such as hours or months.
"""
# %%
import pandas as pd
import numpy as np
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

# msft = pd.read_csv("../csv/MSFT.csv")
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

# Add the time information to the date
msft_close = msft.loc[:, ["Adj Close"]].copy()
msft_close.index = msft_close.index + pd.DateOffset(hours=16)
msft_close.head(2)

# Make the timestamps time-zone-aware
msft_close = msft_close.tz_localize("America/New_York")
msft_close.head(2)
