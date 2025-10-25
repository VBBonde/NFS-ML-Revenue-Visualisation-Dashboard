import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Bar Charts")

NFS_raw = pd.read_csv("LatestData.csv")

customers_raw = NFS_raw["PotentialCustomer"].tolist()
customers = []
for i in customers_raw:
    if i not in customers:
        customers.append(i)
    else:
        pass

chosenCustomer = st.selectbox("Choose a customer", options=customers)
results = NFS_raw.loc[NFS_raw["PotentialCustomer"] == chosenCustomer]


eventTitle_grossBookingTotal = px.bar(
    data_frame=NFS_raw,
    x=results["EventTitle"],
    y=results["GrossBookingTotal"],
    labels={
        "x": "Event Title",
        "y": "Gross Booking Total",
    },
    color_discrete_sequence=["orange"],
)

st.subheader("Event Title vs. Gross Booking Total")
st.write(eventTitle_grossBookingTotal)

eventTitle_numberOfPeople = px.bar(
    data_frame=NFS_raw,
    x=results["EventTitle"],
    y=results["NumberOfPeople"],
    labels={
        "x": "Event Title",
        "y": "Number of People",
    },
    color_discrete_sequence=["orange"],
)

st.subheader("Event Title vs. Number of People")
st.write(eventTitle_numberOfPeople)
