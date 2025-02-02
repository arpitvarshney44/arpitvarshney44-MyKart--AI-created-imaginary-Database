import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(42)  # Reproducible results
random.seed(42)

# Define dataset sizes
num_customers = 700
num_products = 100
num_orders = 10000  # Increased orders
num_suppliers = 50  # Increased suppliers
num_warehouses = 3

# Generate diverse names
unique_names = list(set(fake.name() for _ in range(300)))[:250]  # Ensuring uniqueness
random.shuffle(unique_names)

# Create Customers.csv
customers = [{"Customer ID": i+1, "Name": unique_names[i % len(unique_names)], "Location": fake.city(),
              "Contact": fake.phone_number(), "Purchase History": random.randint(1, 50)} for i in range(num_customers)]
customers_df = pd.DataFrame(customers)
customers_df.to_csv("Customers.csv", index=False)

# Create Products.csv (100 products)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books", "Toys", "Beauty", "Automotive"]
products = [{"Product ID": i+1, "Name": fake.word().capitalize(), "Category": random.choice(categories),
             "Price": round(random.uniform(10, 500), 2), "Stock Quantity": random.randint(5, 200),
             "Supplier ID": random.randint(1, num_suppliers)} for i in range(num_products)]
products_df = pd.DataFrame(products)
products_df.to_csv("Products.csv", index=False)

# Create Suppliers.csv
suppliers = [{"Supplier ID": i+1, "Name": fake.company(), "Location": fake.city(),
              "Contact": fake.phone_number(), "Lead Time": random.randint(1, 20)} for i in range(num_suppliers)]
suppliers_df = pd.DataFrame(suppliers)
suppliers_df.to_csv("Suppliers.csv", index=False)

# Create Orders.csv
orders = [{"Order ID": i+1, "Customer ID": random.randint(1, num_customers), "Product ID": random.randint(1, num_products),
           "Order Date": fake.date_between(start_date="-1y", end_date="today"),
           "Quantity": random.randint(1, 5), "Total Price": round(random.uniform(50, 2000), 2),
           "Order Status": random.choice(["Delivered", "Pending", "Shipped", "Cancelled"])}
          for i in range(num_orders)]
orders_df = pd.DataFrame(orders)
orders_df.to_csv("Orders.csv", index=False)

# Create Warehouse_Stock.csv
warehouse_stock = [{"Warehouse ID": random.randint(1, num_warehouses), "Product ID": random.randint(1, num_products),
                    "Stock Quantity": random.randint(20, 500), "Last Restock Date": fake.date_between(start_date="-6m", end_date="today")}
                   for _ in range(num_products)]
warehouse_stock_df = pd.DataFrame(warehouse_stock)
warehouse_stock_df.to_csv("Warehouse_Stock.csv", index=False)

# Create Shipments.csv
shipments = [{"Shipment ID": i+1, "Order ID": random.randint(1, num_orders), "Carrier Name": fake.company(),
              "Dispatch Date": fake.date_between(start_date="-6m", end_date="today"),
              "Delivery Date": fake.date_between(start_date="-5m", end_date="today"),
              "Status": random.choice(["In Transit", "Delivered", "Delayed", "Lost"])}
             for i in range(num_orders)]
shipments_df = pd.DataFrame(shipments)
shipments_df.to_csv("Shipments.csv", index=False)

# Create Returns.csv (10% returns)
returns = [{"Return ID": i+1, "Order ID": random.randint(1, num_orders), "Product ID": random.randint(1, num_products),
            "Reason": random.choice(["Damaged", "Wrong Item", "Not Satisfied", "Other"]),
            "Refund Amount": round(random.uniform(10, 500), 2)} for i in range(int(num_orders * 0.1))]
returns_df = pd.DataFrame(returns)
returns_df.to_csv("Returns.csv", index=False)

print("All logically linked CSV files have been generated successfully!")
