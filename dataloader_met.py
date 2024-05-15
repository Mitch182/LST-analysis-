import pandas as pd 
from datetime import datetime 
from pathlib import Path 

def print_rows_removal(mask, reason):
    frac = mask.sum() / mask.shape[0]
    print(
        "[METdata] filtered out "
        f"{mask.sum()}/{mask.shape[0]} ({round(frac * 100, 2)}%) rows "
        f"where {reason}"
    )

def set_date_as_column(df, src_col="Timestamps"):
    timestamp_is_index = "Timestamps" not in df and isinstance(
        df.index, pd.DatetimeIndex
    )

    if timestamp_is_index:
        timestamps = df.index.to_series()
    else:
        timestamps = df[src_col]

    # create date column
    df["date"] = timestamps.dt.date


class METdataloader(object):

    def __init__(self):
        pass

    def _read_csv(self, fpath):
        df = pd.read_csv(fpath, skiprows = 2)

        #add station identifier to column 
        parts = fpath.name.split('-')
        print(parts)
        name_part = parts[0][4:8]
        print(name_part)
        df["src_fname"] = name_part

        return df 
    
    def _preprocess_data(self, df):

        df["Timestamps"] = pd.to_datetime(df["Timestamps"])
        print(df.dtypes)
        # Filter the DataFrame to include only data between 2018 and 2022
        between_2018_2022 = (df["Timestamps"].dt.year >= 2018) & (df["Timestamps"].dt.year <= 2022)
        df = df[between_2018_2022]

        # Print rows that were removed
        print_rows_removal(
            ~between_2018_2022, f"timestamp is not between 2018 and 2022"
        )  

        # it's a UTC timestamp, and we're UTC+1
        df["Timestamps"] = df["Timestamps"] + pd.DateOffset(hours=1)

        set_date_as_column(df, src_col= 'Timestamps')

         # set the timestamp as the index
        df = df.set_index("Timestamps").sort_index()

        return df 
    
    
    def load_data(self, experiment_name, sensor_name):
        if isinstance(sensor_name, (list, tuple)):
            return self._load_data_for_multiple_sensors(
                experiment_name, sensor_name
            )

        print(f"[MITDataLoader] loading {experiment_name}/{sensor_name}")
        data_dir = WEATHER_DATA_DIR / experiment_name / sensor_name
        if not data_dir.exists():
            raise ValueError(
                "the directory for the given experiment and device does not exist"
            )
        # dfs = [self._read_csv(fpath) for fpath in data_dir.glob("**/*.CSV")]

        # Exclude files with 'raw' in the filename
        dfs = []
        for fpath in data_dir.glob("**/*.csv"):
            if "raw" not in fpath.name.lower():
                df = self._read_csv(fpath)
                if df is not None:  # Check if the DataFrame is not None
                    dfs.append(df)

        df = pd.concat(dfs)
        df = self._preprocess_data(df)
        return df
    
    def _load_data_for_multiple_sensors(self, experiment_name, sensor_names):
        df = pd.concat(
            {
                name: self.load_data(experiment_name, name)
                for name in sensor_names
            },
            names=["sensor_name", "timestamp"],
        )
        return df


WEATHER_DATA_DIR = Path("/home/mitch182/code/wsl/AAMS_5mindata")
experiment_name = "AAMS_5mindata"
sensor_name = "All-5G0D2194(5G0D2194)-1667305005"
loader= METdataloader()


df = loader.load_data(experiment_name, sensor_name)

df.to_csv("/home/mitch182/code/wsl/AAMS_5mindata/clean_weather.csv")

   #TODO: 
   # - Write load data function
   # - add filters to elimate faltty measurements
   # - lit 
    


    