from config_upload_csv_to_db import user, password, host, port, database
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}', poolclass=NullPool)
date1 = '2020-06-13'
date2 = '2020-06-18'
date1=pd.to_datetime(date1)
date2=pd.to_datetime(date2)
campaign = "DOZ_iOS_lkl-1_purch_val-based_campaign-opt_purch-opt"
qry = f"SELECT campaign, sum(event_revenue) as event_revenue_sum, sum(event_revenue_usd) as event_revenue_usd_sum from events where event_time between '{date1}' and '{date2}' and campaign = '{campaign}' group by campaign"
df2 = pd.read_sql(qry, engine)


df3 = pd.read_sql('select campaign,count(event_name) as count_installs from installs1 i group by campaign', engine)

dm = df2.merge(df3, how='left', left_on='campaign', right_on='campaign')

print(dm)

