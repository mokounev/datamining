import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime as DT

#create dataframe, separate datetime into date and time
df = pd.read_csv('dataset_mood_smartphone.csv', delimiter=',')
# print(df)
df = pd.read_csv('dataset_mood_smartphone.csv', delimiter=',', parse_dates=[0], infer_datetime_format=True)
temp = pd.DatetimeIndex(df['time'])
df['Date'] = temp.date
df['Time'] = temp.time
del df['time']

# average mood per person per day
df_mood = df.iloc[ :5641,:]
mood_average = df_mood.groupby(['id', 'Date']).mean().reset_index()
mood_average.columns = ['id', 'Date', 'mood']

# average arousal per person per day
df_arousal = df.iloc[5641:11284,:]
arousal_average = df_arousal.groupby(['id', 'Date']).mean().reset_index()
arousal_average.columns = ['id', 'Date', 'arousal']
combine_df = pd.merge(mood_average, arousal_average,  how='left', left_on=['id','Date'], right_on = ['id','Date'])

# average valence per person per day
df_valence = df.iloc[11284:16927,:]
valence_average = df_valence.groupby(['id', 'Date']).mean().reset_index()
valence_average.columns = ['id', 'Date', 'valence']
combine_df = pd.merge(combine_df, valence_average,  how='left', left_on=['id','Date'], right_on = ['id','Date'])

# !not taken into account the missing hours!
df_activity = df.iloc[16927:39892,:]
activity_average = df_activity.groupby(['id', 'Date']).mean().reset_index()
activity_average.columns = ['id', 'Date', 'activity']
combine_df = pd.merge(combine_df, activity_average,  how='left', left_on=['id','Date'], right_on=['id','Date'])

# screen time per person per day
df_screen = df.iloc[39892:136470,:]
screen_total = df_screen.groupby(['id', 'Date']).sum().reset_index()
screen_total.columns = ['id', 'Date', 'screentime (s)']
combine_df = pd.merge(combine_df, screen_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])

# number of texts + calls per person per day
df_call = df.iloc[136470:141709,:]
df_sms = df.iloc[141709:143507,:]
call_total = df_call.groupby(['id', 'Date']).sum().reset_index()
sms_total = df_sms.groupby(['id', 'Date']).sum().reset_index()
sms_total.columns = ['id', 'Date', '# texts']
call_total.columns = ['id', 'Date', '# calls']
combine_df = pd.merge(combine_df, sms_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, call_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])

# time of all the variables
df_builtin = df.iloc[143507:234795, :]
df_unknown = df.iloc[373231:374170, :]
df_utilities = df.iloc[374170:376657, :]
df_communication = df.iloc[234795:309071, :]
df_entertainment = df.iloc[309071:336196, :]
df_finance = df.iloc[336196:337135, :]
df_games = df.iloc[337135:337948, :]
df_office = df.iloc[337948:343590, :]
df_other = df.iloc[343590:351240, :]
df_social = df.iloc[351240:370385, :]
df_travel = df.iloc[370385:373231, :]
df_weather = df.iloc[376657:376912, :]

# sum the total time per variable
b_total = df_builtin.groupby(['id', 'Date']).sum().reset_index()
un_total = df_unknown.groupby(['id', 'Date']).sum().reset_index()
ut_total = df_utilities.groupby(['id', 'Date']).sum().reset_index()
com_total = df_communication.groupby(['id', 'Date']).sum().reset_index()
ent_total = df_entertainment.groupby(['id', 'Date']).sum().reset_index()
fin_total = df_finance.groupby(['id', 'Date']).sum().reset_index()
gam_total = df_games.groupby(['id', 'Date']).sum().reset_index()
off_total = df_office.groupby(['id', 'Date']).sum().reset_index()
other_total = df_other.groupby(['id', 'Date']).sum().reset_index()
soc_total = df_social.groupby(['id', 'Date']).sum().reset_index()
tra_total = df_travel.groupby(['id', 'Date']).sum().reset_index()
wea_total = df_weather.groupby(['id', 'Date']).sum().reset_index()

# give nice column names
b_total.columns = ['id', 'Date', 'builtin (s)']
un_total.columns = ['id', 'Date', 'unknown (s)']
ut_total.columns = ['id', 'Date', 'utilities (s)']
com_total.columns = ['id', 'Date', 'communication (s)']
ent_total.columns = ['id', 'Date', 'entertainment (s)']
fin_total.columns = ['id', 'Date', 'finance (s)']
gam_total.columns = ['id', 'Date', 'games (s)']
off_total.columns = ['id', 'Date', 'office (s)']
other_total.columns = ['id', 'Date', 'other (s)']
soc_total.columns = ['id', 'Date', 'social (s)']
tra_total.columns = ['id', 'Date', 'travel (s)']
wea_total.columns = ['id', 'Date', 'weather (s)']

#combine into our master file
combine_df = pd.merge(combine_df, b_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, un_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, ut_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, com_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, ent_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, fin_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, gam_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, off_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, other_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, soc_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, tra_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])
combine_df = pd.merge(combine_df, wea_total,  how='left', left_on=['id','Date'], right_on=['id','Date'])

#show our master file
# print(combine_df)

