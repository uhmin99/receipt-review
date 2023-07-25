import os
import pandas as pd
import mlflow

mlflow.start_run()

# Read Data
data_folder = "../lakehouse/storage/receipt-image-delta"
parquet_files = [f for f in os.listdir(data_folder) if f.endswith('.parquet')]

# Read and concatenate data from all Parquet files into a single DataFrame
df_list = [pd.read_parquet(os.path.join(data_folder, f)) for f in parquet_files]
df = pd.concat(df_list, ignore_index=True)

# Log Metrics to MLflow
mlflow.log_metric("num_samples", df.shape[0])
mlflow.log_metric("num_features", df.shape[1])

mlflow.end_run()
