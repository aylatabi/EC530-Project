import pandas as pd
from csv_loader import load_csv, map_dtypes, build_create_table
df = pd.read_csv("locations.csv")
test_dict = {'Location': 'TEXT', 'Latitude / Longitude': 'TEXT'}
#python -m pytest pytest_project.py 
def test_df_creation():  
    result = load_csv("locations.csv")
    assert df["Location"][0] == result["Location"][0]
    
def test_df_mapping():
   result =  map_dtypes(df)
   assert test_dict["Location"] == result["Location"]
   
def test_create_table_sql():
    test_sql_string = "CREATE TABLE locations(id INTEGER PRIMARY KEY AUTOINCREMENT, Location TEXT, Latitude / Longitude TEXT);"
    result = build_create_table("locations", test_dict) 
    assert test_sql_string == result
# def test_bad_coordinates_latitude_1():
#     result = find_closest_airport((-200, -97.7431), None, False, df)
#     assert result == -1
