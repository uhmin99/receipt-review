# Receipt Review Project

Receipt Review is a project inspired by Naver Receipt Review system, built as a demonstration of implementing a Lakehouse architecture. The main objective of this project is to showcase the usage of Delta Lake and Apache Spark to ingest and manage data, MLFlow for Machine Learning Operations (MLOps), and Apache NiFi for ETL and Business Intelligence (BI). The project utilizes the "CORD: A Consolidated Receipt Dataset for Post-OCR Parsing" dataset for analysis.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Data Ingestion and Lakehouse](#data-ingestion-and-lakehouse)
- [Machine Learning Operations (MLOps)](#machine-learning-operations-mlops)
- [ETL and Business Intelligence (BI)](#etl-and-business-intelligence-bi)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Receipt Review project aims to create a system similar to Naver Receipt Review. It involves the processing of receipt data and implementing an end-to-end Lakehouse architecture for data storage, management, machine learning, ETL, and BI. The project relies on various technologies and frameworks to achieve these objectives, including Delta Lake, Apache Spark, MLFlow, and Apache NiFi.

## Project Structure

The project is organized into the following directories:

- `MLOps`: Contains the Python scripts for MLFlow integration and managing the machine learning lifecycle.
- `data`: Includes the "CORD: A Consolidated Receipt Dataset for Post-OCR Parsing" data.
- `front-end`: Empty directory where Apache NiFi binaries need to be placed for ETL and BI tasks.
- `lakehouse`: Contains the scripts to set up Delta Lake and Apache Spark for data storage.

## Requirements

To run the Receipt Review project, you need the following software and dependencies:

- Apache Spark: For running Delta Lake and data processing.
- MLFlow: For managing the machine learning lifecycle.
- Apache NiFi: For ETL and Business Intelligence tasks.

Ensure you have these components installed and configured correctly before proceeding.

## Getting Started

To get started with the Receipt Review project, follow these steps:

1. Clone this repository to your local machine.
2. Set up Apache Spark and Delta Lake by running the scripts in the `lakehouse` directory.
3. Ingest the data from the "CORD: A Consolidated Receipt Dataset for Post-OCR Parsing" into Delta Lake using the scripts in the `lakehouse` directory.
4. Start MLFlow and configure it to work with the Lakehouse for machine learning operations.

## Data Ingestion and Lakehouse

The `lakehouse` directory contains the necessary scripts to set up Delta Lake and Apache Spark for data storage. The data from the "CORD" dataset can be ingested into the Lakehouse for further processing and analysis.

## Machine Learning Operations (MLOps)

For managing the machine learning lifecycle, MLFlow has been integrated into the project. The `MLOps` directory contains Python scripts for MLFlow integration, including training and tracking machine learning models using data from the Lakehouse.

## ETL and Business Intelligence (BI)

The `front-end` directory requires Apache NiFi binaries to be placed for ETL and BI tasks. Apache NiFi can be used to perform ETL operations on the data stored in the Lakehouse and enable Business Intelligence functionalities.

## Contributing

Contributions to the Receipt Review project are welcome! If you find any issues or want to add new features, feel free to create pull requests. Please follow the project's coding standards and guidelines when contributing.

## License

The Receipt Review project is open-source and is distributed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code according to the terms of the license.

---

With this README.md file, users and contributors will have a better understanding of the project, its objectives, and the required steps to set it up and run it successfully. Adjust the instructions and details as needed based on the actual implementation and requirements of your project.