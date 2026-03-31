import sys
import pandas as pd
from enum import Enum



def load_csv(file_path):
    return pd.read_csv(file_path)    

def map_dtypes(df):
    results = {}  
    for col_name in df.columns:
        dtype = df[col_name].dtype
        if dtype == "str":
            results[col_name] = "TEXT"  
        elif dtype == "int64":
            results[col_name] = "INTEGER"  
        elif dtype == "float64":
            results[col_name] = "REAL"
        else:
            results[col_name] = "TEXT"
    return results

def build_create_table(table_name, table_dict):
    sql_table_name = "CREATE TABLE " + table_name
    
    columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]
    
    for key, value in table_dict.items():
        columns.append(key + " " + value)
    
    sql_table_data = ", ".join(columns)
    sql_string = sql_table_name + "(" + sql_table_data + ");"
    return sql_string

# def build_sql_table(sql_string):
    
def main():
    
    df = load_csv("locations.csv")
    results = map_dtypes(df)
    print(results)
    build_create_table("locations", results)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
