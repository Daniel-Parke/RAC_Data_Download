# RAC Data Downloader
## General Use Guidelines

This script is designed to download historical data from the RAC Foundation website, allowing the user to add/remove required datasets by updating `RAC_API_Sheet.csv` sheet.

## How to Run

Execute the `rac_datadownload.py` file via the command line to start the data collection process. This script generates individual CSV files for each API key provided and compiles an Excel (.xlsx) file with all information allocated to separate sheets.

Before running the program, ensure you meet the basic requirements to ensure its correct execution. If you are not using an IDE like Jupyter or VSCode, then remember to install Python 3.9 or higher first. Run the .py file in your terminal to start the process, assuming you meet the requirements listed below.

## Requirements

- **RAC_API_Sheet.csv**: This file must be located in the same directory as the `.py` file. It contains the current API keys, data descriptions, and source information.
- **Customization**: You can adjust the description and source information within `RAC_API_Sheet.csv` to suit your needs, provided a valid API key is used. The default values are accurate as of publishing but may need updating if the RAC Foundation changes their web links.
- **Modifying Data Categories**: To exclude a dataset from the download list, simply delete its row from `RAC_API_Sheet.csv`.


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
pip install openpyxl
pip install xlsxwriter
pip install httpx
pip install backoff
```

    
## Libraries used within RAC data downloader:
```python
import asyncio
import os
import sys
from timeit import default_timer as timer
import httpx
import pandas as pd
from backoff import on_exception, expo
```

![WiseWattage](https://i.imgur.com/Y7oMz2Y.png)