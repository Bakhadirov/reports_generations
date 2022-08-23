-- В настоящем скрипте необходимо менять необходимые для получения данные
-- на 9 и 10 строке. Даты построения отчета, media_source и campaign
with a as (
    select
        campaign ,
        sum(event_revenue) as event_revenue_sum,
        sum(event_revenue_usd) as event_revenue_usd_sum from events e
        where e.event_time::date between '2020-06-11' and '2020-06-11' and e.media_source = 'googleadwords_int'
    group by campaign
),
b as (
    select
        campaign,
        count(event_name) as count_installs
    from installs1 i
    group by campaign
)
select *
from a
left join b
on a.campaign = b.campaign