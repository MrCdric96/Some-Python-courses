"""What is pandas : is a software library written for the python programming language for datamanipulations and analasys."""
import pandas as pd

xyz_web = {"Day":[1, 2, 3, 4, 5, 6], "Visitors":[1000, 700, 6000, 1000, 400, 350], "Bounce_Rate":[20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(xyz_web)
print(df)