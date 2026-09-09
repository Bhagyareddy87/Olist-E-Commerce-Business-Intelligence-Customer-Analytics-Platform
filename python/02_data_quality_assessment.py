                                     ### HANDLE MISSING VALUES ###

 ########### Issue #1: order_approved_at. ###########
import pandas as pd
from pathlib import Path

# Raw data location
data_path = Path(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Raw"
)

# Load orders dataset
orders = pd.read_csv(data_path / "olist_orders_dataset.csv")


# Find the affected orders
# Find orders with missing approval date
orders_missing_approved = orders[
    orders["order_approved_at"].isna()
]
# Check the order status
print(orders_missing_approved)

orders_missing_approved["order_status"].value_counts()
# Investigate the 14 delivered orders
orders_missing_approved[
    orders_missing_approved["order_status"] == "delivered"
]
delivered_missing_approved = orders_missing_approved[
    orders_missing_approved["order_status"] == "delivered"
]

delivered_missing_approved[
    [
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
]
# Investigate the created orders
orders_missing_approved[
    orders_missing_approved["order_status"] == "created"
]
orders_missing_approved[
    orders_missing_approved["order_status"] == "created"
][
    [
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
]


######## Issue #2: order_delivered_carrier_date. ###########
# Find the affected orders
orders_missing_carrier = orders[
    orders["order_delivered_carrier_date"].isna()
]

orders_missing_carrier["order_status"].value_counts()
# investigate the 2 delivered orders
orders_missing_carrier[
    orders_missing_carrier["order_status"] == "delivered"
][
    [
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
]

# investigate the 314 invoiced orders and 301 processing orders.
orders_missing_carrier[
    orders_missing_carrier["order_status"].isin(
        ["invoiced", "processing"]
    )
]["order_status"].value_counts()

# investigate the 2 approved orders.
orders_missing_carrier[
    orders_missing_carrier["order_status"] == "approved"
][
    [
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
]

####### Issue #3 — order_delivered_customer_date. #######
# Step 1: Check which order statuses have missing delivery dates
orders_missing_delivery = orders[
    orders["order_delivered_customer_date"].isna()
]
 # investigate the 8 delivered orders
orders_missing_delivery["order_status"].value_counts()

orders_missing_delivery[
    orders_missing_delivery["order_status"] == "delivered"
][
    [
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
]

####### Issue #4 — review_comment_title. ########
#  Check whether missing titles are related to review scores
reviews = pd.read_csv(
    data_path / "olist_order_reviews_dataset.csv"
)

reviews_missing_title = reviews[
    reviews["review_comment_title"].isna()
]

reviews_missing_title["review_score"].value_counts().sort_index()

####### Issue #5 — review_comment_message. ########
reviews_missing_message = reviews[
    reviews["review_comment_message"].isna()
]

reviews_missing_message["review_score"].value_counts().sort_index()

######## Issue #6 — product_category_name ########
# Check the missing records
products = pd.read_csv(
    data_path / "olist_products_dataset.csv"
)

products_missing_category = products[
    products["product_category_name"].isna()
]

products_missing_category

order_items = pd.read_csv(
    data_path / "olist_order_items_dataset.csv"
)

missing_category_sold = order_items[
    order_items["product_id"].isin(
        products_missing_category["product_id"]
    )
]

missing_category_sold["product_id"].nunique()

### Check whether all 3 are missing for the same products  ###
products_missing_metadata = products[
    products[
        [
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty"
        ]
    ].isna().any(axis=1)
]

products_missing_metadata[
    [
        "product_id",
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty"
    ]
]

products_missing_dimensions = products[
    products[
        [
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
    ].isna().any(axis=1)
]

products_missing_dimensions[
    [
        "product_id",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
]

# ============================================================
# DATA QUALITY ASSESSMENT — MISSING VALUES
# ============================================================
#
# Purpose:
# Assess missing values identified during Data Profiling and
# decide whether they are legitimate, problematic, or require
# further investigation.
#
# ------------------------------------------------------------
# 1. ORDERS — order_approved_at
# ------------------------------------------------------------
# Missing: 160 (0.16%)
#
# Assessment:
# - 141 canceled orders → missing approval is reasonable.
# - 5 created orders → missing approval is reasonable because
#   the orders were not approved/processed further.
# - 14 delivered orders → suspicious because delivered orders
#   normally should have an approval timestamp.
#
# Decision:
# Keep missing values as NaN.
# Do not impute/fill unknown approval timestamps.
# Flag the 14 delivered orders as data-quality anomalies.
#
# ------------------------------------------------------------
# 2. ORDERS — order_delivered_carrier_date
# ------------------------------------------------------------
# Missing: 1,783 (1.79%)
#
# Assessment:
# - unavailable, canceled, invoiced, processing, created and
#   approved orders → missing carrier date is generally reasonable.
# - 2 delivered orders → suspicious because delivered orders
#   should normally have reached the carrier.
#
# Decision:
# Keep missing values as NaN.
# Do not invent carrier delivery dates.
# Flag the 2 delivered orders as data-quality anomalies.
#
# ------------------------------------------------------------
# 3. ORDERS — order_delivered_customer_date
# ------------------------------------------------------------
# Missing: 2.98%
#
# Assessment:
# - canceled, unavailable, invoiced and processing orders →
#   missing delivery date is reasonable.
# - shipped orders → likely not yet delivered.
# - 8 delivered orders → suspicious because delivered orders
#   should normally have an actual delivery date.
#
# Decision:
# Keep missing values as NaN.
# Do not invent delivery dates.
# Flag the 8 delivered orders as data-quality anomalies.
#
# ------------------------------------------------------------
# 4. REVIEWS — review_comment_title
# ------------------------------------------------------------
# Missing: 88.34%
#
# Assessment:
# Customers can provide a review score without writing a
# review title. Missing titles are therefore legitimate.
#
# Decision:
# Keep missing values as NaN.
# Do not delete reviews or create artificial titles.
#
# ------------------------------------------------------------
# 5. REVIEWS — review_comment_message
# ------------------------------------------------------------
# Missing: 58.70%
#
# Assessment:
# Customers can provide a review score without writing a
# review message. Missing messages are therefore legitimate.
#
# Decision:
# Keep missing values as NaN.
# Do not create artificial review text.
#
# ------------------------------------------------------------
# 6. PRODUCTS — product_category_name
# ------------------------------------------------------------
# Missing: 610 products (1.85%)
#
# Assessment:
# All 610 products with missing categories were found in
# order_items, meaning they were actually sold.
#
# Decision:
# Do not delete these products.
# Keep category as NaN for now.
# Investigate possible recovery during Data Cleaning/
# Transformation. If recovery is not possible, treat them
# as Unknown/Uncategorized for analysis.
#
# ------------------------------------------------------------
# 7. PRODUCTS — product_name_lenght,
#              product_description_lenght,
#              product_photos_qty
# ------------------------------------------------------------
# Missing: 610 products (1.85%) for each field.
#
# Assessment:
# The same 610 products are missing all three metadata fields.
# This appears to be one underlying product-metadata issue.
#
# Decision:
# Keep the products.
# Do not delete them.
# Do not automatically replace missing values with 0.
# Decide the appropriate treatment during Data Cleaning.
#
# ------------------------------------------------------------
# 8. PRODUCTS — product_weight_g,
#              product_length_cm,
#              product_height_cm,
#              product_width_cm
# ------------------------------------------------------------
# Missing: 2 products (0.006%) for each field.
#
# Assessment:
# Only 2 products have all four physical attributes missing.
# The percentage is extremely small.
#
# Decision:
# Keep the products and retain the missing values as NaN.
# Do not assume missing physical measurements are zero.
# Handle them during Data Cleaning if required for analysis.
#
# ============================================================
# OVERALL MISSING VALUE ASSESSMENT
# ============================================================
#
# Most missing values are legitimate business/data conditions.
# No missing values will be blindly filled or deleted.
#
# General decision:
# - Keep legitimate missing values as NaN.
# - Flag suspicious records for further quality checks.
# - Investigate recoverable information during Data Cleaning.
# - Never invent values when the actual value is unknown.
#
# Missing Value Assessment: COMPLETE
# Next: Duplicate Assessment
# ============================================================

                                   ### HANDLE DUPLICATE RECORDS ###

######## ISSUE: Inspect the duplicate rows #########
geolocation = pd.read_csv(
    data_path / "olist_geolocation_dataset.csv"
)

geolocation_duplicates = geolocation[
    geolocation.duplicated(keep=False)
]

geolocation_duplicates.head(20)

geolocation.duplicated().sum()

geolocation.drop_duplicates().shape


                                   ###  Data Type Assessment. ###
# load CSV files
import pandas as pd
from pathlib import Path

# Raw data folder
data_path = Path(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Raw"
)

# Load all datasets
customers = pd.read_csv(data_path / "olist_customers_dataset.csv")

geolocation = pd.read_csv(data_path / "olist_geolocation_dataset.csv")

orders = pd.read_csv(data_path / "olist_orders_dataset.csv")

order_items = pd.read_csv(data_path / "olist_order_items_dataset.csv")

payments = pd.read_csv(data_path / "olist_order_payments_dataset.csv")

reviews = pd.read_csv(data_path / "olist_order_reviews_dataset.csv")

products = pd.read_csv(data_path / "olist_products_dataset.csv")

sellers = pd.read_csv(data_path / "olist_sellers_dataset.csv")

category_translation = pd.read_csv(
    data_path / "product_category_name_translation.csv"
)

# Check the data types of each dataset
customers.dtypes
geolocation.dtypes
orders.dtypes
order_items.dtypes
payments.dtypes
reviews.dtypes
products.dtypes
sellers.dtypes
category_translation.dtypes


                                   ###  Invalid / Inconsistent Values ###

#  See all order statuses
orders["order_status"].value_counts()
### order_status ###
# 8 distinct status values were found.
# Values are consistently formatted with no obvious
# spelling or capitalization inconsistencies.
# Decision: No action required.

### See all review scores ###
reviews["review_score"].value_counts().sort_index()
# review_score:
# All review scores are within the valid range of 1-5.
# No invalid values found.
# Decision: No action required.

### See payment ranges ###
payments["payment_value"].min()
payments["payment_value"].max()
order_items["price"].min()
order_items["price"].max()
# payment_value:
# Minimum value is 0.00 and maximum is 13,664.08.
# No negative payment values found.
# Decision: No immediate invalid-value issue.
# price:
# Minimum price is 0.85 and maximum is 6735.00.
# No negative prices found.
# Decision: No immediate invalid-value issue.

### check freight_value ###
order_items["freight_value"].min()
order_items["freight_value"].max()
# freight_value:
# Minimum value is 0.00 and maximum is 409.68.
# No negative freight values found.
# Decision: No immediate invalid-value issue.
# Extreme values will be assessed later as part of outlier analysis.

### check: payment installments ###
payments["payment_installments"].min()
payments["payment_installments"].max()
payments[payments["payment_installments"] == 0]["payment_type"].value_counts()
payments[payments["payment_installments"] == 0]
# payment_installments:
# Values range from 0 to 24.
# 2 credit card payment records have 0 installments.
# Since a credit card payment should normally have at least 1 installment,
# these 2 records are considered suspicious/invalid.
# Decision: Flag for investigation/correction during Data Cleaning.

### check payment_type ###
payments["payment_type"].value_counts()
payments[payments["payment_type"] == "not_defined"]
# payment_type:
# 5 payment types were found.
# 4 are valid/expected payment methods:
# credit_card, boleto, voucher, and debit_card.
# 3 records have payment_type = "not_defined".
# These records also have payment_value = 0.00.
# Decision: Flag these 3 records for investigation during Data Cleaning.

### check payment_sequential ###
payments["payment_sequential"].min()
payments["payment_sequential"].max()
# payment_sequential:
# Values range from 1 to 29.
# Minimum value of 1 is valid because payment sequences start at 1.
# No zero or negative sequence values found.
# Decision: No immediate invalid-value issue.

### check order_item_id ###
order_items["order_item_id"].min()
order_items["order_item_id"].max()
# order_item_id:
# Values range from 1 to 21.
# Minimum value of 1 is valid because item sequences start at 1.
# No zero or negative item sequence values found.
# Decision: No immediate invalid-value issue.

### check the product quantity ###
products["product_photos_qty"].min()
products["product_photos_qty"].max()
# product_photos_qty:
# Values range from 1 to 20.
# No zero or negative values found.
# Decision: No immediate invalid-value issue.

### check the physical dimension fields ###
products["product_weight_g"].min()
products["product_weight_g"].max()
products["product_length_cm"].min()
products["product_length_cm"].max()
products["product_height_cm"].min()
products["product_height_cm"].max()
products["product_width_cm"].min()
products["product_width_cm"].max()

(products["product_weight_g"] == 0).sum()
# product_weight_g:
# Values range from 0 to 40,425 grams.
# 4 products have a weight of 0 grams.
# A physical product should normally have a positive weight.
# Decision: Flag these 4 records for investigation during Data Cleaning.

### product category field ###
products["product_category_name"].value_counts(dropna=False).head(20)
# product_category_name:
# Category values are consistently formatted in the dataset.
# 610 records have missing category values (NaN).
# These missing values were already identified during Missing Values Assessment.
# Decision: No additional invalid-value issue found.
# Missing categories will be handled during Data Cleaning/Transformation.

### check customer_state ###
customers["customer_state"].value_counts(dropna=False)
# customer_state:
# 27 distinct state codes were found.
# Values are consistently formatted as 2-letter uppercase codes.
# No missing or obvious invalid/inconsistent state values found.
# Decision: No action required.

### check seller_state ###
sellers["seller_state"].value_counts(dropna=False)
# seller_state:
# 23 distinct state codes were found.
# Values are consistently formatted as 2-letter uppercase codes.
# No missing or obvious invalid/inconsistent state values found.
# Decision: No action required.

### check customer_cityname ###
customers["customer_city"].isna().sum()
(customers["customer_city"].str.strip() == "").sum()
# customer_city:
# No missing (NaN) values found.
# No blank or empty city values found.
# Decision: No action required.

### check seller_cityname ###
sellers["seller_city"].isna().sum()
(sellers["seller_city"].str.strip() == "").sum()
# seller_city:
# No missing (NaN) values found.
# No blank or empty city values found.
# Decision: No action required.

### check geolocation_state ###
geolocation["geolocation_state"].value_counts(dropna=False)
geolocation["geolocation_city"].isna().sum()
(geolocation["geolocation_city"].str.strip() == "").sum()
# geolocation_state:
# 27 distinct state codes were found.
# Values are consistently formatted as 2-letter uppercase codes.
# No missing or obvious invalid/inconsistent state values found.
# Decision: No action required.

### check customer_zip_code_prefix ###
customers["customer_zip_code_prefix"].min()
customers["customer_zip_code_prefix"].max()
(customers["customer_zip_code_prefix"] <= 0).sum()
# customer_zip_code_prefix:
# Values range from 1003 to 99990.
# No zero or negative ZIP code prefixes found.
# Decision: No immediate invalid-value issue.

### check seller_zip_code_prefix ###
sellers["seller_zip_code_prefix"].min()
sellers["seller_zip_code_prefix"].max()
(sellers["seller_zip_code_prefix"] <= 0).sum()
# seller_zip_code_prefix:
# Values range from 1001 to 99730.
# No zero or negative ZIP code prefixes found.
# Decision: No immediate invalid-value issue.

#### check geolocation_zip_code_prefix ###
geolocation["geolocation_zip_code_prefix"].min()
geolocation["geolocation_zip_code_prefix"].max()
(geolocation["geolocation_zip_code_prefix"] <= 0).sum()
# geolocation_zip_code_prefix:
# Values range from 1001 to 99990.
# No zero or negative ZIP code prefixes found.
# Decision: No immediate invalid-value issue.
 

### check latitude and longitude ###
geolocation["geolocation_lat"].min()
geolocation["geolocation_lat"].max()
geolocation["geolocation_lng"].min()
geolocation["geolocation_lng"].max()
# geolocation_lat:
# Values range from -36.61 to 45.07.
# All values are within the valid latitude range of -90 to 90.
# Decision: No immediate invalid-value issue.

# geolocation_lng:
# Values range from -101.47 to 121.11.
# All values are within the valid longitude range of -180 to 180.
# Decision: No immediate invalid-value issue.

### check order_id ###
orders["order_id"].isna().sum()
(orders["order_id"].str.strip() == "").sum()

### check customer_id ###
orders["customer_id"].isna().sum()
(orders["customer_id"].str.strip() == "").sum()

### check order_id in order_items ###
order_items["order_id"].isna().sum()
(order_items["order_id"].str.strip() == "").sum()

### check product_id in order_items ###
order_items["product_id"].isna().sum()
(order_items["product_id"].str.strip() == "").sum()

### check seller_id in order_items ###
order_items["seller_id"].isna().sum()
(order_items["seller_id"].str.strip() == "").sum()

### check product_id in products ###
products["product_id"].isna().sum()
(products["product_id"].str.strip() == "").sum()

#### check seller_id in sellers ###
sellers["seller_id"].isna().sum()
(sellers["seller_id"].str.strip() == "").sum()

### check order_id in payments ###
payments["order_id"].isna().sum()
(payments["order_id"].str.strip() == "").sum()

### check review_id in reviews ###
reviews["review_id"].isna().sum()
(reviews["review_id"].str.strip() == "").sum()

### check order_id in reviews ###
reviews["order_id"].isna().sum()
(reviews["order_id"].str.strip() == "").sum()

### check customer_id in customers ###
customers["customer_id"].isna().sum()
(customers["customer_id"].str.strip() == "").sum()

# SUMMARY OF ID FIELD ASSESSMENT
# ID fields:
# No missing (NaN) or blank ID values found across the checked datasets.
# Decision: No action required.


### Date validity checks ###

# orders.order_purchase_timestamp:
# Check for invalid or unparseable purchase timestamps.
pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
).isna().sum()


# orders.order_approved_at:
# Check for invalid or unparseable approval timestamps.
pd.to_datetime(
    orders["order_approved_at"],
    errors="coerce"
).isna().sum()


# orders.order_delivered_carrier_date:
# Check for invalid or unparseable carrier delivery dates.
pd.to_datetime(
    orders["order_delivered_carrier_date"],
    errors="coerce"
).isna().sum()


# orders.order_delivered_customer_date:
# Check for invalid or unparseable customer delivery dates.
pd.to_datetime(
    orders["order_delivered_customer_date"],
    errors="coerce"
).isna().sum()


# orders.order_estimated_delivery_date:
# Check for invalid or unparseable estimated delivery dates.
pd.to_datetime(
    orders["order_estimated_delivery_date"],
    errors="coerce"
).isna().sum()


# order_items.shipping_limit_date:
# Check for invalid or unparseable shipping limit dates.
pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
).isna().sum()


# reviews.review_creation_date:
# Check for invalid or unparseable review creation dates.
pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
).isna().sum()


# reviews.review_answer_timestamp:
# Check for invalid or unparseable review answer timestamps.
pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
).isna().sum()
# Date validity:
# All non-missing datetime values can be successfully parsed.
# No invalid or unparseable date values were found.
# Missing datetime values were already identified during Missing Values Assessment.
# Decision: No additional invalid-date issue found.


### Purchase date → Approval date ###
orders["purchase_date"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

orders["approved_date"] = pd.to_datetime(
    orders["order_approved_at"],
    errors="coerce"
)

(orders["approved_date"] < orders["purchase_date"]).sum()
# Purchase → Approval:
# No orders were found where the approval date occurs before the purchase date.
# Decision: No action required.

### Approval date → Carrier date ###
orders["carrier_date"] = pd.to_datetime(
    orders["order_delivered_carrier_date"],
    errors="coerce"
)
orders["carrier_date"] = pd.to_datetime(
    orders["order_delivered_carrier_date"],
    errors="coerce"
)

(orders["carrier_date"] < orders["approved_date"]).sum()

orders[
    orders["carrier_date"] < orders["approved_date"]
]["order_status"].value_counts()
# check the time difference
orders["approval_to_carrier_days"] = (
    orders["carrier_date"] - orders["approved_date"]
).dt.total_seconds() / (60 * 60 * 24)

orders[
    orders["approval_to_carrier_days"] < 0
]["approval_to_carrier_days"].describe()


### check extreme cases: -170 days ###
orders[
    orders["approval_to_carrier_days"] < 0
].sort_values("approval_to_carrier_days").head(5)[
    [
        "order_id",
        "order_status",
        "purchase_date",
        "approved_date",
        "carrier_date",
        "approval_to_carrier_days"
    ]
]
# Approval → Carrier date:
# 1,359 orders have a carrier delivery date earlier than the approval date.
# These records are logically inconsistent with the expected order timeline.
# Most affected orders are delivered (1,350) and 9 are shipped.
# Extreme cases show the carrier date occurring several days or even months
# before the approval date.
# Decision: Flag these records for investigation during Data Cleaning.

### Carrier date → Customer delivery date ###
(
    pd.to_datetime(orders["order_delivered_customer_date"], errors="coerce")
    < orders["carrier_date"]
).sum()
# investigate 23 affected orders
orders[
    pd.to_datetime(orders["order_delivered_customer_date"], errors="coerce")
    < orders["carrier_date"]
].sort_values("carrier_date")[
    [
        "order_id",
        "order_status",
        "carrier_date",
        "order_delivered_customer_date"
    ]
]
# Carrier → Customer delivery:
# 23 delivered orders have a customer delivery date earlier
# than the carrier handover date.
# These records are logically inconsistent with the expected order timeline.
# Decision: Flag these records for investigation during Data Cleaning.

### Purchase → Customer Delivery ###
(
    pd.to_datetime(orders["order_delivered_customer_date"], errors="coerce")
    < orders["purchase_date"]
).sum()
# Purchase → Customer delivery:
# No orders were found where the customer delivery date
# occurs before the purchase date.
# Decision: No action required.

### Review creation date → Review answer timestamp ###
(
    pd.to_datetime(reviews["review_answer_timestamp"], errors="coerce")
    <
    pd.to_datetime(reviews["review_creation_date"], errors="coerce")
).sum()
# Review creation → Review answer:
# No reviews were found where the answer timestamp
# occurs before the review creation date.
# Decision: No action required.

### shipping_limit_date vs purchase date ###
(
    pd.to_datetime(order_items["shipping_limit_date"], errors="coerce")
    <
    orders.set_index("order_id")
    .loc[order_items["order_id"], "purchase_date"].values
).sum()
# Purchase → Shipping limit:
# No order items were found where the shipping limit date
# occurs before the purchase date.
# Decision: No action required.

 ### Invalid / Inconsistent Values - Summary ###

# Most checked fields contain valid and consistently formatted values.
# A small number of suspicious values were identified:
# 2 credit card payments with 0 installments,
# 3 payments with payment_type = "not_defined",
# 4 products with product_weight_g = 0,
# 1,359 orders with carrier date before approval date,
# and 23 orders with customer delivery date before carrier date.
# These records will be flagged and investigated during Data Cleaning.
# No other major invalid or inconsistent values were identified.

                                        ###### 🔑 Key & Referential Integrity #######
### orders.customer_id → customers.customer_id ###
orders["customer_id"].isin(customers["customer_id"]).value_counts()

### order_items.order_id → orders.order_id ###

# Check whether every order_id in order_items
# exists in the orders table.
order_items["order_id"].isin(orders["order_id"]).value_counts()

### order_items.order_id → orders.order_id ###
# Check whether every order_id in order_items
# exists in the orders table.
order_items["order_id"].isin(orders["order_id"]).value_counts()

### order_items.product_id → products.product_id ###
# Check whether every product_id in order_items
# exists in the products table.
order_items["product_id"].isin(products["product_id"]).value_counts()

### order_items.seller_id → sellers.seller_id ###
# Check whether every seller_id in order_items
# exists in the sellers table.
order_items["seller_id"].isin(sellers["seller_id"]).value_counts()

### payments.order_id → orders.order_id ###
# Check whether every order_id in payments
# exists in the orders table.
payments["order_id"].isin(orders["order_id"]).value_counts()

### reviews.order_id → orders.order_id ###
# Check whether every order_id in reviews
# exists in the orders table.
reviews["order_id"].isin(orders["order_id"]).value_counts()

### customers.customer_id uniqueness ###
# Check whether customer_id uniquely identifies each customer record.
customers["customer_id"].duplicated().sum()

### customers.customer_unique_id uniqueness ###
# Check whether customer_unique_id appears multiple times.
# Multiple occurrences are expected because the same customer
# may place multiple orders.
customers["customer_unique_id"].duplicated().sum()
### customers.customer_unique_id completeness ###
# Check for missing customer_unique_id values.
customers["customer_unique_id"].isna().sum()

### products.product_id uniqueness ###
# Check whether product_id uniquely identifies
# each product record.
products["product_id"].duplicated().sum()

### sellers.seller_id uniqueness ###
# Check whether seller_id uniquely identifies
# each seller record.
sellers["seller_id"].duplicated().sum()

### products.product_category_name → category_translation.product_category_name ###
# Check whether product categories have a corresponding
# entry in the category translation table.
products["product_category_name"].isin(
    category_translation["product_category_name"]
).value_counts(dropna=False)
# Products → Category Translation: Unmatched Categories 
# Find product categories that are not present
# in the category translation table.
unmatched_categories = products.loc[
    products["product_category_name"].notna()
    & ~products["product_category_name"].isin(
        category_translation["product_category_name"]
    ),
    "product_category_name"
].unique()

unmatched_categories
# Unmatched Product Categories
# Count products belonging to categories that are
# not present in the category translation table.
products[
    products["product_category_name"].isin(unmatched_categories)
]["product_category_name"].value_counts()
# category_translation.product_category_name uniqueness 
# Check whether each product category appears only once
# in the category translation table.
category_translation["product_category_name"].duplicated().sum()
# category_translation.product_category_name_english uniqueness 
# Check whether multiple product categories map to
# the same English translated category.
category_translation["product_category_name_english"].duplicated().sum()

### Order → Customer consistency ###
# Check whether an order_id is associated with more than one customer_id.
orders.groupby("order_id")["customer_id"].nunique().max()

### Customer → Order relationship ###
# Check the maximum number of orders associated
# with a single customer_id.
orders.groupby("customer_id")["order_id"].nunique().max()

### Order → Order Items relationship ###
# Check the maximum number of items associated
# with a single order.
order_items.groupby("order_id")["order_item_id"].nunique().max()

### Order item sequence consistency ###
# Check whether any order has an order_item_id
# greater than 1 without having item 1.
order_items.groupby("order_id")["order_item_id"].min().gt(1).sum()

### Payment sequence consistency ###
# Check whether any order has a payment sequence
# starting above 1.
payments.groupby("order_id")["payment_sequential"].min().gt(1).sum()
# Identify orders where the minimum payment sequence
# is greater than 1.
payment_sequence_issues = payments.groupby("order_id")["payment_sequential"].min()

payment_sequence_issues = payment_sequence_issues[
    payment_sequence_issues > 1
]

payment_sequence_issues
# Display payment records for orders where the
# first recorded payment sequence is greater than 1.
payments[
    payments["order_id"].isin(payment_sequence_issues.index)
].sort_values(["order_id", "payment_sequential"]).head(30)

### Order-to-payment completeness ###
# Check how many orders have at least one payment record.
orders_with_payment = payments["order_id"].nunique()
total_orders = orders["order_id"].nunique()
print("Total orders:", total_orders)
print("Orders with payment:", orders_with_payment)
print("Orders without payment:", total_orders - orders_with_payment)
### Identify orders without payment ###
# Find the order(s) that exist in orders
# but have no corresponding payment record.
orders_without_payment = orders[
    ~orders["order_id"].isin(payments["order_id"])
]
print(orders_without_payment[
    ["order_id", "customer_id", "order_status"]
])

### Delivered orders without review ###
# Identify delivered orders that do not have a review record.
delivered_orders = orders[
    orders["order_status"] == "delivered"
]
delivered_without_review = delivered_orders[
    ~delivered_orders["order_id"].isin(reviews["order_id"])
]
print("Total delivered orders:", delivered_orders["order_id"].nunique())
print("Delivered orders without review:", delivered_without_review["order_id"].nunique())

### Orders without order items ###
# Identify orders that do not have any associated order items.
orders_without_items = orders[
    ~orders["order_id"].isin(order_items["order_id"])
]
print("Total orders:", orders["order_id"].nunique())
print("Orders without items:", orders_without_items["order_id"].nunique())
### Orders without items - Status analysis ###
# Check the order status of orders that have no order-item records.
print(
    orders_without_items["order_status"]
    .value_counts()
)

### Sellers without order items ###
# Identify sellers that do not appear in order_items.
sellers_without_items = sellers[
    ~sellers["seller_id"].isin(order_items["seller_id"])
]
print("Total sellers:", sellers["seller_id"].nunique())
print("Sellers without order items:", sellers_without_items["seller_id"].nunique())

### Products without order items ###
# Identify products that do not appear in order_items.
products_without_items = products[
    ~products["product_id"].isin(order_items["product_id"])
]
print("Total products:", products["product_id"].nunique())
print("Products without order items:", products_without_items["product_id"].nunique())
### Key & Referential Integrity - Summary ###

# All major foreign-key relationships were validated successfully.
# No orphan customer, product, seller, payment, or review references were found.
# Primary identifiers are unique in their respective master datasets.
# All products and sellers are represented in order_items.
#
# A small number of business-integrity anomalies were identified:
# 1 delivered order has no payment record,
# and 3 orders (2 invoiced and 1 shipped) have no order-item records.
# These records will be flagged for investigation during Data Cleaning.
#
# Delivered orders without reviews were observed, but this is acceptable
# because submitting a review is optional.




                                        ###### Outlier Assessment #######
### Price Outlier Assessment ###
# Calculate Q1 and Q3 for product prices.
Q1 = order_items["price"].quantile(0.25)
Q3 = order_items["price"].quantile(0.75)

# Calculate the Interquartile Range (IQR).
IQR = Q3 - Q1

# Calculate the statistical outlier boundaries.
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Identify price outliers.
price_outliers = order_items[
    (order_items["price"] < lower_bound) |
    (order_items["price"] > upper_bound)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of price outliers:", len(price_outliers))
print("Percentage of price outliers:",
      round(len(price_outliers) / len(order_items) * 100, 2), "%")

### Price Outlier - Extreme Value Analysis ###
# Display the highest-priced order items.
print(
    price_outliers[
        ["order_id", "product_id", "price"]
    ]
    .sort_values("price", ascending=False)
    .head(20)
)
### Price Outlier - Conclusion ###
# 8,427 order-item prices (7.48%) are statistically classified
# as outliers using the IQR method.
# The extreme prices include legitimate high-value products
# and do not show obvious invalid or impossible values.
# Decision: Keep the price values unchanged.
# These outliers should be retained for business analysis because
# they may represent genuine high-value products.


### Freight Value Outlier Assessment ###
# Calculate Q1 and Q3 for freight values.
Q1 = order_items["freight_value"].quantile(0.25)
Q3 = order_items["freight_value"].quantile(0.75)

# Calculate the Interquartile Range (IQR).
IQR = Q3 - Q1

# Calculate the statistical outlier boundaries.
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Identify freight value outliers.
freight_outliers = order_items[
    (order_items["freight_value"] < lower_bound) |
    (order_items["freight_value"] > upper_bound)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of freight value outliers:", len(freight_outliers))
print("Percentage of freight value outliers:",
      round(len(freight_outliers) / len(order_items) * 100, 2), "%")

### Freight Value Outlier - Extreme Value Analysis ###

# Display the highest freight values.
print(
    freight_outliers[
        ["order_id", "product_id", "freight_value"]
    ]
    .sort_values("freight_value", ascending=False)
    .head(20)
)
### Freight Value Outlier - Conclusion ###
# 12,134 freight values (10.77%) are statistically classified
# as outliers using the IQR method.
# The extreme freight values are high but can be explained by
# product characteristics and shipping conditions.
# No obvious invalid or impossible freight values were identified.
# Decision: Keep freight values unchanged.
# Retain these outliers because they may represent genuine
# high-cost shipping transactions.


### Payment Value Outlier Assessment ###
# Calculate Q1 and Q3 for payment values.
Q1 = payments["payment_value"].quantile(0.25)
Q3 = payments["payment_value"].quantile(0.75)

# Calculate the Interquartile Range (IQR).
IQR = Q3 - Q1

# Calculate the statistical outlier boundaries.
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Identify payment value outliers.
payment_value_outliers = payments[
    (payments["payment_value"] < lower_bound) |
    (payments["payment_value"] > upper_bound)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of payment value outliers:", len(payment_value_outliers))
print("Percentage of payment value outliers:",
      round(len(payment_value_outliers) / len(payments) * 100, 2), "%")
### Payment Value Outlier - Extreme Value Analysis ###
# Display the highest payment values.
print(
    payment_value_outliers[
        ["order_id", "payment_type", "payment_installments", "payment_value"]
    ]
    .sort_values("payment_value", ascending=False)
    .head(20)
)
### Payment Value Outlier - Conclusion ###
# 7,981 payment values (7.68%) are statistically classified
# as outliers using the IQR method.
# The extreme payment values correspond to high-value transactions
# and use valid payment methods.
# No obvious invalid or impossible payment values were identified.
# Decision: Keep payment values unchanged.
# Retain these outliers because they may represent genuine
# high-value customer transactions.

### Product Weight Outlier Assessment ###
# Calculate Q1 and Q3 for product weight.
Q1 = products["product_weight_g"].quantile(0.25)
Q3 = products["product_weight_g"].quantile(0.75)

# Calculate the Interquartile Range (IQR).
IQR = Q3 - Q1

# Calculate the statistical outlier boundaries.
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Identify product weight outliers.
weight_outliers = products[
    (products["product_weight_g"] < lower_bound) |
    (products["product_weight_g"] > upper_bound)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of weight outliers:", len(weight_outliers))
print("Percentage of weight outliers:",
      round(len(weight_outliers) / products["product_weight_g"].notna().sum() * 100, 2), "%")
### Product Weight Outlier - Extreme Value Analysis ###
# Display the products with the highest weights.
print(
    weight_outliers[
        ["product_id", "product_category_name", "product_weight_g"]
    ]
    .sort_values("product_weight_g", ascending=False)
    .head(20)
)
### Product Weight - Extreme Value Frequency ###
# Check the most frequent high product-weight values.
print(
    products.loc[
        products["product_weight_g"] >= 10000,
        "product_weight_g"
    ]
    .value_counts()
    .head(20)
)
### Product Weight Outlier - Conclusion ###
# 4,551 product weights (13.81%) are statistically classified
# as outliers using the IQR method.
# Many high-weight products occur across legitimate product categories.
# The value 30,000 g occurs 143 times, indicating a repeated
# high-weight value rather than an isolated anomaly.
# Decision: Keep statistical weight outliers unchanged.
# The previously identified 4 products with weight = 0 remain
# separate invalid-value findings and will be flagged for cleaning.

### Product Dimension Outlier Assessment ###
# List the product dimension columns to assess.
dimension_columns = [
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

# Calculate IQR-based outliers for each dimension.
for column in dimension_columns:

    Q1 = products[column].quantile(0.25)
    Q3 = products[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    dimension_outliers = products[
        (products[column] < lower_bound) |
        (products[column] > upper_bound)
    ]

    print("\nColumn:", column)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of outliers:", len(dimension_outliers))
    print(
        "Percentage of outliers:",
        round(
            len(dimension_outliers) /
            products[column].notna().sum() * 100,
            2
        ),
        "%"
    )
### Product Dimension - Extreme Value Analysis ###

# Display the products with the largest values
# for each physical dimension.

for column in dimension_columns:

    print("\nHighest values for:", column)

    print(
        products[
            ["product_id", "product_category_name", column]
        ]
        .sort_values(column, ascending=False)
        .head(10)
    )
### Product Dimension Outlier - Conclusion ###
# Product dimensions contain statistical outliers:
# Length: 1,380 (4.19%)
# Height: 1,892 (5.74%)
# Width: 912 (2.77%)
#
# The extreme values are physically plausible and occur across
# legitimate product categories.
# No obviously impossible dimension values were identified.
# Decision: Keep dimension outliers unchanged.
# Previously identified missing dimension values will remain
# as missing and will be handled during Data Cleaning.

                                                ### Outlier Assessment - Summary ###

# IQR-based outlier analysis was performed on key numeric business fields.
#
# Price:
# 8,427 outliers (7.48%) were identified above the statistical boundary.
# Extreme prices appeared to represent legitimate high-value products.
# Decision: Keep unchanged.
#
# Freight Value:
# 12,134 outliers (10.77%) were identified.
# High freight values can be associated with product size and shipping conditions.
# Decision: Keep unchanged.
#
# Payment Value:
# 7,981 outliers (7.68%) were identified.
# Extreme payment values correspond to high-value transactions.
# Decision: Keep unchanged.
#
# Product Weight:
# 4,551 outliers (13.81%) were identified.
# High weights were observed across legitimate product categories.
# Decision: Keep unchanged.
# Four products with weight = 0 remain flagged as invalid values
# from the earlier Invalid / Inconsistent Values assessment.
#
# Product Dimensions:
# Length: 1,380 outliers (4.19%)
# Height: 1,892 outliers (5.74%)
# Width: 912 outliers (2.77%)
# Extreme dimensions were physically plausible across product categories.
# Decision: Keep unchanged.
#
# Overall conclusion:
# Statistical outliers were investigated and no major evidence of
# erroneous extreme values was found. Outliers will be retained because
# they may represent legitimate business transactions or products.
# Known invalid/suspicious values identified in earlier assessments
# will be handled separately during Data Cleaning.


### Business Rule - Delivered orders must have delivery date ###

# Identify delivered orders where the customer delivery date is missing.
delivered_without_delivery_date = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isna())
]

print(
    "Delivered orders without delivery date:",
    len(delivered_without_delivery_date)
)
### Business Rule - Conclusion ###
# 8 delivered orders do not have a customer delivery date.
# This violates the expected order lifecycle because a delivered
# order should normally have a recorded delivery date.
# Decision: Keep the orders and flag these 8 records for investigation
# during Data Cleaning. Do not impute a delivery date.

### Business Rule - Delivered orders must have carrier date ###
# Identify delivered orders where the carrier delivery date is missing.
delivered_without_carrier_date = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_carrier_date"].isna())
]

print(
    "Delivered orders without carrier date:",
    len(delivered_without_carrier_date)
)
### Business Rule - Conclusion ###
# 2 delivered orders do not have a carrier delivery date.
# This violates the expected order fulfillment lifecycle because
# a delivered order should normally have a recorded carrier date.
# Decision: Keep the orders and flag these 2 records for investigation
# during Data Cleaning. Do not impute a carrier date.

### Business Rule- Order lifecycle chronology ###

# Convert order lifecycle dates to datetime for comparison.
orders["purchase_date"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

orders["approved_date"] = pd.to_datetime(
    orders["order_approved_at"],
    errors="coerce"
)

orders["carrier_date"] = pd.to_datetime(
    orders["order_delivered_carrier_date"],
    errors="coerce"
)

orders["customer_delivery_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"],
    errors="coerce"
)

# Check whether approval occurred before purchase.
approval_before_purchase = orders[
    orders["approved_date"] < orders["purchase_date"]
]

# Check whether carrier handover occurred before approval.
carrier_before_approval = orders[
    orders["carrier_date"] < orders["approved_date"]
]

# Check whether customer delivery occurred before carrier handover.
delivery_before_carrier = orders[
    orders["customer_delivery_date"] < orders["carrier_date"]
]

print("Approval before purchase:", len(approval_before_purchase))
print("Carrier before approval:", len(carrier_before_approval))
print("Delivery before carrier:", len(delivery_before_carrier))
### Business Rule  - Conclusion ###

# The order lifecycle was validated using the expected sequence:
# Purchase -> Approval -> Carrier -> Customer Delivery.
#
# Approval before purchase:
# 0 violations. Rule passed.
#
# Carrier before approval:
# 1,359 violations identified.
# These records will be flagged for investigation.
#
# Customer delivery before carrier:
# 23 violations identified.
# These records will be flagged for investigation.
#
# Decision: Keep the original dates unchanged.
# Investigate and flag chronology violations during Data Cleaning.

### Delivered orders without payment ###

# Identify delivered orders that do not have a payment record.
delivered_without_payment = delivered_orders[
    ~delivered_orders["order_id"].isin(payments["order_id"])
]
print(
    "Delivered orders without payment:",
    delivered_without_payment["order_id"].nunique()
)
### Delivered orders without payment - Conclusion ###
# 1 delivered order does not have a corresponding payment record.
# This is a suspicious business-integrity anomaly.
# Decision: Keep the order and flag it for investigation during Data Cleaning.
# Do not create or impute a payment record.

### Delivered orders must have order items ###

# Identify delivered orders that do not have any order-item records.
delivered_without_items = delivered_orders[
    ~delivered_orders["order_id"].isin(order_items["order_id"])
]

print(
    "Delivered orders without items:",
    delivered_without_items["order_id"].nunique()
)
### Delivered orders must have order items - Conclusion ###
# All delivered orders have at least one associated order item.
# No business rule violation was identified.
# Decision: No action required.


### Payment total vs Order value ###
# Calculate the total item price for each order.
item_totals = (
    order_items
    .groupby("order_id")["price"]
    .sum()
)

# Calculate the total freight value for each order.
freight_totals = (
    order_items
    .groupby("order_id")["freight_value"]
    .sum()
)

# Calculate the expected order value.
expected_order_value = item_totals + freight_totals

# Calculate the total payment recorded for each order.
payment_totals = (
    payments
    .groupby("order_id")["payment_value"]
    .sum()
)

# Combine expected order value and payment totals.
payment_check = pd.DataFrame({
    "expected_order_value": expected_order_value,
    "total_payment": payment_totals
})

# Calculate the difference between payment and expected order value.
payment_check["difference"] = (
    payment_check["total_payment"]
    - payment_check["expected_order_value"]
)

# Calculate the absolute difference for identifying significant mismatches.
payment_check["absolute_difference"] = (
    payment_check["difference"].abs()
)

# Display orders with the largest payment differences.
print(
    payment_check[
        ["expected_order_value", "total_payment", "difference"]
    ]
    .sort_values("difference", key=abs, ascending=False)
    .head(20)
)
### Payment mismatch - Detailed investigation ###
# Select the order with the largest payment difference.
largest_mismatch_order = payment_check[
    payment_check["absolute_difference"] ==
    payment_check["absolute_difference"].max()
].index[0]
# Display the order's item records.
print("Order items:")
print(
    order_items[
        order_items["order_id"] == largest_mismatch_order
    ]
)
# Display the order's payment records.
print("\nPayments:")
print(
    payments[
        payments["order_id"] == largest_mismatch_order
    ]
)
### Payment mismatch - Order item investigation ###
# Display the item records for the largest payment mismatch.
print(
    order_items[
        order_items["order_id"] == largest_mismatch_order
    ][
        ["order_id", "order_item_id", "product_id", "price", "freight_value"]
    ]
)
### Payment total vs Order value - Conclusion ###
# 381 orders have payment totals that differ from
# item price + freight by more than 0.01.
# Most of these mismatches (375) belong to delivered orders.
# The available fields do not provide sufficient evidence
# to classify the differences as incorrect transactions.
# Decision: Keep the original values and flag the mismatches
# for further investigation during Data Cleaning.

### Payment mismatch - Order status analysis ###
# Add order status to the payment reconciliation table.
payment_check_with_status = payment_check.merge(
    orders[["order_id", "order_status"]],
    on="order_id",
    how="left"
)
# Show the status distribution of orders with significant payment differences.
print(
    payment_check_with_status[
        payment_check_with_status["absolute_difference"] > 0.01
    ]["order_status"].value_counts()
)

### Review date must be after purchase date ###
# Convert review creation date to datetime.
reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)
# Create a lookup of order purchase dates.
order_purchase_dates = orders[
    ["order_id", "purchase_date"]
]
# Combine review records with their order purchase date.
review_timing = reviews.merge(
    order_purchase_dates,
    on="order_id",
    how="left"
)
# Identify reviews created before the order was purchased.
reviews_before_purchase = review_timing[
    review_timing["review_creation_date"] < review_timing["purchase_date"]
]
print(
    "Reviews created before purchase:",
    len(reviews_before_purchase)
)
### Review timing - Conclusion ###
# 74 reviews have a creation date earlier than the
# corresponding order purchase date.
# This violates the expected business timeline because
# a review should normally occur after the order is purchased.
# Decision: Keep the original dates and flag these 74 records
# for investigation during Data Cleaning.

### Review answer must be after review creation ###
# Identify reviews where the answer timestamp
# occurs before the review creation date.
reviews_before_answer = review_timing[
    review_timing["review_answer_timestamp"] < review_timing["review_creation_date"]
]
print(
    "Reviews answered before creation:",
    len(reviews_before_answer)
)
### Review answer timing - Conclusion ###
# No reviews have an answer timestamp earlier than
# the review creation date.
# The review answer timeline is consistent.
# Decision: No action required.

### Shipping limit date must be after purchase date ###
# Identify orders where the shipping limit date
# occurs before the purchase date.
shipping_before_purchase = order_items[
    pd.to_datetime(
        order_items["shipping_limit_date"],
        errors="coerce"
    ) < order_items["order_id"].map(
        orders.set_index("order_id")["purchase_date"]
    )
]
print(
    "Shipping limit before purchase:",
    len(shipping_before_purchase)
)
### Shipping limit date - Conclusion ###
# No orders have a shipping limit date earlier than
# the purchase date.
# The shipping timeline is consistent.
# Decision: No action required.

### Delivered orders must have approval date ###
# Identify delivered orders where the approval date is missing.
delivered_without_approval = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_approved_at"].isna())
]
print(
    "Delivered orders without approval date:",
    len(delivered_without_approval)
)
### Delivered orders without approval date - Conclusion ###
# 14 delivered orders do not have an approval date.
# This violates the expected order lifecycle because a delivered
# order should normally have an approval record.
# Decision: Keep the orders and flag these 14 records for investigation
# during Data Cleaning. Do not impute an approval date.


### Business Rule Validation - Summary ###

# Order lifecycle validation:
# 0 orders had approval before purchase.
# 1,359 orders had carrier date before approval.
# 23 orders had customer delivery before carrier date.
#
# Delivered order validation:
# 14 delivered orders had no approval date.
# 2 delivered orders had no carrier date.
# 8 delivered orders had no customer delivery date.
# 1 delivered order had no payment record.
# 0 delivered orders had no order items.
#
# Review validation:
# 74 reviews were created before the corresponding purchase date.
# 0 reviews had an answer timestamp before the review creation date.
#
# Shipping validation:
# 0 orders had a shipping limit date before the purchase date.
#
# Payment reconciliation:
# 381 orders had payment totals differing from calculated
# order value (item price + freight) by more than 0.01.
# These differences require investigation and were not classified
# as invalid transactions.
#
# Overall conclusion:
# Most business rules passed successfully.
# A small number of timeline, completeness, and payment reconciliation
# anomalies were identified.
# Original values will be preserved, and suspicious records will be
# flagged for investigation during Data Cleaning.