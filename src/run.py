from ml_module.data_extract import extract_data
from ml_module.data_prep import clean_data, impute_missing_values, feature_engineer, encode_features
from ml_module.modelling import model

df = extract_data()
df = clean_data(df)
df = impute_missing_values(df)
df = feature_engineer(df)
df = encode_features(df)
model(df)