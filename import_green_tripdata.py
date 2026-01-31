import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

# USE read_parquet FOR THE .parquet FILE
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')

# PUSH TO DB
df_green.to_sql(name='green_tripdata', con=engine, if_exists='replace', chunksize=100000)
print("Success!")