import pandas as pd
"""Concatanation"""

df1 = pd.DataFrame({"HPI":[80, 85, 88, 85], "Int_rate":[2, 3, 2, 2], "US_GDP_Thousand":[50, 55, 65, 55]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI":[80, 85, 88, 85], "Int_rate":[2, 3, 2, 2], "US_GDP_Thousand":[50, 55, 65, 55]}, index=[2005, 2006, 2007, 2008])

concat = pd.concat([df1, df2])

print(concat)