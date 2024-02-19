import asyncio
import os
import sys
from timeit import default_timer as timer
import httpx
import pandas as pd
from backoff import on_exception, expo

# Start Timer
start = timer()

async def main():
    """Main function to orchestrate the script execution."""
    os.makedirs("Downloaded_RAC_Data", exist_ok=True)
    data = get_info()
    excel_data, excel_names = await get_data(data)
    await create_excel(excel_data, excel_names)  # Save merged data to Excel

    # End Timer and calculate runtime
    end = timer()
    total_time = end - start
    print(f"\nThis script took approx. {round(total_time, 2)} seconds to complete.\n")

async def fetch_data(session, api, semaphore, desc, source):
    """Asynchronous request with semaphore and exponential backoff."""
    async with semaphore:
        response = await session.get(api, timeout=10)
        response.raise_for_status()  # Ensure a valid response
        data = response.json()
        result = data["values"]
        df = pd.DataFrame(result)

        # Save individual CSV file
        csv_path = os.path.join("Downloaded_RAC_Data", f"{source}_{desc}.csv")
        df.to_csv(csv_path, index=False)
        print(f"Download of {desc} Data was successful and saved to CSV.")

        return df, desc

@on_exception(expo, httpx.HTTPError, max_time=60)
async def get_data(data):
    """Asynchronous loop over data entries, fetching, saving data, and preparing for Excel."""
    semaphore = asyncio.Semaphore(5)  # Controls concurrency level
    excel_data = []
    excel_names = []

    async with httpx.AsyncClient() as session:
        tasks = [
            fetch_data(session, row["API Key"], semaphore, row["Description"], row["Data Source"])
            for _, row in data.iterrows()
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results for Excel
        for result in results:
            if isinstance(result, tuple):
                df, desc = result
                excel_data.append(df)
                excel_names.append(desc)

    return excel_data, excel_names

    return excel_data, excel_names

def get_info():
    """Get information for API location, data source, and file name."""
    try:
        return pd.read_csv("RAC_API_Sheet.csv")
    except FileNotFoundError:
        sys.exit("Could not retrieve information from CSV file, no file was found.")
    except Exception as e:
        sys.exit(f"Could not retrieve information from CSV file: {e}")

async def create_excel(excel_data, excel_names):
    """Create Excel spreadsheet from all collected data."""
    with pd.ExcelWriter(os.path.join("Downloaded_RAC_Data", "All_Data.xlsx"), engine='xlsxwriter') as writer:
        for i, data in enumerate(excel_data):
            # Excel sheet names are limited to 31 characters
            sheet_name = excel_names[i][:31]
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Excel sheet containing all data was successfully saved.")

if __name__ == "__main__":
    asyncio.run(main())
