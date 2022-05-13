import pandas as pd
import practice_pandas_selecting as pps
df2 = pps.df.copy()
# print(df2)
u = df2.loc[1000, "name"] = "JOHN"
# print(df2)
df2.loc[[1000, 1001], "score"] = [3, 4]


# Setting data by boolean indexing
tf = (df2["age"] < 20) | (df2["country"] == "USA")
df2.loc[tf, "name"] = "xxx"

rainfall2 = pps.rainfall.copy()
rainfall2[rainfall2 < 400] = 0
# print(rainfall2)


# Setting data by replacing values
df2.replace("USA", "U.S.")  # to replace all values in the dataframe
df2.replace({"country": {"USA": "U.S."}})  # to replace only the values in the country column (dictionairy)

# Setting data by adding a new column
df2.loc[:, "discount"] = 0
df2.loc[:, "price"] = [49.9, 49.9, 99.9, 99.9]
# print(df2)
df3 = pps.df.copy()  # Let's start with a fresh copy
df3.loc[:, "birth year"] = 2021 - df2["age"]
df3 = df3.reset_index().set_index("name")
df3 = df3.sort_index()
# df3 = df3.sort_values("score")
# print(df3)


# Missing data
df4 = pps.df.copy()  # Let's start with a fresh copy
df4.loc[1000, "score"] = None
df4.loc[1003, :] = None  # this is different from NaN
df4.dropna()  # drops rows that contain empty values
df4.dropna(how="all")  # drops row when all numbers are empty
df4.isna()  # returns boolean table: true when Nan or NOne
df4.fillna({"score": df4["score"].mean()})

# Duplicate data
df5 = pps.df.copy()
# print(df5)
df5.drop_duplicates(["country", "continent"])  # Optionally: subset of the columns as argument
#  By default, this will leave the first occurrence
df5["country"].is_unique
# Out[50]: False
df5["country"].unique()
# Out[51]: array(['Italy', 'USA', 'Germany'], dtype=object)
# By default, it marks only duplicates as True, i.e. WITHOUT THE FIRST OCCURENCE!!! 1000 is false(is the first duplicate)
df5["country"].duplicated()
# Out[52]: user_id
# 1001 False
# 1000 False
# 1002 True
# 1003 False
# Name: country, dtype: bool

# To get all rows where "country" is duplicated, use "keep=False"
a = df5.loc[df5["country"].duplicated(keep=False), :]
# print(a)


# Arithmetic Operations
df6 = pps.rainfall.copy()
df6 + 100
more_rainfall = pd.DataFrame(data=[[100, 200], [300, 400]],
                             columns=["City 1", "City 4"],
                             index=[1, 2])
# print(more_rainfall)
# print(df6)
# print(df6 + more_rainfall)
b = df6.add(more_rainfall, fill_value=0)
# print(b)
# When you have a DataFrame and a Series in your calculation,
# by default the Series is broadcast along the index:so the series is added to all rows!!!
# # print(df6)
c = df6.loc[1, :]
print(c)
d = c + df6
# print(d)


#   Working with Text Columns
users = pd.DataFrame(data=[" mArk ", "JOHN ", "Tim", " jenny"], columns=["name"])
users_cleaned = users.loc[:, "name"].str.strip().str.capitalize()
users_cleaned.str.startswith("J")


#   Applying a Function: applymap method,
def format_string(x: str) -> str:
    """format_string _summary_

    _extended_summary_

    Args:
        x (str): _description_

    Returns:
        str: _description_
    """
    return f"{x:,.2f}"


e = df6.applymap(format_string)
# better with lambda
print(df6.applymap(lambda x: f"{x:,.2f}"))
print(e)

"""
View vs. Copy
- Set values on the original DataFrame, not on a DataFrame that has been sliced off another DataFrame
- If you want to have an independent DataFrame after slicing, make an explicit copy:
    selection = df.loc[:, ["country", "continent"]].copy()
While things are complicated with loc and iloc, it’s worth remembering that all
DataFrame methods such as df.dropna() or df.sort_values("column_name") always return a copy.
"""
