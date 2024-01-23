import pandas as pd
"""Slicing"""

xyz_web = {"Day":[1, 2, 3, 4, 5, 6], "Visitors":[1000, 700, 6000, 1000, 400, 350], "Bounce_Rate":[20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(xyz_web)
#print(df.head(2))
#print(df.tail(2))

"""Merging"""

df1 = pd.DataFrame({"HPI":[80, 90, 70, 60], "Int_race":[2, 1, 2, 3], "IND_GDP":[50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI":[80, 90, 70, 60], "Int_race":[2, 1, 2, 3], "IND_GDP":[50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

merge = pd.merge(df1, df2, on="HPI")

print(merge)




