# binalysis
Trade Analysis based on Binance API

# Scope 
Present scope is limited to testing hypothesis based on tick data. 

1. <i>Statistical performance of <b></i>order book weighted average price</b> <i>as a 
predictor of price fluctuations</i>. At present the code uses simple 
visualisations to provide a feel. The next step would be to take a large sample to 
and define the metrics for success.


# Getting started

### Virtual Environment
Activate and setup Virtual Environments

Setup (https://docs.python-guide.org/dev/virtualenvs/)
```
$ pip install virtualenv # install virtualenv
$ virtualenv venv # create the folder 
$ source venv/bin/activate
```

Install requirements

```
$ pip install -r requirements.txt
```

### API Keys

As the tool is based on APIs to the Binance exchange, the user is expected to create 
API keys with the name <u>keys.json</u> in the main folder. The content should have 
the following format (exact key names).
```
{
  "api_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

