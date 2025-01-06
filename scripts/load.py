#import os
#import pandas as pd
#from scripts.extract import extract_csv, extract_api, extract_sql
#from scripts.transform import clean_data, add_calculated_columns
import mysql.connector
import json

# อ่านค่า config จากไฟล์ config.json
with open('config/config.json') as config_file:
    config = json.load(config_file)

def load_to_mysql(data, table_name, config):
    # เชื่อมต่อกับฐานข้อมูล MySQL
    connection = mysql.connector.connect(
        host=config['mysql_host'],
        user=config['mysql_user'],
        password=config['mysql_password'],
        database=config['mysql_db']
    )
    cursor = connection.cursor()

    # ลบคอลัมน์ 'total_sales' ออกจาก DataFrame หากมี
    if 'total_sales' in data.columns:
        data = data.drop(columns=['total_sales'])

    # เตรียมคำสั่ง SQL สำหรับการ insert ข้อมูล
    for _, row in data.iterrows():
        update_values = ', '.join([f"{col} = %s" for col in data.columns if col != 'transaction_id'])
        sql = f"""
        INSERT INTO {table_name} 
        ({', '.join(data.columns)}) 
        VALUES ({', '.join(['%s'] * len(row))})
        ON DUPLICATE KEY UPDATE 
        {update_values}
        """
        cursor.execute(sql, tuple(row) + tuple(row[1:]))  # ใช้ tuple 2 ครั้งเพื่อให้ข้อมูลตรงกับทั้ง insert และ update
        
    # Commit การเปลี่ยนแปลงและปิดการเชื่อมต่อ
    connection.commit()
    cursor.close()
    connection.close()
