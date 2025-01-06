import streamlit as st
import pandas as pd
import plotly.express as px
from google.cloud import bigquery

# อ่านข้อมูลจาก BigQuery
def load_data_from_bigquery():
    client = bigquery.Client()
    query = "SELECT * FROM your_project_id.your_dataset_id.sales_data"
    data = client.query(query).to_dataframe()
    return data

# สร้างกราฟแสดงข้อมูล
def create_sales_chart(data):
    # สร้างกราฟแสดงยอดขายตามเวลา
    fig = px.line(data, x="date", y="total_sales", title="Sales Over Time")
    st.plotly_chart(fig)

def main():
    st.title("Sales Dashboard")
    
    # โหลดข้อมูลจาก BigQuery
    data = load_data_from_bigquery()
    
    # แสดงข้อมูลตาราง
    st.subheader("Sales Data")
    st.write(data.head())

    # สร้างกราฟแสดงข้อมูล
    create_sales_chart(data)

    # การแสดงยอดขายตามแผนก
    st.subheader("Total Sales by Department")
    department_sales = data.groupby("department")["total_sales"].sum().reset_index()
    st.bar_chart(department_sales.set_index("department")["total_sales"])

    # กราฟการกระจายยอดขาย
    st.subheader("Sales Distribution")
    fig = px.histogram(data, x="total_sales", nbins=20, title="Sales Distribution")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
