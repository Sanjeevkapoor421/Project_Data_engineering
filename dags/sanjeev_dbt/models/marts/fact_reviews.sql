{{ config(
    materialized='table',
    schema='marts'  )
    }}

SELECT
    id,
    time_gmt,
    category,
    city,
    organization,
    rating,
    number_review
FROM {{ ref('yelp_base_data') }}
WHERE rating IS NOT NULL
  AND number_review IS NOT NULL
  AND category IS NOT NULL
  AND city IS NOT NULL
  AND organization IS NOT NULL
  AND time_gmt IS NOT NULL