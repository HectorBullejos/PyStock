import requests
import pandas as pd
import keyring
import matplotlib.pyplot as plt
from datetime import datetime
from iexfinance.stocks import Stock, get_historical_data

service_id = "iex"
username = "bullesen1"

credentials = keyring.get_credential(service_id, None)
if credentials is not None:
    username = credentials.username  # example_username
    password = credentials.password  # example_password




mykey = password
spy = Stock("SPY", output_format='pandas', token= mykey)

print(spy.get_quote())



start = datetime(2020, 9, 18)
end = datetime(2022, 9, 24)

df= get_historical_data("BTC",start,end,output_format = 'pandas', token=mykey)
filepath = 'out.csv'

df.to_csv(filepath)
print(df.head(), df.tail()  )
df.plot()
plt.show()