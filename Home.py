import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from PIL import Image

st.title("NFS Bookings Dashboard")
st.header("Gross Booking Total Prediction")

image = Image.open("NFSTechnology.png")

st.sidebar.image(image)

# st.sidebar.header("User Input Features")

NFS_raw = pd.read_csv("LatestData.csv")
customers_raw = NFS_raw["PotentialCustomer"].tolist()
customers = []
for i in customers_raw:
    if i not in customers:
        customers.append(i)
    else:
        pass

target_mapper = {}
count = 0
for i in customers:
    target_mapper[i] = count
    count += 1


def user_input_features():
    clientBudget = st.number_input("**Client Budget**", 1000, 100000, 10000)
    numberOfPeople = st.slider("**Number Of People**", 3, 81, 10)
    potentialCustomer = st.selectbox("**Potential Customer**", options=customers)
    data = {
        "PotentialCustomer": potentialCustomer,
        "ClientBudget": clientBudget,
        "NumberOfPeople": numberOfPeople,
    }
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()

inputsList = input_df.values.tolist()
potentialCustomer = inputsList[0][0]
clientBudget = inputsList[0][1]
numberOfPeople = inputsList[0][2]


# Combines user input features with entire dataset
# This will be useful for the encoding phase

categorical_cols = ["PotentialCustomer"]

le = LabelEncoder()

NFS_raw[categorical_cols] = NFS_raw[categorical_cols].apply(
    lambda col: le.fit_transform(col)
)

NFS = NFS_raw.drop(
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


input_df["PotentialCustomer"] = input_df["PotentialCustomer"].apply(
    lambda row: target_mapper[row]
)

print(input_df)

# Reads in saved regression model
load_model = pickle.load(
    open(
        "NFSModel.pkl",
        "rb",
    )
)

# Apply the model to make predictions
prediction = load_model.predict(input_df)


predictionList = prediction.tolist()
grossBookingTotal = round(predictionList[0], 2)
print(grossBookingTotal)
st.subheader(
    f"For the customer {potentialCustomer} with a **Client Budget** of £{str(clientBudget)} and an event with {str(numberOfPeople)} people,\
        the predicted **Gross Booking Total** is:"
)
st.write(f"# £{grossBookingTotal} #")
