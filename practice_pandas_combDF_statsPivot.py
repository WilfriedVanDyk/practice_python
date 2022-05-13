import pandas as pd

#       concatenate, join and merge dataframes
#   concatination: pd.concat([df1, df2, df3, ...])
data = [[15, "France", 4.1, "Becky"],
        [44, "Canada", 6.1, "Leanne"]]
more_users = pd.DataFrame(data=data,
                          columns=["age", "country", "score", "name"],
                          index=[1000, 1011])

data1 = [["Mark", 55, "Italy", 4.5, "Europe"],
         ["John", 33, "USA", 6.7, "America"],
         ["Tim", 41, "USA", 3.9, "America"],
         ["Jenny", 12, "Germany", 9.0, "Europe"]]
df = pd.DataFrame(data=data1,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])

a = pd.concat([df, more_users], axis=0)  # glue two DataFrames along the columns, set axis=1
# print(a)

data = [[3, 4],
        [5, 6]]
more_categories = pd.DataFrame(data=data,
                               columns=["quizzes", "logins"],
                               index=[1000, 2000])

b = pd.concat([df, more_categories], axis=1)
# print(b)

#   Joining and Merging: WORKS ONLY WITH 2 DATAFRAMES!!!
#  JOIN: relies on the index
# inner, left, right, outer JOIN (SQL): The left join corresponds to the VLOOKUP case in Excel
df1 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]],
                   columns=["A", "B"])
df2 = pd.DataFrame(data=[[10, 20], [30, 40]],
                   columns=["C", "D"], index=[1, 3])
df1.join(df2, how="inner")  # inner, left, right, outer

# MERGE: relies on columns, merge accepts the ON argument to provide one or more columns as the join condition
# these columns, which have to exist on both Data‐Frames, are used to match the rows:
# Add a column called "category" to both DataFrames
df1["category"] = ["a", "b", "c"]
# Out[81]:   A  B  category
#         0  1  2  a
#         1  3  4  b
#         2  5  6  c
df2["category"] = ["c", "b"]
# Out[82]:  C   D   category
#        1  10  20  c
#        3  30  40  b
df1.merge(df2, how="inner", on=["category"])
# Out[83]: A B category C  D
#        0 3 4 b        30 40
#        1 5 6 c        10 20
df1.merge(df2, how="left", on=["category"])
# Out[84]: A B category C     D
#       0  1 2 a        NaN   NaN
#       1  3 4 b        30.0  40.0
#       2  5 6 c        10.0  20.0


#   Descriptive Statistics and Data Aggregation
# descriptive stats
# By default, they return a Series along axis = 0, which means you get the statistic of the columns

rainfall = pd.DataFrame(data={"City 1": [300.1, 100.2],
                              "City 2": [400.3, "nan"],
                              "City 3": [1000.5, 1100.6]})
data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]
df_country = pd.DataFrame(data=data,
                          columns=["name", "age", "country",
                                   "score", "continent"],
                          index=[1001, 1000, 1002, 1003])
# mean
a = rainfall.mean(axis=1)  # default axis = 0 => mean of the columns
# print(a)

# groupby: All nonnumeric columns are automatically excluded
df_country.groupby(["continent"]).mean()  # groupby accepts a list!
b = df_country.groupby(["continent", "country"]).mean()
# print(b)

# agg : to create your own method
df_country.groupby(["continent"]).agg(lambda x: x.max() - x.min())
# Out[90]: properties age  score
#          continent
#          America    8    2.8
#          Europe     43   4.5

#   Pivoting and Melting
data = [["Oranges", "North", 12.30],
        ["Apples", "South", 10.55],
        ["Oranges", "South", 22.00],
        ["Bananas", "South", 5.90],
        ["Bananas", "North", 31.30],
        ["Oranges", "North", 13.10]]
sales = pd.DataFrame(data=data,
                     columns=["Fruit", "Region", "Revenue"])

pivot = pd.pivot_table(sales,
                       index="Fruit", columns="Region",
                       values="Revenue", aggfunc="sum",
                       margins=True, margins_name="Total")
print(pivot)
# Region  North South  Total
# Fruit
# Apples  NaN   10.55  10.55
# Bananas 31.3  5.90   37.20
# Oranges 25.4  22.00  47.40
# Total   56.7  38.45  95.15
pd.melt(pivot.iloc[:-1, :-1].reset_index(),
        id_vars="Fruit",
        value_vars=["North", "South"], value_name="Revenue")
# Out[93]: Fruit   Region  Revenue
#       0  Apples  North   NaN
#       1  Bananas North   31.30
#       2  Oranges North   25.40
#       3  Apples  South   10.55
#       4  Bananas South   5.90
#       5  Oranges South   22.00
