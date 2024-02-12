# RAC Data Downloader
## General Use Guidelines

Before running the script, ensure you meet a few basic requirements to guarantee correct execution. This is especially important if you are not using an Integrated Development Environment (IDE) like Jupyter or VSCode. Python 3.9 or higher must be installed to run the `.py` file successfully. Information on the data categories available for download is provided at the bottom of this README.

## Requirements

- **RAC_API_Sheet.csv**: This file must be located in the same directory as the `.py` file. It contains the current API keys, data descriptions, and source information.
- **Customization**: You can adjust the description and source information within `RAC_API_Sheet.csv` to suit your needs, provided a valid API key is used. The default values are accurate as of publishing but may need updating if the RAC Foundation changes their web links.
- **Modifying Data Categories**: To exclude a dataset from the download list, simply delete its row from `RAC_API_Sheet.csv`.

## How to Run

Execute the `rac_datadownload.py` file via the command line to start the data collection process. This script generates individual CSV files for each API key provided and compiles an Excel (.xlsx) file with all information allocated to separate sheets.

- **Excel Sheet Names**: Correspond to the descriptions found in `RAC_API_Sheet.csv`.
- **CSV File Naming**: The data source from `RAC_API_Sheet.csv` precedes the description in the filename, separated by an underscore (`_`), e.g., `RAC_FuelPrice.csv`.

## Data Categories Available

- FuelPumpPrice
- WholesaleFuel
- MotoringCost
- TravelCost
- EUDieselPrice
- EUPetrolPrice
- UKFuelConsumption
- FuelDutyMonthly
- FuelDutyAnnual
- UKVehicleTax
- UKPumpPriceTax
- UKTotalEVs
- UKTopTenEVs
- OilMarketPrice
- GreenFleetIndex
- FillingUpCost

## Installation Commands
```python
pip install pandas
pip install requests
pip install openpyxl
```

    
## Libraries used within RAC data downloader:
```python
from timeit import default_timer as timer
import sys
import os.path
import requests
import pandas as pd 
```