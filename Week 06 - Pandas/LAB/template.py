"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("/Users/abisolaafolabi/Documents/CST1510/Week 06 - Pandas/LAB/my_file.csv")   # replace with pd.read_csv("your_file.csv")

# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")

# ================================================================== OUTPUT
# 3. Print the DataFrame.
print(df)
not_ok = df[df["status"]!= "OK"]
print(not_ok)
count = df.groupby("status").size()
print(count)

import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind="bar")
plt.title("Status Count")
plt.savefig("status_count.png")
plt.show

df.to_csv("full_df.csv")


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
