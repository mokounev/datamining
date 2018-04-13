import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime as DT

#create dataframe
df = pd.read_csv('dataset_mood_smartphone.csv', delimiter=',')
# print(df)
df = pd.read_csv('dataset_mood_smartphone.csv', delimiter=',', parse_dates=[0], infer_datetime_format=True)
temp = pd.DatetimeIndex(df['time'])
df['Date'] = temp.date
df['Time'] = temp.time
del df['time']


#separate df into variable df
df_mood = df.iloc[ :5641,:]
df_arousal = df.iloc[5641:11284,:]
df_valence = df.iloc[11284:16927,:]
df_activity = df.iloc[16927:39892,:]
df_screen = df.iloc[39892:136470,:]
df_call = df.iloc[136470:141709,:]
df_sms = df.iloc[141709:143507,:]
df_builtin = df.iloc[143507:234795, :]
df_communication = df.iloc[234795:309071, :]
df_entertainment = df.iloc[309071:336196, :]
df_finance = df.iloc[336196:337135, :]
df_games = df.iloc[337135:337948, :]
df_office = df.iloc[337948:343590, :]
df_other = df.iloc[343590:351240, :]
df_social = df.iloc[351240:370385, :]
df_travel = df.iloc[370385:373231, :]
df_unknown = df.iloc[373231:374170, :]
df_utilities = df.iloc[374170:376657, :]
df_weather = df.iloc[376657:376912, :]



mood_average = df_mood.groupby(['id', 'Date']).mean()
print(mood_average)
# print(df_mood.reset_index().groupby('id','Date').mean())


# new_df = df_mood.merge(df_arousal, how='left', left_on=['id','time'], right_on = ['id','time'])
# new_df = new_df.merge(df_valence, how='left', left_on=['id','time'], right_on = ['id','time'])
# print(new_df)
#
# id = new_df['id']
# print(id[0:223])
# time = new_df['time']
# print(time[0])
# mood = new_df['value_x']
# print(mood)
# value = new_df['value_y']
# plt.scatter(time[0:223],mood[0:223])
