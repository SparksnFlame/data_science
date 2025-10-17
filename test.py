# C:/Users/LENOVO/Documents/Projetos/Data_science/data_science/env/Scripts/Activate.ps1 
import pandas as pd

print("Hello World")

path = "C:\\Users\\LENOVO\\Documents\\Projetos\\Data_science\\cybersec_dataset\\cybersecurity_attacks.csv"
df = pd.read_csv(path)

# print(df.head())

print(df["Protocol"].unique())
