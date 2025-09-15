{{ config(
    materialized='table',
    schema='reporting'
) }}

SELECT
    DATE_TRUNC('day', time_gmt) AS date,
    city,
    category,
    COUNT(*) AS total_reviews,
    AVG(rating) AS avg_rating,
    COUNT(DISTINCT organization) AS total_organizations,
    EXTRACT(DAYOFWEEKISO FROM time_gmt) AS day_of_week, 
    CASE WHEN EXTRACT(DAYOFWEEKISO FROM time_gmt) IN (6,7) THEN 1 ELSE 0 END AS is_weekend,
    EXTRACT(MONTH FROM time_gmt) AS month
FROM {{ ref('fact_reviews') }}
GROUP BY
    date,
    city,
    category,
    day_of_week,
    is_weekend,
    month
ORDER BY
    date,
    city,
    category
