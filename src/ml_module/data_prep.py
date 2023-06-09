import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    
    # drop duplicate rows
    clean_df = df.drop_duplicates()

    # fix invalid sunshine data
    clean_df.loc[clean_df["Sunshine"] < 0, "Sunshine"] = np.nan

    # fix invalid windgustdir data
    clean_df.loc[((clean_df["WindGustDir"] == "NS") | (clean_df["WindGustDir"] == "EW")), "WindGustDir"] = np.nan

    # fix casing problems in pressure data
    clean_df.loc[:, "Pressure9am"] = clean_df["Pressure9am"].str.lower()
    clean_df.loc[:, "Pressure3pm"] = clean_df["Pressure3pm"].str.lower()

    return clean_df

def impute_missing_values(df):
    
    # set up SimpleImputer
    mean_imputer = SimpleImputer(strategy="mean")
    mode_imputer = SimpleImputer(strategy="most_frequent")

    # get numerical and categorical columns
    numerical_cols = df.select_dtypes("number").columns
    categorical_cols = df.select_dtypes("object").columns

    # impute
    imputed_df = df.fillna(value=np.nan)
    imputed_df.loc[:, numerical_cols] = mean_imputer.fit_transform(imputed_df[numerical_cols])
    imputed_df.loc[:, categorical_cols] = mode_imputer.fit_transform(imputed_df[categorical_cols])

    return imputed_df

def feature_engineer(df):

    # convert datatype to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # create day and month column in the dataframe
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day

    # drop date column
    df = df.drop(columns=["Date"])

    return df

def encode_features(df):
    
    # setup our encoder
    pressure_encoder = LabelEncoder()
    pressure_encoder.fit(["low", "med", "high"])
    rain_encoder = LabelEncoder()
    rain_encoder.fit(["No", "Yes"])

    # encode pressure columns
    encoded_df = df.copy()
    pressure_columns = ["Pressure9am", "Pressure3pm"]
    for col in pressure_columns:
        encoded_df[col] = pressure_encoder.transform(encoded_df[col])

    # encode rain columns
    rain_columns = ["RainToday", "RainTomorrow"]
    for col in rain_columns:
        encoded_df[col] = rain_encoder.transform(encoded_df[col])

    # one hot encoding
    ohe_columns = ["Location", "WindGustDir", "WindDir9am", "WindDir3pm", "ColourOfBoats"]
    encoded_df = pd.get_dummies(data=encoded_df, columns=ohe_columns, dtype=int)

    return encoded_df