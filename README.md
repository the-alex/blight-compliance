# blight-compliance


Forked version of starter script repo for [https://inclass.kaggle.com/c/detroit-blight-ticket-compliance](MDST Blight Ticket Compliance Challenge)

#### To run `starter_script.py`

- Make a data directory: `mkdir data`
- Download `train.csv` and `test.csv` from the Kaggle page into `data`
- Run the script: `python starter_script.py`
- Submit the benchmark submission: `data/submission_RF_R.csv`

#### To run `starter_heatmap.py`

- Make a data directory: `mkdir data`
- Download `addresses.csv` and `latlons.csv` from the Kaggle page into `data`
- Run the script: `python starter_heatmap.py`
- Open in your browser `data/blight_tickets.html` 



## Feature Wish List

Parcel Dataset has a lot of useful features. Could join on google_addr
- SalePrice
- IsImproved: If anything has been built on it (jared)
- SEV: Sate equalized [home] value
- TotSqFt: Size of property
- TpState: State of the tax payer's residence. Could be useful?
- PropClass


Lat/Long features to generate
- Distance from a school
- Distance from a Chruch

Census
- Median income
- USPS Vacency


Basic (in stock data)
- BOOL: Does violator/violation address match property address?
-
