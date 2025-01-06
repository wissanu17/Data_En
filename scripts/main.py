import os
import pandas as pd
from extract import extract_csv, extract_api, extract_sql
from transform import clean_data, add_calculated_columns
from load import load_to_mysql
import json

# อ่าน config.json
with open('config/config.json') as config_file:
    config = json.load(config_file)

def main():
    # Extract
    # ดึงข้อมูลจาก CSV
    csv_data = extract_csv('data/sales.csv')

    # ดึงข้อมูลจาก API
    #api_data = extract_api(config['api_url'])

    # ดึงข้อมูลจาก SQL
    sql_data = extract_sql(config['db_connection'], 'SELECT * FROM sales_data')

    # รวมข้อมูล
    all_data = pd.concat([csv_data, sql_data], ignore_index=True)

    # Transform
    all_data = clean_data(all_data)
    all_data = add_calculated_columns(all_data) #ไม่ใช้ก็ได้เพราะคอลัมน์ total_sales คำนวณได้จาก MySQL จึงทำการ drop คอลัมน์นี้ ที่ฟังก์ชัน load_to_mysql

    # Load (MySQL)
    table_name = config['mysql_edge']  # ดึงค่า MySQL Table จากไฟล์ config
    load_to_mysql(all_data, table_name, config)

if __name__ == "__main__":
    main()

