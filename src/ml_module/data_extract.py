import pandas as pd
import sqlite3

def extract_data():
    
    conn = sqlite3.connect('data/fishing.db')
    query = "SELECT * FROM fishing"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df