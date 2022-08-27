import pandas as pd
import os

def fetch_data():
    if os.path.isfile("urls_in_excel.xlsx"):
        df = pd.read_excel("urls_in_excel.xlsx")

    print(df["item"])