SELECT 
    customer_id,
    customer_fname,
    customer_lname,
    customer_city,
    customer_state
FROM {{ source('retail_db', 'customers') }}
