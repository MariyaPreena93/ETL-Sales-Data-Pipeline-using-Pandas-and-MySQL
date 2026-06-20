import pandas as pd

#read source files

customers =pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")

print("Data Read completed")

#Remove duplicates
cust = customers.drop_duplicates()
print("----After removing duplicates----")
print(cust)
print("Duplicate records removed:", (len(customers)-len(cust)))

#Remove row if column is missing
cust = cust.dropna(subset=["email"])

#Replace missing data:

cust = cust.fillna({"city" :"Windsor"})
print(cust)

#finding Invalid productid In orders

ordr = orders[orders["product_id"].isin(products["product_id"])]
print(ordr)

Invalid_orders = orders[~orders["product_id"].isin(products["product_id"])]
print("No. of Invalid_orders: ",len(Invalid_orders))
print("-----Invalid_orders------")
print(Invalid_orders)


#Merge products and orders

sales =pd.merge(ordr,products,on="product_id",how = "left")

sales["revenue"]= sales["quantity"]*sales["price"]
print(sales)

#Total Revenue

total_rev = sales["revenue"].sum()
print("Total_Revenue:",total_rev)

Rev_cat = sales.groupby("product_name")["revenue"].sum()
print("----Revenue by product name----")
print(Rev_cat)

#Merge sales and customers

cust_sales = pd.merge(sales,cust,on ="customer_id",how="inner")
print("----Revenue by customers name----")
cust_rev = cust_sales.groupby("customer_name")["revenue"].sum()
print (cust_rev)

#top selling product
top_prd=(sales.groupby("product_name")["quantity"].sum().idxmax())
print("Top selling product:",top_prd)

#Summary
print("\n-----Summary------")

print("Customer Records:", len(customers))
print("Clean Customer Records:", len(cust))
print("Invalid Orders:", len(Invalid_orders))
print("Valid Orders:", len(ordr))
print("Total Revenue:", total_rev)
print("Top selling product:",top_prd)

#Load into csv file

cust.to_csv("clean_customer.csv",index=False)
sales.to_csv("sales_summary.csv",index=False)
Invalid_orders.to_csv("invalid_orders.csv",index=False)

print("Created file successfully")


#loading into Mysql


from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:preena@localhost/test"
    )
cust.to_sql(
    name="customers",
    con=engine,
    if_exists="replace",
    index=False
)

sales.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully")
