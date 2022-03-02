import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

PATH_TRAIN = "heavymachine_data.csv"
PATH_INPUT = "input_data.csv"
PATH_OUTPUT = "output_data.csv"

df = pd.read_csv(PATH_TRAIN, sep=";")
output_colum = "Hours"
input_colums = ["Model", "Aplication", "Age"]
# retira coluna inutil
df.drop("Chassi", axis="columns", inplace=True)
# retira dados ruidosos
hours = df["Hours"]
std = hours.std()
mean = hours.mean()
df.drop(hours[hours > mean+std].index, inplace=True)

df_dummys = pd.get_dummies(df, columns=["Aplication", "Model"])
train_ds_dummys = df_dummys.sample(frac=0.7, random_state=0)
train_ds_dummys = df_dummys
test_ds_dummys = df_dummys.drop(train_ds_dummys.index)

y = []
x = []
for i, r in train_ds_dummys.iterrows():
    y.append(r["Hours"])
    r.drop("Hours", inplace=True)
    x.append(list(r))
regressor = DecisionTreeRegressor(max_depth=5)
model_categorical = regressor.fit(x, y)

# errors = []
# for i, r in test_ds_dummys.iterrows():
#     y_true = pd.to_numeric(r["Hours"])
#     r.drop("Hours", inplace=True)
#     in_data = np.array(list(r)).reshape(-1, r.shape[0])
#     y_pred = model_categorical.predict(in_data)
#     errors.append(abs(y_pred - y_true))
# mae = np.mean(errors)
# print("Mae: {}".format(mae))


input_data = pd.read_csv(PATH_INPUT, sep=",", nrows=1)
d = pd.DataFrame(columns=list(train_ds_dummys), index=[0])
d.drop("Hours", axis="columns", inplace=True)
d.fillna(value=0, inplace=True)
for i, r in input_data.iterrows():
    d["Model_"+str(r["Model"])] = 1
    d["Aplication_"+str(r["Aplication"])] = 1
    d["Age"] = r["Age"]

x = d.values.tolist()
y = model_categorical.predict(x)

output_data = pd.DataFrame()
output_data["Hours"] = y
output_data.to_csv(PATH_OUTPUT)
# output_data.to_csv(PATH_OUTPUT, sep=";", float_format="%,f")
