import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_excel("dataset.xlsx", sheet_name="Sheet1")
df.drop(["Cabin", "Name", "Ticket"], axis=1)
df["Fare"].astype(int)

input_1 = df[["Age", "Embarked", "Fare", "Parch", "PassengerId", "Pclass", "Sex", "SibSp", "Title",
              "Family_Size"]]
output = df[["Survived"]]
input_1 = np.array(input_1)
output_1 = np.array(output)
# input_train, input_test, output_train, output_test = train_test_split(input_1, output_1, test_size=0.11)
df2 = pd.read_excel("dataset2.xlsx", sheet_name="test_clean")
df2.drop(["Cabin", "Name", "Ticket"], axis=1)
input_test = df2[["Age", "Embarked", "Fare", "Parch", "PassengerId", "Pclass", "Sex", "SibSp", "Title",
                  "Family_Size"]]
output_test = df[["Survived"]]

logst_Reg = LogisticRegression(solver='liblinear', multi_class='ovr')
logst_Reg.fit(input_1, output)

survival_prediction_model = logst_Reg.predict(input_test)
print(survival_prediction_model)