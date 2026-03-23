# Customer Churn Analytics Warehouse (Amazon Redshift)

## Project Overview
This project builds a data warehouse solution using Amazon Redshift to analyze customer churn patterns for a telecom company.

The workflow includes:
- Data ingestion from Amazon S3
- Data warehouse design in Redshift
- Data loading using COPY command
- Analytical query execution
- Performance optimization

## Dataset
The project uses two datasets:
1. telecom_customer_churn.csv
    - Customer demographics
    - Services
    - Tenure
    - Charges
    - Churn status
2. telecom_zipcode_population.csv
    - Zip code
    - Population data
Dataset Link:
```
https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics
```
## Tech Stack Used

- Programming Language: Python
- Cloud Platform: AWS
- Services Used:
    - Amazon S3 (data storage)
    - Amazon Redshift (data warehouse)
    - AWS IAM (access control)
- Libraries:
    - boto3 (AWS SDK)
    - logging (monitoring)
    - python-dotenv (environment management)
- Tools:
    - VS Code
    - Git & GitHub

## Project Architecture
```
Local Dataset 
      ↓
Amazon S3 (Raw Storage) 
      ↓ 
Amazon Redshift (Staging Tables)    
      ↓ 
Analytical Table (customer_churn_analytics)
      ↓ 
SQL Analysis Queries 
      ↓ 
Insights & Reports
```

## Project Structure
```
customer-churn-analytics
|
|-- config/
|   |-- settings.py
|
|-- dataset/
|   |-- telecom_customer_churn.csv
|   |-- telecom_zipcode_population.csv
|
|-- document/
|   |-- configure_redshift.txt
|   |-- redshift.txt
|
|-- scripts/
|   |-- create_table.py
|   |-- customer_analytics.py
|   |-- customer_churn_analytics.py
|   |-- data_ingestion.py
|   |-- maintain_customer_churn_analytics.py
|   |-- upload_to_s3.py
|
|-- service/ 
|   |-- client.py
|   |-- redshift.py
|
|-- output/ 
|
|-- .env
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## How to Run
### Step 1: Clone Repository
Clone repository:
```
git clone https://github.com/vilas-kr/customer-churn-analytics.git
cd customer-churn-analytics
```

### 2 Install Python Dependencies
Install the required libraries for running the python script.
```
pip install -r requirements.txt
```

### 3 Configure AWS Credentials
Configure AWS CLI credentials.
```
aws configure
```
Provide:
```
AWS Access Key ID
AWS Secret Access Key
Region (example: ap-south-1)
Output format: json
```

### Step 4: Configure Environment Variables
Create .env file:
```
BUCKET_NAME = your_bucket
WORK_GROUP_NAME = work_group_name
DATABASE = 'telecom'
IAM_ROLE_ARN = your_iam_role
```
### Step 5: Create Redshift Serverless
Follow the detailed instructions in:
```
document/configure_redshift.txt
```
This step will create the redshift serverless 

### Step 6: Upload Data to S3
```
python scripts/upload_to_s3.py
```
Uploads CSV files to:
```
s3://<bucket>/raw/
```

### Step 7: Create Tables in Redshift
```
python scripts/create_table.py
```
Creates:
- staging tables
- analytics table

### Step 8: Load Data into Redshift
```
python scripts/data_ingestion.py
```
Uses COPY command to load data from S3

### Step 9: Build Analytical Table
```
python scripts/customer_churn_analytics.py
```
Joins datasets and inserts into final table

### Step 10: Run Analytics Queries
```
python scripts/customer_analytics.py
```
Outputs:
- churn rate
- top cities
- revenue loss
- etc

### Step 11: Optimize Redshift
```
python scripts/maintain_customer_churn_analytics.py
```
Runs:
- ANALYZE
- VACUUM

## Result & Insights
- Identified high churn rate segments
- Found cities with maximum churn
- Estimated revenue loss
- Analyzed customer density vs population

## Author
```
Name: Vilas K R
GitHub: https://github.com/vilas-kr
```