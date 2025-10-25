import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

csv_file = "LatestData.csv"

data = pd.read_csv(csv_file)

df = data.copy()

categorical_cols = ["PotentialCustomer"]

le = LabelEncoder()

df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))
print(df[categorical_cols])

x = input("Proceed to model building?")
if x != "yes":
    raise Exception

X = df.drop(
    columns=[
        "EventTitle",
        "Status",
        "SalesPerson",
        "GrossBookingTotal",
        "IntendedStartDate",
        "ClientType",
        "CreatedOn",
        "EventType",
        "Property",
        "SalesStage",
        "MonthCreated",
    ],
    axis=1,
)


y = df["GrossBookingTotal"]


# Build random forest model

from sklearn.ensemble import RandomForestRegressor

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = RandomForestRegressor()
regr.fit(X, y)

predictions = regr.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print("Root Mean Squared Error (RMSE):", rmse, "Closer to 0 is better.")
r2Score = r2_score(y_test, predictions)
print("r2 Score: ", r2Score, "Between 0.50 and 0.99 is Good. 1 is best.")

x = input("Proceed to save model?")
if x != "yes":
    raise Exception


# Saving the model
import pickle

pickle.dump(
    regr,
    open(
        "NFSModel.pkl",
        "wb",
    ),
)
