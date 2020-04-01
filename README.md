## From cmd/prompt/terminal
Program main component can be executed using absolute path to file </path>, command;
>>> python </path>/ProcessResource.py

## The two modules, Main and ProgramClass(s) contain the program codes
1. Main contains the program main(), dependent on the ProgramClass module(header). Calling the method classes for exec.
2. ProgramClass contains 3 classes; the two algorithms compared for efficiency and the ResourceMonitor() class.
3. Project library dependencies include; Sklearn, psutil,


## Results
1. Execution of both algorithms as multi-threads(not parallel-processes) gives results of
2. CPU usage, utilization
3. Memory usage
4. Disk i/o write
4. Page fault
5. Execution time.. etc

## Notes on Data Encoding
###Embark variable
data = [train_clean.csv]
data['Embarked'] = data['Embarked'].fillna(0)
data['Embarked'] = data['Embarked'].astype(int)
    S,C,Q categories
Embark = {"S": 0, "C": 1, "Q": 2}

###Sex
Sex = {"male": 0, "female": 1}

###Titles
Title = {"Mr": 1, "Mrs": 2, "Master": 3, "Miss": 4, "Rev": 5, "Dr": 6}

