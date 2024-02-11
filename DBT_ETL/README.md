# Retail Data Analysis with DBT + Looker

## OVERVIEW

This project involves migrating retail database from PostgresDB into Google BigQuery. Using DBT, transform BigQuery dataset into analytical tables, further use these to build dashboard in Looker.

## Steps taken for Project
1. Setting up GCP Account and create project. 
    Then, install Google Cloud SDK : https://cloud.google.com/sdk/docs/install
    Downlaoad tar file
    tar -xzvf Downloads/google-cloud-cli-VERSION-darwin-x86_64.tar
    ./google-cloud-sdk/install.sh
    gcloud init
    Login with gcp account and pick up the project created above.

2. Migrate Database into BigQuery
    Creates CSV files of tables into CSV in specified path
    COPY (SELECT * from categories) 
    To '<path-to-dump-folder>/categories.csv' 
    With CSV HEADER;

    Create bucket in Google Storage: retail_db_bkt
    Copy dump folder into the retail_db_bkt:
    gsutil cp -r  <path-to-dump-folder>/dump_files gs://retail_db_bkt/retail_db/

    Create BigQuery Dataset Tables using CSV stored in Google Storage Bucket:
    bq mk <project-name>:<dataset-id>
    bq load --source_format=CSV --autodetect <project-name>:<dataset-id>.categories gs://retail_db_bkt/retail_db/dump_files/categories.csv

3. Build DBT Project over BigQuery Dataset
    Install DBT:

    Create DBT Project:

    Create Models, Test and Documentations

4. Create dashboard for analysis tables.

Connecting Looker with BigQuery involves a few steps to set up the integration. 
Looker is a business intelligence and data exploration platform, while BigQuery is a fully-managed, serverless
data warehouse provided by Google Cloud. 






## Folder Structure - retail_dbt


## Tech Stack
1. Python 3.x
2. PostgreSQL
3. DBT
4. gsutil 
5. Google Storage, BigQuery and Looker

### RESOURCES -
1. https://cloud.google.com/?authuser=2&hl=en ($300 or 90-day trial)
2. DBT Documentation + DBT fundamentals
3. 


ChatGPT
Designing a data warehouse involves creating a schema that optimizes for querying and reporting. Below is a possible design for your data warehouse tables based on the provided tables:

Data Insights:
Revenue by Category:
Analyze sales revenue by category over time to identify top-performing and underperforming categories.
Order Status Distribution:
Understand the distribution of order statuses (e.g., processing, shipped, delivered) to monitor the order fulfillment process.
Customer Purchase Behavior:
Analyze customer purchase patterns, such as the average order value, frequency of purchases, and customer lifetime value.
Product Performance:
Evaluate the performance of products based on sales, quantity sold, and revenue generated.
Customer Geography Analysis:
Explore customer distribution by geography to identify regions with the highest customer concentration.
Category Department Relationships:
Understand how categories are distributed across different departments and identify any dependencies.
Order Item Metrics:
Calculate metrics such as average quantity per order item, average subtotal, and average product price.
Customer Segmentation:
Segment customers based on various criteria such as purchase frequency, order value, and geography to tailor marketing strategies.

