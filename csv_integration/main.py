import pandas as pd

print("Hello")

input_csv = pd.read_csv("input.csv")

print(input_csv.head())

output_csv = input_csv.copy()

output_csv["dado1"] = output_csv["dado1"]*10

output_csv.to_csv("output.csv", index=False)
