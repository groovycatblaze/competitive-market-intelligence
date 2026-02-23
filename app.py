import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Entry Strategy Dashboard")

data = pd.read_csv("market_data.csv")

fig = px.bar(data, x="Competitor", y="Market Share")
st.plotly_chart(fig)

st.write("Revenue Projections")
growth_rate = st.slider("Growth Rate", 0.0, 0.5, 0.1)
data["Projected Revenue"] = data["Revenue"] * (1 + growth_rate)
st.write(data)
