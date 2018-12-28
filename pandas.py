import pandas as pd

daily_engagement =  pd.read_csv('daily_engagement_full.csv')

len(daily_engagement['acct'].unique())

