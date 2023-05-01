# AIAP 14

## **a. Full name (as in NRIC) and email address.**

Lim Rui Bing
rbruibingnet@gmail.com

## **b. Overview of the submitted folder and the folder structure.**

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

## **c. Instructions for executing the pipeline and modifying any parameters.**

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

## **e. Overview of key findings from the EDA**
