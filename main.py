import os
import pandas as pd
from exercise.config import DataH

from tools.utils.database import Database
db = Database()

values = DataH().read_yaml_values(r"D:\Kahoku\AutoTest\page\data\game_config_info.yaml")

# print(values["FORTNITE"])

# game_name = "OVERWATCH"
table_name = "fortnite_info"

# db.create_table(table_name)

# for label_id, label in zip(range(len(values[game_name]["LABEL"])), 
#                                    values[game_name]["LABEL"]
#                                 #    values[game_name]["LAMP_EFFECT"]
#                                 ):
#     print(f">>> Label_Name: {label}, Lamp_Effect: None")
#     db.insert_data(table_name, label_id, label, 0)

description, table_data = db.select_from(table_name)
# print(table_data)

df = pd.DataFrame(table_data, columns=[x[0] for x in description])
# array = pd.to_numeric(df["Lamp_Effect"]).tolist()
array =df["Label_Name"].tolist()
# print(array)

list = array
print(list)

# df.plot()

