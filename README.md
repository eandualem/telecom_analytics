# Telecom Analytics

**Table of content**

- [Telecom Analytics](#telecom-analytics)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Data](#data)
  - [Features](#features)
    - [Data Exploration](#data-exploration)
      - [1.0_preprocessing.ipynb:](#10_preprocessingipynb)
      - [1.01_outliers.ipynb](#101_outliersipynb)
      - [1.1_overview:](#11_overview)
      - [1.2_data_analysis:](#12_data_analysis)
    - [Scripts](#scripts)
    - [Test](#test)
    - [Travis CI](#travis-ci)
    - [Dashboard](#dashboard)

## Overview
This repository analyses users’ experience, engagement, and satisfaction to check for growth opportunities in TellCo, a mobile service provider.

## Requirements
Python 3.5 and above, Pip and MYSQL
## Install
```
git clone https://github.com/eandualem/telecom_analytics.git
cd telecom_analytics
pip install -r requirements.txt
```

## Data
  - The data used in the project is generated automatically by TellCo systems.
  - The data is [here](https://drive.google.com/file/d/13w8Ic6iX-phtcKCGAIBd5k5BqYiPce3N/view?usp=sharing) - extracted from a month of aggregated data on xDR. 
  - The features described can be found [here](https://docs.google.com/spreadsheets/d/1pcNqeUeIph6xAQzlI54KCvi8HM91SUNeeDbdOq3rvbE/edit?usp=sharing).

## Features

### Data Exploration
  - Data exploration is done in 4 notebooks

#### 1.0_preprocessing.ipynb:
  - Here I have cleaned the original data by
    - renaming column labels
    - removing duplicates
    - handle null values
    - convert data types

#### 1.01_outliers.ipynb
  - Here I have calculated outliers in each column and their percentages
  - If the percentage is small i have dropped the rows with outliers
  - For columns with a larger percentage of outliers, I have replaced them with values using the IQR.
 - Then I have selected columns for further analysis and saved them in clean_data.csv. 

#### 1.1_overview:
  - I have done task 1.1 here.

#### 1.2_data_analysis:
  - I have done task 1.2 here.

### Scripts
 - All the scripts used by the notebooks are inside the scripts folder.

### Test
 - Tests for the scripts are inside the tests folder.

### Travis CI
  - In the process.

### Dashboard
  - 
