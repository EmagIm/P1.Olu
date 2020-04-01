"""
Implementing 2 ML algorithms to check system and User-level resource usage.
1. A logistic Regression model on the hackneyed Titanic passenger information dataset.
2. Objective; create a prediction model, then predict the survival of test passengers data.
              collate system resource usage data during program execution. Program memory, virtual memory, time, page-fault etc.
"""

# Read data into memory with pandas dataframe library
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class LogRegression_P1:
    def __init__(self):
        pass

    def get_pid(self):
        proc_id = os.getpid()
        return proc_id

    def ML_model_L1(self):
        df = pd.read_excel("dataset.xlsx", sheet_name="Sheet1")
        df.drop(["Cabin", "Name", "Ticket"], axis=1)
        df["Fare"].astype(int)

        input_1 = df[["Age", "Embarked", "Fare", "Parch", "PassengerId", "Pclass", "Sex", "SibSp", "Title",
                      "Family_Size"]]
        output = df[["Survived"]]
        input_1 = np.array(input_1)
        output_1 = np.array(output)
        input_train, input_test, output_train, output_test = train_test_split(input_1, output_1, test_size=0.11)

        logst_Reg = LogisticRegression(solver='liblinear', multi_class='ovr')
        logst_Reg.fit(input_train, output_train)

        survival_prediction_model = logst_Reg.predict(input_test)
        accuracy = logst_Reg.score(input_test, output_test)
        print(survival_prediction_model)
        print(f"Accuracy: {accuracy * 100}")

'''
import csv

with open("dataset.csv", 'rt') as file:
    rdr_data = csv.reader(file)
    with open("dataset2.csv", 'wt') as file:
        wrt_data = csv.writer(file)
        for r in rdr_data:
            wrt_data.writerow((r[0], r[2], r[3], r[5], r[6], r[7], r[8], r[9], r[10]))
'''

# sort 1-d array out