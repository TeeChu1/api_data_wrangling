#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[3]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = '2Q2RKxs4SsH8xsRgisUd'


# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/ ).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# In[4]:


# First, import the relevant modules
import requests
import json


# Note: API's can change a bit with each version, for this exercise it is reccomended to use the "V3" quandl api at `https://www.quandl.com/api/v3/`

# In[10]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
url = 'https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?api_key='+API_KEY\
+'&start_date=2023-11-8&end_date=2023-11-8'
r = requests.get(url)
r.status_code


# In[11]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
json_data = r.json()
print(json_data['dataset_data']['data'])


# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[15]:


url = 'https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?api_key='+API_KEY\
+'&start_date=2017-01-01&end_date=2017-12-31'
r = requests.get(url)


# In[16]:


json_data = r.json()


# In[13]:


json_data['dataset_data']['column_names']


# In[20]:


open_price = [col[1] for col in json_data['dataset_data']['data'] if col[1] != None]
max_open_price = max(open_price)
min_open_price = min(open_price)
print("The highest opening price was ", max_open_price)
print("The highest lowest price was ",min_open_price)


# In[21]:


change = [col[2]-col[3] for col in json_data['dataset_data']['data'] if col[2:3] != None]
big_change = round(max(change), 2)
print("The largest change in a single day was",big_change)


# In[24]:


close_price = [col[4] for col in json_data['dataset_data']['data'] if col[4] != None]
diff = [x - close_price[i-1] for i,x in enumerate(close_price)][1:]
plus_change = [abs(num) for num in diff]
close_diff = str(round(max(plus_change), 2))
print("The largest change in closing price between two days was ",close_diff)


# In[25]:


daily_volume = [col[6] for col in json_data['dataset_data']['data'] if col[6] != None]
avg_daily_volume = round(sum(daily_volume) / len(daily_volume), 1)
print('The average daily trading volume was ', avg_daily_volume)


# In[ ]:




