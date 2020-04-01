"""
Implementing 2 ML algorithms to check system and User-level resource usage.
1. A linear Regression model on the hackneyed Titanic passenger information dataset.
2. Objective; create a prediction model, then predict the Age-variable of passengers from available data.
              collate system resource usage data during program execution. Program memory, virtual memory, time, page-fault etc.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinRegression:
    def __init__(self):
        pass

    def get_pid(self):
        proc_id = os.getpid()
        return proc_id

    def ML_model_L2(self):
        # Read data into memory with pandas dataframe library
        df = pd.read_excel("dataset.xlsx", sheet_name="Sheet1")
        df.drop(["Cabin", "Name", "Ticket"], axis=1)
        df["Fare"].astype(int)

        input_1 = df[["Embarked", "Fare", "Parch", "PassengerId", "Pclass", "Sex", "SibSp", "Survived", "Title",
                      "Family_Size"]]
        output = df[["Age"]]

        input_train, input_test, output_train, output_test = train_test_split(input_1, output, test_size=0.11)

        lin_Reg = LinearRegression()
        lin_Reg.fit(input_train, output_train)

        age_prediction_model = lin_Reg.predict(input_test)
        accuracy = lin_Reg.score(input_test, output_test)
        print(age_prediction_model)
        print(f"Accuracy: {accuracy * 100}")



