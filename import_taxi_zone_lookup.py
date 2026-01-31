import pandas as pd
from sqlalchemy import create_engine

# Using the 5432 port we confirmed earlier
engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

# Use read_csv for this file
df_zones = pd.read_csv('taxi_zone_lookup.csv')

# Load into Postgres
df_zones.to_sql(name='zones', con=engine, if_exists='replace')

print("Zones table created successfully!")fa