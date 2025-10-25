import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Scatter Graphs")

NFS_raw = pd.read_csv("LatestData.csv")


clientBudget_grossBookingTotal = px.scatter(
    data_frame=NFS_raw,
    x="ClientBudget",
    y="GrossBookingTotal",
    size="GrossBookingTotal",
    trendline="ols",
    color_discrete_sequence=["orange"],
)

st.subheader("Client Budget vs. Gross Booking Total")
st.write(clientBudget_grossBookingTotal)

numberofPeople_clientBudget = px.scatter(
    data_frame=NFS_raw,
    x="NumberOfPeople",
    y="ClientBudget",
    size="ClientBudget",
    trendline="ols",
    color_discrete_sequence=["orange"],
)

st.subheader("Number of People vs. Client Budget")
st.write(numberofPeople_clientBudget)
