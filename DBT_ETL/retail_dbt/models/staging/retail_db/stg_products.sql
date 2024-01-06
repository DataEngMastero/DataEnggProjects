SELECT 
  product_id,
  product_name,
  product_price,
  product_image,
  category_name,
  department_name
FROM {{ source('retail_db','products') }} p
LEFT JOIN {{ source('retail_db','categories') }} c ON p.product_category_id = c.category_id
LEFT JOIN {{ source('retail_db','departments') }} d ON c.category_department_id = d.department_id
