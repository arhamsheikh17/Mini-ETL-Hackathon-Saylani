
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------------------------------------
# Load Data
# -----------------------------------------------------------
st.title("Banggood Product Analysis Dashboard")

df = pd.read_csv("transformed_banggood_products_with_category_clean.csv")

st.subheader("Dataset Overview")
st.write(df.head())
st.write("Total Products:", len(df))

# -----------------------------------------------------------
# Price Distribution per Category (KDE)
# -----------------------------------------------------------
st.subheader("Price Distribution per Category")

fig, ax = plt.subplots(figsize=(8, 5))
for category, group in df.groupby("category"):
    group["price"].plot(kind="kde", ax=ax, label=category)

ax.set_title("Price Distribution per Category")
ax.set_xlabel("Price")
ax.legend()
st.pyplot(fig)

# -----------------------------------------------------------
# Rating vs Price Scatter Plot
# -----------------------------------------------------------
st.subheader("Rating vs Price Relationship")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["rating"], df["price"])
ax.set_xlabel("Rating")
ax.set_ylabel("Price")
ax.set_title("Rating vs Price")
st.pyplot(fig)

# -----------------------------------------------------------
# Top Reviewed Products (Bar Chart)
# -----------------------------------------------------------
st.subheader("Top 10 Most Reviewed Products")

top_reviewed = df.nlargest(10, "review_count")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_reviewed["title"], top_reviewed["review_count"])
ax.set_xlabel("Review Count")
ax.set_title("Top 10 Most Reviewed Products")
ax.invert_yaxis()
st.pyplot(fig)

# -----------------------------------------------------------
# Best Value Score (Rating / Price)
# -----------------------------------------------------------
st.subheader("Top 10 Best Value Products (Rating ÷ Price)")

df["value_score"] = df["rating"] / df["price"]
best_value = df.sort_values("value_score", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(best_value["title"], best_value["value_score"])
ax.set_xlabel("Value Score (Higher = Better)")
ax.set_title("Top 10 Best Value Products")
ax.invert_yaxis()
st.pyplot(fig)

# -----------------------------------------------------------
# Avg Review Count Per Category
# -----------------------------------------------------------
st.subheader("Average Review Count per Category")

avg_reviews = df.groupby("category")["review_count"].mean().sort_values()

fig, ax = plt.subplots(figsize=(8, 5))
avg_reviews.plot(kind="barh", ax=ax)
ax.set_xlabel("Average Review Count")
ax.set_title("Average Review Count per Category")
st.pyplot(fig)

# Done
st.success("Dashboard Loaded Successfully!")
