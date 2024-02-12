""" Import functions and libraries required for functionality. """
from timeit import default_timer as timer
import sys
import os  # Adjusted import for using os.makedirs
import requests
import pandas as pd

# Start Timer.
start = timer()

def main():
    """Main structure calling requested functions from below."""
    print("")
    data = get_info()
    excel = get_data(data)
    create_excel(excel)

    # End Timer and calculate runtime.
    end = timer()
    total_time = end - start
    print("")
    print(f"This script took approx. {round(total_time, 2)} seconds to complete.")
    print("********************************************************")
    print("")

def get_info():
    """Get information for API location, data source, and file name to be saved.
    Return this data to be used later."""
    try:
        data = pd.read_csv("RAC_API_Sheet.csv")
        return data
    except FileNotFoundError:
        print("********************************************************")
        sys.exit("Could not retrieve information from CSV file, no file was found.")
    except Exception:  # pylint: disable=broad-exception-caught
        print("********************************************************")
        sys.exit("Could not retrieve information from CSV file.")

def get_data(data):
    """Loop n times for all entries within data list, and allocate variables at location[i].
    Save this to separate CSV file for each entry found in "data" dictionary."""
    # Ensure the directory exists before proceeding
    os.makedirs("Downloaded_RAC_Data", exist_ok=True)  # Create the directory if it doesn't exist

    exdf = []
    exname = []
    excel = [exdf, exname]

    for i in range(len(data)):
        try:
            source = data["Data Source"][i]
            desc = data["Description"][i]
            api = data["API Key"][i]

            req = requests.get(api, timeout=10)
            response = req.json()
            result = response["values"]
            datafr = pd.DataFrame(result)
            exdf.append(datafr)
            exname.append(desc)

            # Save data to CSV file
            csv_path = os.path.join("Downloaded_RAC_Data", f"{source}_{desc}.csv")
            datafr.to_csv(csv_path, index=False, header=False)

            print(f"{i+1}. Download of {desc} Data was successful.")
        except requests.RequestException:
            print("********************************************************")
            print(f"Request Exception Error, could not download {desc} from API source.")
            print("********************************************************")
        except (KeyError, NameError):
            print("********************************************************")
            print(f"Could not find variable or dictionary value required to save {desc} CSV file.")
            print("********************************************************")
        except Exception:  # pylint: disable=broad-exception-caught
            print("********************************************************")
            print(f"Could not save {desc} CSV file.")
            print("********************************************************")

    print("")
    return excel

def create_excel(excel):
    """Create Excel spreadsheet from all data collected in program, saving each
    into an individual sheet within the excel file."""
    # Ensure the directory exists before proceeding
    os.makedirs("Downloaded_RAC_Data", exist_ok=True)  # Reaffirmed for clarity, but could be omitted here as it's already ensured in get_data

    with pd.ExcelWriter(os.path.join("Downloaded_RAC_Data", "All_Data.xlsx")) as writer:
        try:
            for i, data in enumerate(excel[0]):
                data.to_excel(writer, sheet_name=f"{excel[1][i]}", index=False, header=False)
            print("Excel sheet containing all data was successfully saved.")
        except (KeyError, NameError):
            print("********************************************************")
            print("Could not find variable or dictionary/list value required to save Excel file.")
            print("********************************************************")
        except Exception:  # pylint: disable=broad-exception-caught
            print("********************************************************")
            print("Could not save Excel file.")
            print("********************************************************")

if __name__ == "__main__":
    main()
