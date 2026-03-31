import pandas as pd
from csv_loader import load_csv
df = pd.read_csv("locations.csv")

def test_austin_airport():  
    result = load_csv("locations.csv")
    assert df["Location"][0] == result["Location"][0]
    
# def test_bad_coordinates_latitude_1():
#     result = find_closest_airport((-200, -97.7431), None, False, df)
#     assert result == -1
