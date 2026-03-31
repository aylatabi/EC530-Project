import sys
import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)    
    
    
def main():
    
    df = load_csv("locations.csv")
    
    print(df.head())
    return 0


if __name__ == "__main__":
    sys.exit(main())
