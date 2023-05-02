# AIAP 14

## a. Full name (as in NRIC) and email address.

Lim Rui Bing
rbruibingnet@gmail.com

## b. Overview of the submitted folder and the folder structure.

```
├── src
│   └── run.py
│   └── ml_module
│       └── data_extract.py
│       └── data_prep.py
│       └── modelling.py
├── data
│   └── fishing.db
├── README.md
├── eda.ipynb
├── requirements.txt
└── run.sh
```

## c. Instructions for executing the pipeline and modifying any parameters.

To execute the pipeline:
1. Install dependencies using `pip install -r requirements.txt`
2. Run `./run.sh`

To modify parameters:
1. Head to ./src/ml_module/modelling.py
2. Edit the parameters in the method named `model`

## d. Description of logical steps/flow of the pipeline.

### 1. Data Extraction

1. Extracted from `data/fishing.db` using sqlite3
2. Read in using `pandas.read_sql_query()`

### 2. Data Preparation

1. Duplicate values are dropped
2. Invalid data are converted to `np.nan`
3. Missing values are imputed using `sklearn.imputer.SimpleImputer`
4. Date column is converted to datetime to engineer 2 new columns `Month` and `Day`
5. Categorical features are encoded using `sklearn.preprocessing.LabelEncoder` and `pandas.get_dummies`

### 3. Modelling

1. Data from step 2 is split in 80% training data and 20% test data
2. Train data is used for fitting and prediction
2. Metric scores like `accuracy` and `f1_score` are obtained

## e. Overview of key findings from the EDA

1. Rainfall tends to be higher when there is less sunshine
2. Rainfall tends to be higher when there is higher humidity
3. Rainfall tends to be higher when there is more cloud
4. Tomorrow is less likely to rain when there is more sunshine
5. Sunshine tends to be higher when there is less cloud
6. Average temperatures have a smaller range of values when there is more rainfall
7. Woodlands seem to have a greater percentage of raining on the next day
8. Lower pressure have a greater percentage of raining on the next day
9. Raining today have a greater percentage of raining on the next day

## f. Described how the features in the dataset are processed (summarized in a table)

| Feature         | How its processed                                                      |
| --------------- | ---------------------------------------------------------------------- |
| Date            | Converted to datetime then dropped after creating Month and Day column |
| Location        | One-hot encoded                                                        |
| Rainfall        | -                                                                      |
| Evaporation     | -                                                                      |
| Sunshine        | Negative values are changed to np.nan then imputed mean                |
| WindGustDir     | One-hot encoded                                                        |
| WindGustSpeed   | -                                                                      |
| WindDir9am      | One-hot encoded                                                        |
| WindDir3pm      | One-hot encoded                                                        |
| WindSpeed9am    | -                                                                      |
| WindSpeed3pm    | -                                                                      |
| Humidity9am     | -                                                                      |
| Humidity3pm     | -                                                                      |
| Pressure9am     | Ordinal encoded i.e. low = 0, med = 1, high = 2                        |
| Pressure3pm     | Ordinal encoded i.e. low = 0, med = 1, high = 2                        |
| Cloud9am        | -                                                                      |
| Cloud3pm        | -                                                                      |
| RainToday       | Binary encoded i.e. No = 0, Yes = 1                                    |
| RainTomorrow    | Binary encoded i.e. No = 0, Yes = 1                                    |
| ColourOfBoats   | One-hot encoded                                                        |
| AverageTemp     | -                                                                      |
| Day             | Created from Date column as day of the month                           |
| Month           | Created from Date column as month i.e. Jan = 1, Feb = 2                |

## g. Explanation of your choice of models for each machine learning task.

1. Logistic regression - simplest model, if it can solve the classification problem, there is no need for more complicated models which might be a waste of computation power
2. K Nearest Neighbors - supports non-linear solutions which is great to pair up with logistic regression
3. Multi Layer Perceptron Classifier - realised the F1 scores are not that great, thus I tried to use a neural network model
4. Random Forest - seems like MLP had a poor F1 score as well, thus tried the random forest classifier from sklearn

## h. Evaluation of the models developed. Any metrics used in the evaluation should also be explained.

1. LogisticRegression
Accuracy Score: 0.87
F1 Score: 0.67

2. KNeighborsClassifier
Accuracy Score: 0.82
F1 Score: 0.44

3. MLPClassifier
Accuracy Score: 0.83
F1 Score: 0.62

4. RandomForestClassifier
Accuracy Score: 0.86
F1 Score: 0.66

Surprisingly, the logistic regression model performed the best when we are using the F1 score metric. F1 score is used because it takes into account both the precision and recall of the model.
