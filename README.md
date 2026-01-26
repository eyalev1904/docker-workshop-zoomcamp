# docker-workshop-zoomcamp
Workshop Codespaces
1) pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
Answer : 25.3
2) The hostname is db and the port is 5432
3) After downloading the data, pushing data to DB
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

--USE read_parquet FOR THE .parquet FILE
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')

--PUSH TO DB
df_green.to_sql(name='green_tripdata', con=engine, if_exists='replace', chunksize=100000)
print("Success!")

SQL Query
select count(*) from green_tripdata
where trip_distance <= 1
and lpep_pickup_datetime between '2025-11-01' and '2025-12-01'
Answer : 8,007

4) Query : select lpep_pickup_datetime from green_tripdata
where trip_distance <= 100
order by trip_distance desc 
limit 1

Answer : 2025-11-14 15:36:27

5) Query :
SELECT 
    z."Zone", 
    SUM(g.total_amount) AS total_pickup_amount
FROM green_tripdata g
  JOIN zones z ON g."PULocationID" = z."LocationID"
WHERE CAST(g.lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_pickup_amount DESC
LIMIT 1;

Answer : East Harlem North
