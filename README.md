# Fetch Rewards Coding Exercise - Analytics Engineer

## Introduction
This repository contains my submission for the Fetch Rewards Coding Exercise for the Analytics Engineer position. The exercise involves reviewing unstructured JSON data, diagramming a structured relational data model for Data Warehouse, generating SQL queries to answer business questions, evaluating data quality issues, and communicating findings with stakeholders.



# Task 1

The proposed data warehouse design aims to create an efficient and scalable solution for storing and analyzing receipt, user, and brand data. By utilizing a star schema approach with fact and dimension tables, 
this design enables fast querying, easy data integration, and support for complex analytics.
### Fact Tables
fact_receipts: This table stores transactional data related to receipts, including key metrics such as total spent, points earned, and purchased item count. It also contains foreign keys to link to relevant dimension tables like dim_users and dim_dates.
fact_receipt_items: This table provides a granular level of detail for each item purchased in a receipt. It includes information like quantity, price, and discount, and links to the fact_receipts table and dimension tables dim_brands and dim_products.
### Dimension Tables
dim_users: Stores user information like state, created date, last login, and active status. It includes effective date ranges to handle slowly changing dimensions.
dim_brands: Contains brand details such as brand code, name, barcode, and top brand flag. It links to the dim_categories and dim_cpg tables.
dim_categories: Stores category information with a self-referencing relationship to handle category hierarchies.
dim_cpg: Provides details about the consumer packaged goods (CPG) companies.
dim_products: Stores product information including name, description, price, and foreign keys to dim_brands and dim_categories.
dim_dates: Acts as a date dimension table to enable easy date-based analysis and aggregation at different time granularities.

### Relationships
The fact tables are connected to the dimension tables through foreign key relationships:
fact_receipts links to dim_users and dim_dates
fact_receipt_items links to fact_receipts, dim_brands, and dim_products
dim_brands links to dim_categories and dim_cpg
dim_products links to dim_brands and dim_categories
dim_categories has a self-referencing relationship for parent-child hierarchy
This star schema design allows for efficient querying and easy understanding of the data relationships.
### Benefits
Improved Decision-Making: By consolidating data from multiple sources into a single, coherent framework, this design enables informed, data-driven decision making.
Better Business Intelligence: The organized structure facilitates faster reporting, analysis, and trend identification across the organization.
Scalability: The design can accommodate growth in data volume and complexity, ensuring the data warehouse remains future-proof.
Flexibility: The dimensional modeling approach allows for easy addition of new data sources and adaptability to changing business requirements.
Enhanced Data Quality: By integrating and cleansing data from various sources, the data warehouse ensures consistency and reduces errors.
You can view the detailed ER diagram and explanation in the er_diagram.html file.
 ![Screenshot 2024-06-19 203023](https://github.com/hvaria/fetch_assesment/assets/98721412/8d9bd98e-3803-45b4-ae01-bf11ed57ce6a)


# Task 2
## Business Questions
What are the top 5 brands by receipts scanned for the most recent month?
File = top5.sql

When considering average spend from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
File = average_spend.sql


# Task 3
## Data Quality Evaluation

Missing Values:

Receipts Data: bonusPointsEarned, bonusPointsEarnedReason, finishedDate, pointsAwardedDate, pointsEarned, purchaseDate, purchasedItemCount, rewardsReceiptItemList, totalSpent.
Users Data: lastLogin, signUpSource, state.
Brands Data: category, categoryCode, topBrand, brandCode.
Duplicate Records:

Receipts Data: 586 duplicates.
Users Data: 475 duplicates.
Brands Data: No duplicates.
Inconsistent Date Formats:

Receipts Data: finishedDate, pointsAwardedDate, purchaseDate.
Users Data: Consistent.
Outliers/Invalid Values:

Receipts Data: purchasedItemCount ranges from 0 to 689, totalSpent ranges from 0.0 to 4721.95.
Users Data: Unexpected role values like 'fetch-staff'.
Brands Data: topBrand has 0, NaN, and 1 values.
Referential Integrity:

Receipts Data: 1119 receipts with userId not in Users dataset.
Brands Data: 1167 brands with cpg not in Brands dataset.

# Task 4 

## Email

Hey,
I wanted to give you a quick update on the data quality assessment I've been working on for our upcoming analysis project. I've been digging into the receipts, users, and brands datasets using Python and Pandas, and I've uncovered a few issues that we should tackle before moving forward.

Here's a summary of what I found:
Missing Values: All three datasets have some missing information in different columns. For example, the receipts data is missing details about bonus points, purchase details, and totals. We'll need to figure out how to handle these gaps, whether that's filling them in with reasonable estimates or leaving out the incomplete records.
Duplicate Records: I spotted a pretty significant number of duplicate records in the receipts (586) and users (475) datasets based on the unique columns. We should come up with a plan for dealing with these duplicates, keeping in mind how it might affect our analysis.
Inconsistent Date Formats: The date columns in the receipts dataset (finishedDate, pointsAwardedDate, purchaseDate) have different formats. If we standardize these, it'll be much easier to analyze the data across different time periods.
Potential Outliers: Some of the numeric columns in the receipts data, like purchasedItemCount and totalSpent, have really wide ranges that suggest there might be outliers. We should take a closer look to determine if these are valid data points or errors that need to be fixed.
Unexpected Categorical Values: I noticed some unexpected values in the categorical columns. For instance, the role column in the users dataset has 'fetch-staff' in addition to the expected 'consumer' value. We need to clarify what these values mean and decide how to handle them.
Referential Integrity Issues: There are some inconsistencies between the datasets that go against referential integrity. Some receipts have userIds that don't exist in the users dataset, and some brands have cpg values that don't match any brand _id. We need to investigate these discrepancies and make sure the relationships between the datasets are valid.

To resolve these data quality issues, it would be helpful to have more information on:
The expected values and formats for each column
How to handle missing data (e.g., imputation methods, exclusion criteria)
The correct relationships between the datasets (e.g., foreign key mappings)
Business rules for identifying and handling outliers and invalid data
Additionally, to optimize the data assets we're creating, it would be great to know:
The specific questions we're trying to answer with this data
The expected volume and growth rate of the data
Any additional data sources that could enrich our analysis
Regarding performance and scaling, I think the data volume might increase quite a bit over time. To get ahead of this, we should consider:
Optimizing our data processing scripts for efficiency
Using tools like Apache Spark for large-scale data processing
Implementing data partitioning and indexing strategies to improve query performance
Setting up a data pipeline to handle incremental updates and real-time data ingestion
Let me know if you have any questions or if there's anything else I can help with. I'm looking forward to discussing these findings with you and the team!

Best,
Himanshu
