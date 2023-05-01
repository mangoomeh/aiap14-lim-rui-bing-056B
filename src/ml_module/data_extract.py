import pandas as pd
import sqlite3

def extract_data():
    conn = sqlite3.connect('fishing.db')
    query = "SELECT * FROM fishing"
    return pd.read_sql_query(query, conn)