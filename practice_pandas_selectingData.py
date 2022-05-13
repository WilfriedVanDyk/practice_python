import pandas as pd
file = pd.read_excel("xl/course_participants.xlsx")
# print(file)

data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]
df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
""" or construct a dataframe with a dictionary: "city1" etc are the column names, index set as default here
        rainfall = pd.DataFrame(data={"City 1": [300.1, 100.2],
                              "City 2": [400.3, 300.4],
                              "City 3": [1000.5, 1100.6]})

        _extended_summary_
"""
# print(df.info())
# print(df.dtypes)

# INDICES !!!!!!!
df.index.name = "user_id"
# print(df)
# Whenever you call a method on a DataFrame in the form df.method_name(),
# you will get back a copy of the DataFrame with that method applied, leaving the original DataFrame untouched.
# reasign the new df to the old one!! to 
df.reset_index()  # gives a new standaard index column, the old index column changes into a regular column
df.reset_index().set_index("name")  # changes the standard index column to name_index column
df.reindex([999, 1000, 1001, 1004])  # to change the index figures
df.sort_index()  # to sort by the index column
df.sort_values(["continent", "age"])  # to sort by diff columns

# COLUMNS!!!!
df.columns.name = "properties"
df.rename(columns={"name": "First Name", "age": "Age"})
df.drop(columns=["name", "country"], # drop columns and indices at the same time
        index=[1000, 1003])
df.T  # Shortcut for df.transpose()

# SELECTING DATA
#       SELECTING BY NAME
# df.loc[row_selection, column_selection]
df.loc[:, ["continent", "country", "name", "age", "score"]] # to reorder the columns
# Single value          Scalar          df.loc[1000, "country"]
# Using scalars for both row and column selection returns a scalar
df.loc[1001, "name"]
# diff between series and dataframes
# Both DataFrame and Series have an index, but only the DataFrame has column headers
# When you select a column as Series, the column header becomes the name of the Series.
# One column(1d)        Series          df.loc[:, "country"] or you can write: df[column_selection]
# One row(1d)           Series          df.loc[1000, :]
# Using a scalar on either the row or column selection returns a Series
df.loc[[1001, 1002], "age"]
# One column(2d)        DataFrame       df.loc[:, ["country"]]
# Multiple columns      DataFrame       df.loc[:, ["country", "age"]] or df[["country", "age"]]
# Range of columns      DataFrame       df.loc[:, "name":"country"] slicing with labels include the upper end.
# One row(2d)           DataFrame       df.loc[[1000], :]
# Multiple rows         DataFrame       df.loc[[1003, 1000], :]
# Range of rows         DataFrame       df.loc[1000:1002, :]
# Selecting multiple rows and columns returns a DataFrame
df.loc[:1002, ["name", "country"]]

#       SELECTING BY POSITION WITH integer location iloc
# df.iloc[row_selection, column_selection]
# Single value          Scalar          df.iloc[1, 2]
df.iloc[0, 0]
# One column(1d)        Series          df.iloc[:, 2]
# One row(1d)           Series          df.iloc[1, :]
df.iloc[[0, 2], 1]
# One column(2d)        DataFrame       df.iloc[:, [2]]
# Multiple columns      DataFrame       df.iloc[:, [2, 1]]
# Range of columns      DataFrame       df.iloc[:, :3]
# One row(2d)           DataFrame       df.iloc[[1], :]
# Multiple rows         DataFrame       df.iloc[[3, 1], :]
# Range of rows         DataFrame       df.iloc[1:3, :]
df.iloc[:3, [0, 2]]

#       SELECTING BY BOOLEAN INDEXING
"""
        and     &
        or      |
        not     ~
"""
tf = (df["age"] > 40) & (df["country"] == "USA")
# print(tf) # shows only an index column with a boolean column
# print(df.loc[tf, :]) # uses the tf boolean results to show the other columns
a = df.loc[df.index > 1001, :]
# print(a)
u = df.loc[df.index > 1001]
# print(u)
df.loc[df["country"].isin(["Italy", "Germany"]), :]

# df[boolean_df]
# This could be the yearly rainfall in millimeters
rainfall = pd.DataFrame(data={"City 1": [300.1, 100.2],
                              "City 2": [400.3, 300.4],
                              "City 3": [1000.5, 1100.6]})
# rainfall Out[28]: City 1 City 2 City 3
# 0 300.1 400.3 1000.5
# 1 100.2 300.4 1100.6
rainfall < 400
# Out[29]: City 1 City 2 City 3
#        0 True   False  False
#        1 True   True   False
rainfall[rainfall < 400]
# Out[30]: City 1 City 2 City 3
#       0  300.1  NaN    NaN
#       1  100.2  300.4  NaN

#       SELECTING BY USING A MULTI INDEX P96
# A MultiIndex needs to be sorted
df_multi = df.reset_index().set_index(["continent", "country"])
# print (df_multi, "/n")
df_multi = df_multi.sort_index()
# print(df_multi, "/n")
df_multi.loc["Europe", :]
# print(df_multi.loc["Europe", :])
df_multi.loc[("Europe", "Italy"), :] # selecting over multiple indexes wiht a TUPLE!!
df_multi.reset_index(level=0) # resets the first index column to a regular column


# a view versus  a copy
