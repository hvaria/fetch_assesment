import pandas as pd

# Loading data into DataFrames
with open('Data/receipts.json', 'r') as file:
    receipts_data = file.read().strip()
    receipts_df = pd.read_json(receipts_data, lines=True)

with open('Data/users.json', 'r') as file:
    users_data = file.read().strip()
    users_df = pd.read_json(users_data, lines=True)

with open('Data/brands.json', 'r') as file:
    brands_data = file.read().strip()
    brands_df = pd.read_json(brands_data, lines=True)

#Checking for missing values
print("Missing values check:")
missing_values_receipts = receipts_df.isnull().sum()
missing_values_users = users_df.isnull().sum()
missing_values_brands = brands_df.isnull().sum()
print("Receipts:")
print(missing_values_receipts)
print("Users:")
print(missing_values_users)
print("Brands:")
print(missing_values_brands)

# Checking for duplicate records
print("\nDuplicate records check:")

def get_hashable_columns(df):
    hashable_columns = []
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, (int, float, str, bool, pd.Timestamp, type(None)))).all():
            hashable_columns.append(col)
    return hashable_columns

receipts_hashable_columns = get_hashable_columns(receipts_df)
users_hashable_columns = get_hashable_columns(users_df)
brands_hashable_columns = get_hashable_columns(brands_df)

duplicate_receipts = receipts_df.duplicated(subset=receipts_hashable_columns).sum()
duplicate_users = users_df.duplicated(subset=users_hashable_columns).sum()
duplicate_brands = brands_df.duplicated(subset=brands_hashable_columns).sum()

print(f"Number of duplicate receipts: {duplicate_receipts}")
print(f"Number of duplicate users: {duplicate_users}")
print(f"Number of duplicate brands: {duplicate_brands}")

# Checking for inconsistent date formats
print("\nInconsistent date format check:")
date_columns = ['createDate', 'dateScanned', 'finishedDate', 'modifyDate', 'pointsAwardedDate', 'purchaseDate']
for col in date_columns:
    if col in receipts_df.columns:
        unique_date_formats = receipts_df[col].astype(str).apply(lambda x: x[:10]).nunique()
        print(f"Unique date formats in {col}: {unique_date_formats}")

if 'createdDate' in users_df.columns:
    unique_date_formats = users_df['createdDate'].astype(str).apply(lambda x: x[:10]).nunique()
    print(f"Unique date formats in createdDate: {unique_date_formats}")

# Checking for outliers/invalid values
print("\nOutlier/invalid value checks:")
if 'purchasedItemCount' in receipts_df.columns:
    min_purchased_items = receipts_df['purchasedItemCount'].min()
    max_purchased_items = receipts_df['purchasedItemCount'].max()
    print(f"Min purchasedItemCount: {min_purchased_items}, Max: {max_purchased_items}")

if 'totalSpent' in receipts_df.columns:
    min_total_spent = receipts_df['totalSpent'].min()
    max_total_spent = receipts_df['totalSpent'].max()
    print(f"Min totalSpent: {min_total_spent}, Max: {max_total_spent}")

if 'role' in users_df.columns:
    unique_roles = users_df['role'].unique()
    print(f"Unique values in role column: {unique_roles}")

if 'active' in users_df.columns:
    unique_active_values = users_df['active'].unique()
    print(f"Unique values in active column: {unique_active_values}")

if 'topBrand' in brands_df.columns:
    unique_top_brand_values = brands_df['topBrand'].unique()
    print(f"Unique values in topBrand column: {unique_top_brand_values}")

# Checking referential integrity
print("\nReferential integrity checks:")
if 'userId' in receipts_df.columns and '_id' in users_df.columns:
    receipts_without_user = receipts_df[~receipts_df['userId'].isin(users_df['_id'])].shape[0]
    print(f"Number of receipts with userId not in users: {receipts_without_user}")

if 'cpg' in brands_df.columns and '_id' in brands_df.columns:
    brands_with_invalid_cpg = brands_df[brands_df['cpg'].notnull() & ~brands_df['cpg'].isin(brands_df['_id'])].shape[0]
    print(f"Number of brands with cpg not in brands: {brands_with_invalid_cpg}")
