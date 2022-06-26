import pandas as pd
import numpy as np
import csv, psycopg2, sys


host = 'chunee.db.elephantsql.com'
user = 'wgkidwwr'
password = 'zFIST-t4IAq5hgO_36ij0V4j8e36lAIe'
database = 'wgkidwwr'


conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cur = conn.cursor()



cur.execute("DROP TABLE IF EXISTS air_data;")
cur.execute("""
CREATE TABLE air_data(
    SO2 FLOAT,
    NO2 FLOAT,
    O3 FLOAT,
    CO FLOAT,
    PM10 FLOAT,
    PM2_5 FLOAT,
    total_bad INT);
    """)


dataset = pd.read_csv('Airpollution_dataset.csv')
dataset_idx = pd.DataFrame()
# dataset_idx['SO2'] = range(len(dataset))

data = pd.concat([dataset_idx, dataset], axis = 1)
data = np.array(data)


for i in range(len(data)):
    input = data[i]
    print(input)

    cur.execute("""INSERT INTO air_data (SO2, NO2, O3, CO, PM10, PM2_5, total_bad) VALUES (%s, %s, %s, %s, %s, %s, %s);""", input)

conn.commit()
