#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from optionsparser import get_parameters
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Input config file")

args = parser.parse_args()

# Set optional parameters with default values and required parameter values with their type
defaults = {
           "xlabel"      : "Date of observation",
           "title"       : "Weather Observations",
           "start"       : "01/06/2021",
           "end"         : "01/10/2021",
           "output"      : "weather.png",
           "ylabel"      : "Temperature in Celsius",
           "data_column" : "T",
           }

required = {
           "input"  : str
           }

# now, parse the config file
parameters = get_parameters(args.input, required, defaults)

# load the data
weather = pd.read_csv(parameters.input,comment='#')

# define the start and end time for the plot
start_date=pd.to_datetime(parameters.start,dayfirst=True)
end_date=pd.to_datetime(parameters.end,dayfirst=True)

# The date format in the file is in a day-first format, which matplotlib does nto understand.
# so we need to convert it.
weather['Local time'] = pd.to_datetime(weather['Local time'],dayfirst=True)
# select the data
weather = weather[weather['Local time'].between(start_date,end_date)]


# Now, we have the data loaded, and adapted to our needs. So lets get plotting

# In[4]:


import matplotlib.pyplot as plt
# start the figure.
fig, ax = plt.subplots()
ax.plot(weather['Local time'], weather['T'])
# label the axes
ax.set_xlabel(parameters.xlabel)
ax.set_ylabel(parameters.ylabel)
ax.set_title(parameters.title)
# adjust the date labels, so that they look nicer
fig.autofmt_xdate()
# save the figure
fig.savefig(parameters.output)


# In[ ]:




