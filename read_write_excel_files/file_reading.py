import pandas as pd

# total sales per store and per month
df = pd.read_excel(r"sales_data\new\January.xlsx")
a = df.info()
# print(a)

    # Reading and Writing Excel Files with pandas
# look at the read_excel function and the ExcelFile class
# before looking at the to_excel method and the ExcelWriter class.
# Along the way, I’ll also introduce Python’s with statement

#   The read_excel Function
# sheet_name: Instead of providing a sheet name, you could also provide the index of the sheet(zero-based), e.g.,
#       sheet_name = 0. If you set sheet_name = None, pandas will read the whole workbook and
#       return a dictionary in the form of {"sheetname": df}. To read a selection of sheets, provide a
#       list with sheet names or indices.
# skiprows: This allows you to skip over the indicated number of rows.
# usecols: If the Excel file includes the names of the column headers, provide them in a list to select the
#       columns, e.g., ["Store", "Employees"]. Alternatively, it can also be a list of column indices,
#       e.g., [1, 2], or a string(not a list!) of Excel column names, including ranges, e.g., "B:D,G". You
#       can also provide a function: as an example, to only include the columns that start with Manager,
#       use: usecols = lambda x: x.startswith("Manager").
# nrows: Number of rows you want to read.
# index_col: Indicates which column should be the index, accepts a column name or an index, e.g.,
#       index_col = 0. If you provide a list with multiple columns, a hierarchical index will be created.
# header: If you set header = None, the default integer headers are assigned except if you provide the
#       desired names via the names parameter. If you provide a list of indices, hierarchical column headers
#       will be created.
# names: Provide the desired names of your columns as list.
# na_values: Pandas interprets the following cell values as NaN by default(I introduced NaN in Chapter 5): empty
#       cells,  # NA, NA, null, #N/A, N/A, NaN, n/a, -NaN, 1.#IND, nan, #N/A N/A, -1.#QNAN, -
#       nan, NULL, -1.  # IND, <NA>, 1.#QNAN. If you’d like to add one or more values to that list,
#       provide them via na_values.
# keep_default_na: If you’d like to ignore the default values that pandas interprets as NaN, set
#       keep_default_na = False.
# convert_float:  Excel stores all numbers internally as floats and by default, pandas transforms numbers without
#       meaningful decimals to integers. If you want to change that behavior, set
#       convert_float = False (this may be a bit faster).
# converters: Allows you to provide a function per column to convert its values. For example, to make the text in a
#       certain column uppercase, use the following: converters = {"column_name": lambda x: x.upper()}

df = pd.read_excel("xl/stores.xlsx",
                   sheet_name="2019", skiprows=1, usecols="B:F")
print(df)
b = df.info()
print(b)


def fix_missing(x):
    """fix_missing: fix missing

    Args:
        x (Str): a wrong word (here MISSING)

    Returns:
        bool: False
    """
    return False if x in ["", "MISSING"] else x


df = pd.read_excel("xl/stores.xlsx",
                   sheet_name="2019", skiprows=1, usecols="B:F",
                   converters={"Flagship": fix_missing})
# print(df)
# Out[6]: Store         Employees   Manager     Since       Flagship
#       1 San Francisco 12          Neriah      2019-11-02  False
#       0 New York      10          Sarah       2018-07-20  False
#       2 Chicago       4           Katelin     2020-01-31  False
#       3 Boston        5           Georgiana   2017-04-01  True
#       4 Washington DC 3           Evan        NaT         False
#       5 Las Vegas     11          Paul        2020-01-06  False

# The Flagship column now has Dtype "bool"
df.info()
# To read in all sheets, you would need to provide sheet_name=None.
sheets = pd.read_excel("xl/stores.xlsx", sheet_name=["2019", "2020"], # here 2sheets are taken in
                       skiprows=1, usecols=["Store", "Employees"]) # notice difference with line 35 usecols!!
sheets["2019"].head(2)
# Out[8]:   Store        Employees
#     0     New York        10
#     1     San Francisco   12

# If the source file doesn’t have column headers, set header=None and provide them via
# names. Note that sheet_name also accepts sheet indices:
df = pd.read_excel("xl/stores.xlsx", sheet_name=0,
                   skiprows=2, skipfooter=3,
                   usecols="B:C,F", header=None,
                   names=["Branch", "Employee_Count", "Is_Flagship"])
# df
# Out[9]: Branch        Employee_Count Is_Flagship
#       0 New York      10              False
#       1 San Francisco 12              MISSING
#       2 Chicago       4               NaN

# To handle NaN values, use a combination of na_values and keep_default_na. The
# next sample tells pandas to only interpret cells with the word MISSING as NaN and
# nothing else:
df = pd.read_excel("xl/stores.xlsx", sheet_name="2019",
                   skiprows=1, usecols="B,C,F", skipfooter=2,
                   na_values="MISSING", keep_default_na=False)
# df
# Out[10]: Store            Employees   Flagship
#        0 New York         10             False
#        1 San Francisco    12             NaN
#        2 Chicago          4                       !!!Notice: here no value: only missing can have value NaN
#        3 Boston           5              True

#   the ExcelFile Class
# if you want to read in multiple sheets from a file in the legacy xls format:
# in this case, using ExcelFile will be faster
# as it prevents pandas from reading in the whole file multiple times.
# ExcelFile can be used as a context manager so the file is properly closed again.
# old way to open a file:
# f = open("output.txt", "w") # r, w, a
# f.write("Some text")
# f.close()
# better is: using this context manager
# Objects that support the with statement are called context managers
# this includes the ExcelFile and ExcelWriter objects in this chapter,
# as well as database connection objects
with open("output.txt", "w") as f:
    f.write("Some text")

# Let’s see the ExcelFile class in action:
with pd.ExcelFile("xl/stores.xls") as f:
    df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
    df2 = pd.read_excel(f, "2020", skiprows=1, usecols="B:F", nrows=2)
# df1
# Out[13]: Store Employees Manager Since Flagship
# 0 New York 10 Sarah 2018-07-20 False
# 1 San Francisco 12 Neriah 2019-11-02 MISSING

# ExcelFile also gives you access to the names of all sheets:
stores = pd.ExcelFile("xl/stores.xlsx")
# stores.sheet_names
# Out[14]: ['2019', '2020', '2019-2020']

# Finally, pandas allows you to read Excel files from a URL, similar to how we did it
# with CSV files in Chapter 5. Let’s read it directly from the companion repo:
url = ("https://raw.githubusercontent.com/fzumstein/"
       "python-for-excel/1st-edition/xl/stores.xlsx")
pd.read_excel(url, skiprows=1, usecols="B:E", nrows=2)
# Out[15]: Store Employees Manager Since
# 0 New York 10 Sarah 2018-07-20
# 1 San Francisco 12 Neriah 2019-11-02
