import pandas as pd
import numpy as np
import datetime as dt
#   The to_excel Method and ExcelWriter Class
# sheet_name: Name of the sheet to write to.
# startrow and startcol:
#   startrow is the first row where the DataFrame will be written to and
#   startcol is the first # column.
#   This uses zero-based indexing, so if you want to write your DataFrame into cell B3, use
#   startrow = 2 and startcol = 1.
# index and header: If you want to hide the index and / or header, set them to index = False and header = False,
#   respectively.
# na_rep and inf_rep: By default, np.nan will be converted to an empty cell, while np.inf, NumPy’s representation
#   of infinity, will be converted to the string inf. Providing values allows you to change this
#   behavior.
# freeze_panes: Freeze the first couple of rows and columns by supplying a tuple:
#   for example (2, 1) will freeze the first two rows and the first column.

data=[[dt.datetime(2020,1,1, 10, 13), 2.222, 1, True],
      [dt.datetime(2020,1,2), np.nan, 2, False],
      [dt.datetime(2020,1,2), np.inf, 3, True]]
df = pd.DataFrame(data=data,
                  columns=["Dates", "Floats", "Integers", "Booleans"])
df.index.name="index"
# df
# Out[17]: Dates               Floats   Integers Booleans
# index
# 0        2020-01-01 10:13:00  2.222    1       True
# 1        2020-01-02 00:00:00  NaN      2       False
# 2        2020-01-02 00:00:00  inf      3       True
df.to_excel("written_with_pandas.xlsx", sheet_name="Output",
            startrow=1, startcol=1, index=True, header=True,
            na_rep="<NA>", inf_rep="<INF>")

# ExcelWriter class
# If you want to write multiple DataFrames to the same or different sheets, you will
# need to use the ExcelWriter class. The following sample writes the same DataFrame
# to two different locations on Sheet1 and one more time to Sheet2
with pd.ExcelWriter("written_with_pandas2.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1", startrow=1, startcol=1)
    df.to_excel(writer, sheet_name="Sheet1", startrow=10, startcol=1)
    df.to_excel(writer, sheet_name="Sheet2")


