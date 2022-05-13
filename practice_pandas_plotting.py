# to open jupyter note book in other plane add code below: and click "run cell"
# %%
"""
if you want to list all currently available magic commands, 
 run %lsmagic, and for a detailed description, run %magic.
"""
import numpy as np
import pandas as pd
# in jupyterbooks add following line:
# %matplotlib inline # or more dynamic the following:
# Or %matplotlib notebook

# MATPLOTLIB
data = pd.DataFrame(data=np.random.rand(4, 4) * 100000,
                    index=["Q1", "Q2", "Q3", "Q4"],
                    columns=["East", "West", "North", "South"])
data.index.name = "Quarters"
data.columns.name = "Region"
print(data)
data.plot()  # Shortcut for data.plot.line()

# Set the plotting backend to Plotly
# %%
pd.options.plotting.backend = "plotly"
data.plot()
# Display the same data as bar plot
data.plot.bar(barmode="group")


# line    Line Chart, default when running df.plot()
# bar     Vertical bar chart
# barh    Horizontal bar chart
# hist    Histogram
# box     Box plot
# kde     Density plot, can also be used via density
# area    Area chart
# scatter Scatter plot
# hexbin  Hexagonal bin plots
# pie     Pie chart


# %%


