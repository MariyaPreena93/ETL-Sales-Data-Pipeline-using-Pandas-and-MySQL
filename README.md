# ETL Sales Data Pipeline using Pandas and MySQL

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, and MySQL.

The pipeline reads customer, order, and product data from CSV files, performs data cleansing and validation, generates sales analytics, exports cleaned datasets, and loads the final data into a MySQL database.

This project simulates a real-world ETL workflow commonly used in data engineering and analytics environments.

## Objectives

- Read data from multiple source files
- Remove duplicate customer records
- Handle missing values
- Validate product references in orders
- Identify invalid orders
- Merge datasets
- Calculate sales revenue
- Generate business reports
- Export cleaned data to CSV files
- Load processed data into MySQL

---

## Technologies Used

- Python 3.x
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL Workbench
---

## Source Files

### customers.csv

Contains customer information.

| Column |
|----------|
| customer_id |
| customer_name |
| city |
| email |

### products.csv

Contains product master data.

| Column |
|----------|
| product_id |
| product_name |
| category |
| price |

### orders.csv

Contains customer order transactions.

| Column |
|----------|
| order_id |
| customer_id |
| product_id |
| quantity |
| order_date |

---

## ETL Process

### Extract

Read source CSV files using Pandas.

```python
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
```

### Transform

#### Remove Duplicate Records

```python
cust = customers.drop_duplicates()
```
#### Remove Records with Missing Email
```python
cust = cust.dropna(subset=["email"])
```

#### Fill Missing City Values

```python
cust = cust.fillna({"city": "Windsor"})
```

#### Validate Product IDs

Identify invalid orders where Product ID does not exist in the Product Master.

```python
Invalid_orders = orders[
    ~orders["product_id"].isin(products["product_id"])
]
```

#### Merge Orders and Products

```python
sales = pd.merge(
    ordr,
    products,
    on="product_id",
    how="left"
)
```

#### Calculate Revenue

```python
sales["revenue"] = (
    sales["quantity"] * sales["price"]
)
```

---

## Business Reports Generated

### Total Revenue

Calculate total sales revenue.

### Revenue by Product

Generate product-wise revenue summary.

### Revenue by Customer

Generate customer-wise revenue summary.

### Top Selling Product

Identify the product with the highest quantity sold.

### ETL Summary

Generate summary statistics including:

- Customer Records
- Clean Customer Records
- Valid Orders
- Invalid Orders
- Total Revenue
- Top Selling Product

---

## Output Files

### clean_customer.csv
Contains cleaned customer data.

### sales_summary.csv
Contains processed sales data with calculated revenue.

### invalid_orders.csv
contains invalid orders
---

## Load to MySQL

The cleaned datasets are loaded into MySQL tables using SQLAlchemy.

```python
cust.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)

sales.to_sql(
    "sales",
    con=engine,
    if_exists="replace",
    index=False
)
```

---

## Sample Output

```text
Duplicate records removed: 1

No. of Invalid Orders: 1

Total Revenue: 7302

Top Selling Product: Notebook

----- Summary -----

Customer Records: 11
Clean Customer Records: 9
Invalid Orders: 1
Valid Orders: 14
Total Revenue: 7302
Top Selling Product: Notebook
```

---

## Project Structure

```
etl-sales-data-pipeline/
│
├── customers.csv
├── products.csv
├── orders.csv
├── clean_customer.csv
├── sales_summary.csv
├── etl_sales_pipeline.py
├── README.md
```

---

## Key Skills Demonstrated

- Data Extraction
- Data Cleaning
- Data Validation
- Data Transformation
- Pandas Data Analysis
- Data Merging (Joins)
- Revenue Calculations
- CSV File Processing
- MySQL Data Loading
- ETL Pipeline Development

---

## Future Enhancements

- Add exception handling
- Export ETL summary report to a text file
- Generate revenue dashboards using Matplotlib
- Add logging functionality
- Schedule ETL jobs using Airflow or Cron
## Author

Mariya Preena

ETL | Data Analytics | Python | SQL | Pandas
