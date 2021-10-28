# Automated Trading using python

Setting up work environment

The easiest way to get started is by installing Anaconda. Anaconda is a distribution of Python, and it offers different IDEs like Spyder, Jupyter, __, ___ etc

Installing Quandl

Quandl will help us in retrieving the historical data of the stock. To ninstall quandl type the below command in the terminal – 

pip install quandl

After the packages have been imported, we will extract data from Quandl, using the API key.

qd.ApiConfig.api_key = "<API key>”
