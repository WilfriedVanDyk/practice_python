"""            pd: import           df(dataframe): export
CSV files      pd.read_csv          df.to_csv
JSON           pd.read_json         df.to_json
HTML           pd.read_html         df.to_html
Clipboard      pd.read_clipboard    df.to_clipboard
Excel files    pd.read_excel        df.to_excel => PART 3
SQL Databases  pd.read_sql          df.to_sql   => chapter 11
"""
import pandas as pd
#   Exporting CSV Files
data1 = [["Mark", 55, "Italy", 4.5, "Europe"],
         ["John", 33, "USA", 6.7, "America"],
         ["Tim", 41, "USA", 3.9, "America"],
         ["Jenny", 12, "Germany", 9.0, "Europe"]]
df = pd.DataFrame(data=data1,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
df.index.name = "user_id"
df.to_csv(r"csv\course_participants.csv")

#   Importing CSV Files
msft = pd.read_csv("csv/MSFT.csv") # sep: separator or delimiter the CSV uses in case it isn’t the default comma
msft.info()  # to get a summary of the df
# "head" and "tail" methods: to see the first and last few rows of the DataFrame. number of rows is default 5
# "describe" method: to get some basic statistics

# selecting a few columns because of space issues (You can also just run: msft.head() )
a = msft.loc[:, ["Date", "Adj Close", "Volume"]].head()
# print(a)
b = msft.loc[:, ["Date", "Adj Close", "Volume"]].tail(2)
# print(b)
msft.loc[:, ["Adj Close", "Volume"]].describe()

"""
df.info()     Provides number of data points, index type, dtype, and memory usage.
df.describe() Provides basic statistics including count, mean, std, min, max, and percentiles.
df.head(n=5)  Returns the first n rows of the DataFrame.
df.tail(n=5)  Returns the last n rows of the DataFrame.
df.dtypes     Returns the dtype of each column.
"""

# read a CSV file directly from the companion repo
# The line break in the URL is only to make it fit on the page
url = ("https://raw.githubusercontent.com/fzumstein/"
       "python-for-excel/1st-edition/csv/MSFT.csv")
msft = pd.read_csv(url)
c = msft.loc[:, ["Date", "Adj Close", "Volume"]].head(2)
print(c, "\nvoila")
