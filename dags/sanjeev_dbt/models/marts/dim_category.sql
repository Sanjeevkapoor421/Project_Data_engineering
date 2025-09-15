{{ config(
    materialized='table',
    schema='marts'
) }}

SELECT
    category AS category_name
FROM {{ ref('yelp_base_data') }}
GROUP BY category
ORDER BY category
