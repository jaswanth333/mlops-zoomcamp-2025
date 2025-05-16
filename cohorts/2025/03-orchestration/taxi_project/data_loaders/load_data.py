import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Simple data loader to read a Parquet file.
    Make sure the file path is correct relative to your Mage project.
    """
    # Path to your parquet file inside the Mage project folder
    file_path = 'yellow_tripdata_2023-01.parquet'

    # Load the parquet file into a pandas DataFrame
    df = pd.read_parquet(file_path)

    df.head()

    # Return the DataFrame to pass it to next Mage block
    return df

