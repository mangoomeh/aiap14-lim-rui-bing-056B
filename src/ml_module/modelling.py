from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def model(df):

    # get y-values (series)
    y = df["RainTomorrow"]

    # get features (dataframe)
    X = df.loc[:, df.columns != "RainTomorrow"]

    # feature scaling
    X = StandardScaler().fit_transform(X)
    
    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20, train_size=.8)

    # create models
    models = []
    models.append(LogisticRegression(max_iter=5000))
    models.append(KNeighborsClassifier(n_neighbors=12))
    models.append(MLPClassifier(hidden_layer_sizes=(150,100,50), 
                                max_iter=300,activation = 'relu',
                                solver='adam',
                                random_state=1))
    models.append(RandomForestClassifier())
    
    # fit, predict and show metrics
    for model in models:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(type(model).__name__)
        print("Accuracy Score:", accuracy_score(y_test, y_pred))
        print("F1 Score:", f1_score(y_test, y_pred))
