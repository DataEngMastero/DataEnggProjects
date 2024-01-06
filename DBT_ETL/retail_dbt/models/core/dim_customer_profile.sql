WITH customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

customer_orders AS (
    SELECT 
        customer_id,
        min(order_date) first_order_date,
        max(order_date) most_recent_order_date,
        sum(quantity) lifetime_products,
        sum(subtotal) lifetime_value,
        count(order_id) number_of_orders
    FROM {{ ref('stg_orders') }}
    GROUP BY 1
)

SELECT 
    c.customer_id,
    customer_fname,
    customer_lname,
    first_order_date,
    most_recent_order_date,
    lifetime_value,
    lifetime_products,
    coalesce(number_of_orders, 0) as number_of_orders
FROM customers c
LEFT JOIN customer_orders co ON co.customer_id = c.customer_id

