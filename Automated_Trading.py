import pandas as pd
import quandl as qd
  
qd.ApiConfig.api_key = "1234567890"
  
msft_data = qd.get("EOD/MSFT",
                   start_date="2010-01-01",
                   end_date="2020-01-01")
msft_data.head()
