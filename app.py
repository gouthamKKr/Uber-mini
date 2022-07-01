import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
    

app_mode = st.sidebar.selectbox('Select Page',['Home','Count Vs Category','Count Vs Purpose','Miles Travelled','Trips VS Hours','Trips Vs Week Days','Trips Vs Days of December','Trips VS Month','Count Vs Starting Point','Pickup Point Vs Frequency','End Point Vs Frequency','Purpose'])
data = pd.read_csv("Uber Drives.csv")
data = data.dropna()

data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")
hour=[]
day=[]
dayofweek=[]
month=[]
weekday=[]
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday

if app_mode=='Home':
    st.title('Uber Data Analysis') 
    st.markdown('Dataset :')
    st.write(data.head(11))

elif app_mode=='Count Vs Category':
    fig=plt.figure(figsize=(10,4))
    plt.title('Count Vs Category')
    data['CATEGORY*'].value_counts()
    sns.countplot(x='CATEGORY*',data=data)
    st.pyplot(fig)

elif app_mode=='Count Vs Purpose':
    fig=plt.figure(figsize=(10,4))
    plt.title('Count Vs purpose')
    data['PURPOSE*'].value_counts()
    sns.countplot(y='PURPOSE*',data=data)
    st.pyplot(fig)
    
elif app_mode=='Miles Travelled':
    fig=plt.figure(figsize=(10,4))
    plt.title('Miles travelled by people')
    data['MILES*'].plot.hist()
    plt.xlabel('Miles')
    plt.ylabel('Frequency')
    st.pyplot(fig)
    
elif app_mode=='Trips VS Hours':
    fig=plt.figure(figsize=(10,4))
    hours = data['START_DATE*'].dt.hour.value_counts()
    hours.plot(kind='bar',color='red',figsize=(10,5))
    plt.xlabel('Hours')
    plt.ylabel('Frequency')
    plt.title('Number of trips Vs hours')
    st.pyplot(fig)

elif app_mode=='Trips Vs Week Days':
    fig=plt.figure(figsize=(10,4))
    days = data['WEEKDAY'].value_counts()
    days.plot(kind='barh', color='seagreen', figsize=(10,5))
    plt.xlabel('Frequency')
    plt.ylabel('Days')
    plt.title('Number of trips Vs days in a week')
    st.pyplot(fig)
    
elif app_mode=='Trips Vs Days of December':
    fig=plt.figure(figsize=(20,10))
    plt.title('Number of trip Vs Days of December')
    data['DAY'][data['MONTH']==12].value_counts().plot(kind='bar',figsize=(20,5),color='green')
    plt.xlabel('Days of December')
    plt.ylabel('Frequency')
    st.pyplot(fig)

elif app_mode=='Trips VS Month':
    fig=plt.figure(figsize=(20,10))
    plt.title('Number of trip Vs Month')
    data['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='black')
    st.pyplot(fig)

elif app_mode=='Count Vs Starting Point':
    fig=plt.figure(figsize=(20,10))
    plt.title('Count Vs Starting point')
    data['START*'].value_counts().plot(kind='bar',figsize=(25,10),color='blue')
    st.pyplot(fig)
    
elif app_mode=='Pickup Point Vs Frequency':
    fig=plt.figure(figsize=(20,10))
    months = data['START*'].value_counts().nlargest (10)
    months.plot(kind='barh', color='lightblue', figsize=(10,5))
    plt.xlabel('Frequency')
    plt.ylabel('Pickup point')
    plt.title('Pickup point Vs Frequency')
    st.pyplot(fig)
    
elif app_mode=='End Point Vs Frequency':
    fig=plt.figure(figsize=(20,10))
    months = data['STOP*'].value_counts().nlargest (10)
    months.plot(kind='barh', color='lightgreen', figsize=(10,5))
    plt.xlabel('Frequency')
    plt.ylabel('End point')
    plt.title('End point Vs Frequency')
    st.pyplot(fig)
    
elif app_mode=='Purpose':
    fig=plt.figure(figsize=(10,4))
    purpose = data.groupby('PURPOSE*').mean()
    purpose.plot(kind = 'barh',figsize=(15,5))
    st.pyplot(fig)