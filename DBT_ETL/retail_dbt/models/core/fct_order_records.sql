WITH customers AS (
    SELECT 
        customer_id,
        customer_city,
        customer_state
    FROM {{ ref('stg_customers') }}
),

orders AS (
    SELECT 
        order_id,
        customer_id,
        order_date,
        status,
        sum(quantity) product_quantity,
        sum(subtotal) order_amount
    FROM {{ ref('stg_orders') }}
    GROUP BY 1,2,3,4
)

SELECT 
    order_id,
    customer_state state,
    customer_city city,
    order_date,
    status,
    product_quantity,
    order_amount
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id