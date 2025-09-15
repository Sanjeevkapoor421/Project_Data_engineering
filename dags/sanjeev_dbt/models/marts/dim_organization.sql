{{ config(
    materialized='table',
    schema='marts'
) }}

SELECT
    organization
FROM {{ ref('yelp_base_data') }}
GROUP BY organization
ORDER BY organization
