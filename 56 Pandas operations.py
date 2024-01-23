import pandas as pd
"""Joining"""

#df1 = pd.DataFrame({"Int_race":[2, 1, 2, 3], "IND_GDP":[50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
#df2 = pd.DataFrame({"Low_Tier_HPI":[50, 45, 67, 34], "Unployement":[1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])

#joined = df1.join(df2)

#print(joined)

"""Changing the index and column headers"""
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df = pd.DataFrame({"Day":[1, 2, 3, 4], "Visitors":[200, 100, 230, 300], "Bounce_Rate":[20, 45, 60, 10]})
df.rename(columns={"Visitors":"Users"})
df.set_index("Day", inplace=True)
df.plot()
plt.show()