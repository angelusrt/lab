import kagglehub

customers_file = "olist_customers_dataset.csv"
geolocation_file = "olist_geolocation_dataset.csv"
order_items_file = "olist_order_items_dataset.csv"
order_payments_file = "olist_order_payments_dataset.csv"
order_review_file = "olist_order_reviews_dataset.csv"
orders_file = "olist_orders_dataset.csv"
products_file = "olist_products_dataset.csv"
sellers_file = "olist_sellers_dataset.csv"
category_name_file = "product_category_name_translation.csv"

path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

print("Path to dataset files:", path)

