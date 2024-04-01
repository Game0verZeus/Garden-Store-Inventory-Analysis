import pandas as pd

# 1. Load the data into a DataFrame called inventory.
inventory = pd.read_csv('inventory.csv')

# 2. Inspect the first 10 rows of inventory.
print(inventory.head(10))

# 3. Select the first 10 rows and save them to staten_island.
staten_island = inventory.head(10)

# 4. Select the column product_description from staten_island and save it to product_request.
product_request = staten_island['product_description']

# 5. Select rows where location is 'Brooklyn' and product_type is 'seeds' and save to seed_request.
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# 6. Add a column called in_stock which is True if quantity is greater than 0.
inventory['in_stock'] = inventory['quantity'] > 0

# 7. Create a column called total_value that is equal to price multiplied by quantity.
inventory['total_value'] = inventory['price'] * inventory['quantity']

# 8. Define a lambda function to combine product_type and product_description.
combine_lambda = lambda row: '{} - {}'.format(row['product_type'], row['product_description'])

# 9. Create a new column in inventory called full_description using the combine_lambda function.
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
