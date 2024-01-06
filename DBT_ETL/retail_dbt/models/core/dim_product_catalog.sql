WITH products AS (
    SELECT
        product_id,
        product_name,
        category_name,
        department_name
    FROM {{ ref('stg_products') }}
),

orders AS (
    SELECT 
        product_id,
        sum(quantity) lifetime_products,
        sum(subtotal) lifetime_value,
        count(order_id) number_of_orders
    FROM {{ ref('stg_orders') }}
    GROUP BY 1
)

SELECT 
    p.product_id,
    product_name,
    category_name,
    department_name,
    lifetime_value,
    lifetime_products,
    coalesce(number_of_orders, 0) as number_of_orders
FROM products p
LEFT JOIN orders o ON o.product_id = p.product_id