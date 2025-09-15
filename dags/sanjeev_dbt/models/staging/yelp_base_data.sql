{{ config(
    materialized='table',
) }}

SELECT
    CAST("ID" AS NUMBER)                       AS id,
    TO_TIMESTAMP("Time_GMT",'MM/DD/YYYY HH24:MI')                   AS time_gmt,
    CAST("Phone" AS STRING)                    AS phone,
    CAST("Organization" AS STRING)             AS organization,
  --  CAST("OLF" AS STRING)                      AS olf,
    CAST("Rating" AS FLOAT)                    AS rating,
    CAST("NumberReview" AS NUMBER)             AS number_review,
    CAST("Category" AS STRING)                 AS category,
    CAST("Country" AS STRING)                  AS country,
    CAST("CountryCode" AS STRING)              AS country_code,
    CAST("State" AS STRING)                    AS state,
    CAST("City" AS STRING)                     AS city,
    CAST("Street" AS STRING)                   AS street,
    CAST("Building" AS STRING)                 AS building
FROM {{ source('staging', 'yelp_raw_data') }}
