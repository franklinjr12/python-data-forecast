import pandas as pd
import math
import random

df = pd.DataFrame()
a = 2
b = 1
c = 0.5

valuesx = []
valuesy = []
valuesz = []
out = []

size = 1000
for i in range(size):
    valuesx.append(a*i+random.random())
    valuesy.append(b*i+random.random())
    valuesz.append(c*i+random.random())
    out.append(valuesx[i]+valuesy[i]+valuesz[i])

df["x"] = valuesx
df["y"] = valuesy
df["z"] = valuesz
df["out"] = out

print(df.describe())

df.to_csv("data.csv")
