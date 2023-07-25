import pandas as pd
import numpy as np
import tensorflow as tf
import mlflow
import mlflow.tensorflow

# Step 1: Start the MLflow run
mlflow.start_run()


# Step 2: Read Data from Parquet File
parquet_file_path = "../lakehouse/storage/receipt-json-delta/"
df = pd.read_parquet(parquet_file_path)

# Preprocess the data and split into features (X) and target (y)
# Assuming your data has a column 'target' for the target variable
X = df.drop(columns=['valid_line']).values
y = df['valid_line'].values

# Split the data into training and validation sets
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 3: Define the Model
model = tf.keras.Sequential([
    # Define your CNN layers here (or any other architecture)
    # Example:
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])


# Step 4: Compile and Train the Model
num_epochs = 10
batch_size = 32

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=num_epochs, batch_size=batch_size, validation_data=(X_val, y_val))


# Step 5: Log metrics and hyperparameters to MLflow
mlflow.tensorflow.autolog()
mlflow.log_param("num_epochs", num_epochs)
mlflow.log_param("batch_size", batch_size)


# Step 6: Save the Model
model.save("binary_classification_model.h5")


# Step 7: End the MLflow run
mlflow.end_run()
