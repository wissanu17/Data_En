def clean_data(dataframe):
    """
    ทำความสะอาดข้อมูล เช่น ลบข้อมูลซ้ำซ้อนหรือ Missing
    """
    dataframe = dataframe.dropna()           # ลบค่า Missing
    dataframe = dataframe.drop_duplicates()  # ลบข้อมูลซ้ำซ้อน
    print(f"Cleaned data: {len(dataframe)} rows remaining.")
    return dataframe

def add_calculated_columns(dataframe):
    """
    เพิ่มคอลัมน์ 'total_sales' = quantity * price
    """
    dataframe['total_sales'] = dataframe['quantity'] * dataframe['price']
    print("Added calculated column 'total_sales'.")
    return dataframe
