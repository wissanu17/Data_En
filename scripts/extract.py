import pandas as pd
import requests
from sqlalchemy import create_engine

def extract_csv(file_path):
    """
    ดึงข้อมูลจากไฟล์ CSV
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Extracted {len(data)} rows from {file_path}")
        return data
    except Exception as e:
        print(f"Error extracting CSV: {e}")
        return None

def extract_api(api_url):
    """
    ดึงข้อมูลจาก API ยังไม่ได้ใช้
    """
    try:
        response = requests.get(api_url)
        data = pd.DataFrame(response.json())
        print(f"Extracted {len(data)} rows from API: {api_url}")
        return data
    except Exception as e:
        print(f"Error extracting data from API: {e}")
        return None

def extract_sql(connection_string, query):
    """
    ดึงข้อมูลจาก MySQL Database
    """
    try:
        engine = create_engine(connection_string)
        data = pd.read_sql(query, engine)
        print(f"Extracted {len(data)} rows from SQL")
        return data
    except Exception as e:
        print(f"Error extracting data from SQL: {e}")
        return None

