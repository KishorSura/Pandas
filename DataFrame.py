#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd


# In[98]:


df=pd.read_csv("C:/Users/DELL/Desktop/Book1.csv")


# In[99]:


df


# In[10]:


weather_data={
    "day":["01-01-2017","01-02-2017","01-03-2017","01-04-2017","01-05-2017","01-06-2017"],
    "temperature":[32,35,28,24,32,31],
    "windspeed":[6,7,2,7,4,2],
    "event":["Rain","Sunny","Snow","Snow","Rain","Sunny"]
}
df1=pd.DataFrame(weather_data)
df1


# In[32]:


#first two rows
df.head(2)


# In[33]:


#last row 
df.tail(1)


# In[34]:


#slicing 
df[2:4]


# In[36]:


#column names 
df.columns


# In[38]:


df.day


# In[40]:


df[["day","event"]]


# In[41]:


type(df["event"])


# In[43]:


df[["event","day","temperature"]]


# In[44]:


df["temperature"].max()


# In[45]:


df["temperature"].mean()


# In[46]:


df["temperature"].std()


# In[47]:


df.describe()


# In[48]:


df[df.temperature>32]


# In[50]:


df[df.temperature==df["temperature"].max()]


# In[51]:


df.index


# In[52]:


df.set_index("day")


# In[58]:


weather=[
    ("01-01-2017",32,6,"Rain"),
    ("01-02-2017",35,7,"Sunny"),
    ("01-03-2017",28,2,"Snow")
]
df=pd.DataFrame(weather,columns=["day","temperature","windspeed","event"])


# In[59]:


df


# In[61]:


weather=(
{"day":"01-01-2017","temperature":32,"windspeed":6,"event":'Rain'},
 {"day":"01-02-2017","temperature":35,"windspeed":7,"event":'Sunny'},
   {"day":"01-03-2017","temperature":28,"windspeed":2,"event":'Snow'}, 
)
df=pd.DataFrame(weather)


# In[62]:


df


# In[77]:


#missing heading
book1=pd.read_csv("C:/Users/DELL/Desktop/Book1.csv",header=None,names=["day","temperature","windspeed","event"])
df1=pd.DataFrame(book1)
df1


# In[78]:


#to write 
df.to_csv("new file",index=False)


# In[80]:


#only selected columns
df.to_csv("new file",columns=["day","temperature"],index=False)


# In[87]:


file=pd.read_csv("C:/Users/DELL/Desktop/Book2.csv",parse_dates=["day"])
df2=pd.DataFrame(file)


# In[88]:


df2


# In[91]:


type(df2.day[0])


# In[92]:


df2.set_index("day",inplace=True)


# In[93]:


df2


# In[96]:


new_df=df2.fillna(0)
new_df


# In[100]:


new_df=df2.fillna(
{ "temperature":0,
"windspeed":0,
"event":"no event"})
new_df


# In[102]:


new_df=df2.fillna(method="ffill")
new_df


# In[103]:


new_df=df2.fillna(method="bfill")
new_df


# In[105]:


new_df=df2.fillna(method="ffill",limit=1)
new_df


# In[106]:


new_df=df2.fillna(method="bfill",axis="columns")
new_df


# In[108]:


newdf=df2.interpolate(method="time")
newdf


# In[109]:


newdf=df2.dropna() 
newdf


# In[110]:


newdf=df2.dropna(how="all")
newdf


# In[111]:


newdf=df2.dropna(thresh=1)
newdf


# In[120]:


dt=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(dt)
df=df2.reindex(idx)
df


# In[121]:


dt=pd.date_range("1-1-2017","1-11-2017")
idx=pd.DatetimeIndex(dt)
df=df2.reindex(idx)
df


# In[ ]:




