SELECT 
  order_id,
  order_item_id,
  DATE(order_date) order_date,
  order_customer_id customer_id,
  order_status status,
  order_item_product_id product_id,
  order_item_quantity quantity,
  order_item_subtotal subtotal
FROM {{ source('retail_db', 'orders') }} o
JOIN {{ source('retail_db', 'order_items') }} oi ON oi.order_item_order_id = o.order_id

