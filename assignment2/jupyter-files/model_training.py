#!/usr/bin/env python
# coding: utf-8

# # Model Training 
# This section will train the BERT model with the cleaned dataset.
# 
# ### Import required Library

# ### Download sentence transformer and encoder for BERT

# In[12]:


# Importing all required libraries
from bertopic import BERTopic
import pandas as pd 
import os
import pickle


# ### Import the cleaned dataset for BERT

# In[13]:


DATADIR = f"{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}/dataset"
cleaned_df = pd.read_csv(f"{DATADIR}/cleaned_tweets.csv")

cleaned_df.head()


# ### Train the BERT model
# This section will train the bert model if it does not exist. If not it will import the exisiting model to save time. 

# In[21]:


MODELDIR = f"{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}/model"
model_path = f"{MODELDIR}/bert"

def train_model():
    if not os.path.exists(MODELDIR):
        os.makedirs(MODELDIR)
    bert_model = BERTopic(verbose=True)
    tweets = cleaned_df['cleaned_tweet'].to_list()
    topics, probabilities = bert_model.fit_transform(tweets)
    bert_model.save(f"{MODELDIR}/bert", serialization="pickle")
    # save_model(bert_model, "bert")

if os.path.isfile(model_path):
    bert_model = BERTopic.load(model_path)
else: 
    train_model()


# ### View Bert topic information

# In[15]:


bert_model.get_topic_info()


# In[16]:


bert_model.get_topic(0)


# In[17]:


# Show the size of topics in descending order
bert_model.get_topic_freq().head()


# ### Visualisation for BERT model

# In[18]:


bert_model.visualize_topics()


# ### Visualise Terms 
# This method will show a few selected terms in bar chart format of the TF-IDF scores.

# In[19]:


bert_model.visualize_barchart()


# ### Visualise Topic Similarity 
# This method will visualise how similar certain topics are to each other using a heatmap.

# In[20]:


bert_model.visualize_heatmap()

