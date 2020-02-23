# Import the libraries
import OpenBlender
import pandas as pd
import json

# get my token
import os, glob
    # you need to create a folder token and put the token in the textfile
with open("credentials/mytoken.txt", "r", encoding="utf-8") as token:
    for line in token:
        myToken = line

# Specify the action
action = 'API_getObservationsFromDataset'
# Specify your Token and 'Apple Inc. Price' id_dataset
parameters = { 
      'token': myToken,
      'id_dataset':'5d4c39d09516290b01c8307b',
      'date_filter':{"start_date":"2017-01-01T06:00:00.000Z",
                     "end_date":"2020-02-09T06:00:00.000Z"}
}
# Pull the data into a Pandas Dataframe
df = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)

print(df.head())