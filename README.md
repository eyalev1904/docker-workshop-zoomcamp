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

6) Query :
   SELECT 
	lpep_pickup_datetime,
    z_do."Zone" AS dropoff_zone,
    MAX(t.tip_amount) AS max_tip
FROM 
    green_tripdata t
JOIN 
    zones z_pu ON t."PULocationID" = z_pu."LocationID"
JOIN 
    zones z_do ON t."DOLocationID" = z_do."LocationID"
WHERE 
    z_pu."Zone" = 'East Harlem North'
    AND t.lpep_pickup_datetime >= '2025-11-01 00:00:00'
    -- AND t.lpep_pickup_datetime < '2025-12-01 00:00:00'
GROUP BY 
    1,2
ORDER BY 
    max_tip DESC
LIMIT 1;

Answer : Yorkville West

7) Answer : terraform init, terraform apply -auto-approve, terraform destroy
