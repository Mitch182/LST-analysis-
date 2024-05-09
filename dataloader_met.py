import pandas as pd 
from datetime import datetime 

def print_rows_removal(mask, reason):
    frac = mask.sum() / mask.shape[0]
    print(
        "[METdata] filtered out "
        f"{mask.sum()}/{mask.shape[0]} ({round(frac * 100, 2)}%) rows "
        f"where {reason}"
    )

class METdataloarder(object):

    def __init__(self):
        pass

    def _read_csv(self, fpath):
        df = pd.read_csv(fpath, skiprows = 2)

        #add station identifier to column 
        parts = fpath.name.split('-')
        name_part = parts[1][:4]
        df["src_fname"] = name_part

        return df 
    
    def _preprocess_data(self, df):

        df["Timestamps"] = pd.to_datetime(df["Timestamps"], unit="m")


    # Get the current year
    this_year = datetime.now().year

    # Filter the DataFrame to include only data between 2018 and 2022
    between_2018_2022 = (df["timestamp"].dt.year >= 2018) & (df["timestamp"].dt.year <= 2022)
    df = df[between_2018_2022]

    # Print rows that were removed
    print_rows_removal(
        ~between_2018_2022, f"timestamp is not between 2018 and 2022"
    )
    

    


    