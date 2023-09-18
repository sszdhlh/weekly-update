import csv
import os

path = "C:\\Users\\cicr9\\Documents\\各sku销量-Weekly\\cin7 data"
files = os.listdir(path)

# Initializing dictionaries and lists
sku_sales = {}  # Dictionary to hold sales numbers by SKU

for filename in files:
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for line in reader:
            if len(line) < 8 or not line[0] or not line[7]:
                continue

            # Filtering conditions
            item_condition = line[6] == 'Use'
            description_conditions = any(substring in line[4].upper() for substring in ["DELIVERY", "INSTALL", "SHIPPING", "FEE", "OC", "INSTALLATION", "SHIPPING"])
            if item_condition or description_conditions:
                continue

            sku = line[4]
            qty = float(line[5])

            # Adding to sales dictionary
            if sku != 'Item Code':
                if sku in sku_sales:
                    sku_sales[sku] += qty
                else:
                    sku_sales[sku] = qty

# Writing out the results
output_path = 'result/salenum by sku.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(['SKU', 'Number'])
    for sku, qty in sku_sales.items():
        csv_write.writerow([sku, qty])
