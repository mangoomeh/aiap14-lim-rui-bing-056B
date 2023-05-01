from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.neighbors import KNeighborsClassifier

def model(df):

    # get y-values (series)
    y = df["RainTomorrow"]

    # get features (dataframe)
    X = df.loc[:, df.columns != "RainTomorrow"]
    
    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20, train_size=.8)

    # create models
    models = []
    models.append(LogisticRegression(max_iter=5000))
    models.append(KNeighborsClassifier(n_neighbors=15))
    
    # fit, predict and show metrics
    for model in models:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(f1_score(y_test, y_pred))
