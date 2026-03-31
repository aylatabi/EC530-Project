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

def main():
    
    df = load_csv("locations.csv")
    results = map_dtypes(df)
    print(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())
