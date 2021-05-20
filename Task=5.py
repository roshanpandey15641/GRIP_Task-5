#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Sports

# # The Sparks Foundation

# In[1]:


#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # load Data(Matches)

# In[2]:


df = pd.read_csv(r"matches.csv",encoding='latin')
df.head()


# In[3]:


df.shape


# In[6]:


df.keys().values


# In[7]:


#checking missing value
df.isnull().sum()


# In[12]:


plt.figure(figsize=(10,10))
sns.heatmap(df.isnull())
plt.show()


# In[9]:


df.drop(['umpire3'],axis=1,inplace=True)


# In[10]:


df[df.isnull().any(axis=1)]


# In[13]:


df.city.fillna('Dubai',inplace=True)
df.winner.fillna('Match Cancelled',inplace=True)
df.player_of_match.fillna('Match Cancelled',inplace=True)
df.umpire1.fillna('Anonymous',inplace=True)
df.umpire2.fillna('Anonymous',inplace=True)


# In[14]:


a=df["winner"]
c=a.value_counts()
b=pd.DataFrame({'Team':c.index,'Value':c.values})

plt.figure(figsize=(10,5))
sns.barplot(b["Team"],b["Value"])
plt.title("Most Wins")
plt.xticks(rotation=90)
plt.show()


# In[15]:


a=df["player_of_match"]
c=a.value_counts().head(20)
b=pd.DataFrame({'Team':c.index,'Value':c.values})

plt.figure(figsize=(10,5))
sns.barplot(b["Team"],b["Value"])
plt.title("Most Sucessful players")
plt.xticks(rotation=90)
plt.show()


# In[16]:


a=df['toss_winner']
b=a.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(b.index,b.values)
plt.xticks(rotation=90)
plt.title("Most Toss Winners")
plt.show()


# In[17]:


a=df['winner']
b=df['toss_winner']
c=a==b
d=pd.DataFrame({'winning after winning toss':a,'true/false':c})
e=d['winning after winning toss']
f=d['true/false']==True
g=e[f]
plt.figure(figsize=(10,5))
sns.countplot(g)
plt.title("Winners after winning the toss")
plt.xticks(rotation=90)
plt.show()


# In[18]:


a=df['winner']=='Mumbai Indians'
b=df['player_of_match']
c=b[a]
d=c.value_counts().head()
plt.figure(figsize=(10,5))
sns.barplot(d.index,d.values)
plt.title("Most Sucessful players in Most Winning team(Mumbai Indians)")
plt.xticks(rotation=90)
plt.show()


# In[19]:


bat_first=df[df['win_by_runs']!=0]
bat_first.head()


# In[20]:


a=bat_first['winner'].value_counts().head()
sns.barplot(a.index,a.values)
plt.xticks(rotation=90)
plt.title('Winner after batting first')
plt.show()


# In[21]:


a=bat_first['win_by_runs']
plt.hist(a)
plt.title('Distribution of runs')
plt.show()


# In[22]:


ball_first=df[df['win_by_wickets']!=0]
ball_first.head()


# In[23]:


a=ball_first['winner'].value_counts().head()
sns.barplot(a.index,a.values)
plt.title('Winners after balling first')
plt.xticks(rotation=90)
plt.show()


# In[24]:


a=ball_first['win_by_wickets']
plt.hist(a,bins=20)
plt.title('Win by wickets')
plt.show()


# # Data 2 (Deliveries)

# In[26]:


df2=pd.read_csv("deliveries.csv")
df2.head()


# In[27]:


a=df2['batsman'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(a.index,a.values)
plt.title("Most played batsman")
plt.show()


# In[28]:


a=df2['bowler'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(a.index,a.values)
plt.title("most played bowlers")
plt.show()


# In[29]:


a=df2['total_runs']>=6
b=df2['batsman']
c=b[a].value_counts().head()
plt.figure(figsize=(10,5))
sns.barplot(c.index,c.values)
plt.title("Players with most sixes")
plt.show()


# In[30]:


a=df2['dismissal_kind']=='bowled'
b=df2['bowler']
c=b[a].value_counts().head()
plt.figure(figsize=(10,5))
plt.title("bowlers who took most wickets")
sns.barplot(c.index,c.values)
plt.show()


# In[31]:


a=df2['dismissal_kind']=='caught'
b=df2['fielder']
c=b[a]
d=c.value_counts().head()
plt.figure(figsize=(10,5))
sns.barplot(d.index,d.values)
plt.title("Filders with most catches")
plt.show()


# In[32]:


a=df2['dismissal_kind']=='run out'
b=df2['fielder']
c=b[a]
d=c.value_counts().head()
plt.figure(figsize=(10,5))
sns.barplot(d.index,d.values)
plt.title("Fielders who took most wickets")
plt.show()


# In[33]:


a=df2['dismissal_kind']=='stumped'
b=df2['fielder']
c=b[a]
d=c.value_counts().head()
plt.figure(figsize=(10,5))
sns.barplot(d.index,d.values)
plt.title('Fielders who stumped most')
plt.show()


# In[ ]:




