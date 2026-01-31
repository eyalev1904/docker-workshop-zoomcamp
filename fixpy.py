import pandas as pd
from sqlalchemy import create_engine

# Use the port from your docker-compose (5433)
engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

try:
    # Create a tiny 1-row dataframe to test
    test_df = pd.DataFrame({'test_col': [1]})
    test_df.to_sql(name='test_table', con=engine, if_exists='replace')
    print("Success! Connection works and table created.")
except Exception as e:
    print(f"Error: {e}")