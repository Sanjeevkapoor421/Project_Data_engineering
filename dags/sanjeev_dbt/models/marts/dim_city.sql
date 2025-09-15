{{ config(
    materialized='table',
    schema='marts'
) }}

SELECT
    city,
    state,
    country,
    country_code
FROM {{ ref('yelp_base_data') }}
GROUP BY city, state, country, country_code
ORDER BY country, state, city