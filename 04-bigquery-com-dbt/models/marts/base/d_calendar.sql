{{ config(materialized='table') }}

with date_spine as (
    select
        date
    from unnest(
        generate_date_array('2020-01-01', '2030-12-31')
    ) as date
)

select
    date as date_day,

    extract(year from date) as year,
    extract(month from date) as month,
    extract(day from date) as day,
    extract(quarter from date) as quarter,

    format_date('%A', date) as day_name,
    format_date('%B', date) as month_name,

    extract(isoweek from date) as week_of_year,
    extract(dayofweek from date) as day_of_week,

    case
        when extract(dayofweek from date) in (1, 7) then true
        else false
    end as is_weekend
from date_spine
